from django.core.files.storage import Storage
from django.core.files.base import ContentFile
from django.conf import settings
from supabase import create_client
import io

class SupabaseStorage(Storage):
    """
    Backend simples para usar Supabase Storage com Django.
    - Requer as vars: SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, SUPABASE_BUCKET
    - Para arquivos privados, usamos signed URLs; para públicos, retornamos URL pública.
    Ajuste conforme as APIs do supabase-py na versão que você usar.
    """
    def __init__(self):
        url = settings.SUPABASE_URL
        key = settings.SUPABASE_SERVICE_ROLE_KEY  # use service role key no server
        self.bucket = getattr(settings, "SUPABASE_BUCKET", "public")
        self.client = create_client(url, key)

    def _open(self, name, mode='rb'):
        # Baixa o arquivo e retorna um arquivo-like
        # Dependendo da versão do SDK, use client.storage.from_(bucket).download(name)
        data = self.client.storage.from_(self.bucket).download(name)
        # data pode ser bytes ou uma resposta; adapte conforme SDK
        if isinstance(data, bytes):
            return io.BytesIO(data)
        # se SDK retorna um objeto com .content:
        try:
            return io.BytesIO(data.content)
        except Exception:
            return io.BytesIO(data)

    def _save(self, name, content):
        # content é um File object do Django
        # Ler bytes
        content.seek(0)
        data = content.read()
        # A API do supabase-py costuma aceitar bytes/file-like
        # Upload; o caminho usado aqui é o 'name'
        # Atenção: se o arquivo já existir, pode ocorrer erro — você pode primeiro deletar.
        self.client.storage.from_(self.bucket).upload(name, data)
        return name

    def exists(self, name):
        # Tenta obter estatísticas / metadata; se exibir erro 404, retorna False
        try:
            meta = self.client.storage.from_(self.bucket).list(path=name, limit=1)
            # Dependendo do retorno do SDK, ajuste a checagem
            return bool(meta)
        except Exception:
            return False

    def url(self, name):
        # Para arquivos públicos:
        # public_url = f"{settings.SUPABASE_URL}/storage/v1/object/public/{self.bucket}/{name}"
        # return public_url
        # Para privados (signed url):
        expires_in = getattr(settings, "SUPABASE_SIGNED_URL_EXPIRES_IN", 3600)  # segs
        try:
            # Algumas versões: client.storage.create_signed_url(bucket, path, expires_in)
            signed = self.client.storage.create_signed_url(self.bucket, name, expires_in)
            return signed.get("signedURL") if isinstance(signed, dict) else signed
        except Exception:
            # fallback para URL pública (se o bucket for público)
            return f"{settings.SUPABASE_URL}/storage/v1/object/public/{self.bucket}/{name}"

    def delete(self, name):
        try:
            self.client.storage.from_(self.bucket).remove([name])
        except Exception:
            pass

    def size(self, name):
        # Se precisar do tamanho, tente pegar metadata
        try:
            meta = self.client.storage.from_(self.bucket).get_public(name)
            # Ajuste conforme retorno do SDK
            return meta and meta.get("size", 0)
        except Exception:
            return 0