from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import os
from contas.models import userProfile
from home.EduVision_IA.main import import_img, cut_image
from home.EduVision_IA.graph_creator import graficoobj


# Create your views here.
@login_required
def index(request):
    # Detecta user agent para mobile
    try:
        user_profile = userProfile.objects.get(user_id=request.user.id)
    except userProfile.DoesNotExist:
        user_profile = None
    context = {
        'user_profile': user_profile
    }
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    is_mobile = any(device in user_agent for device in ['mobile', 'android', 'iphone'])
    if is_mobile:
        return render(request, 'home/index-mobile.html',context)
    else:
        return render(request, 'home/index-desktop.html',context)


@login_required
@require_http_methods(["POST"])
def upload_file(request):
    try:
        if 'file' not in request.FILES:
            return JsonResponse({
                'success': False,
                'error': 'Nenhum arquivo foi enviado'
            }, status=400)
        
        uploaded_file = request.FILES['file']
        
        # Verificar se é uma imagem
        if not uploaded_file.content_type.startswith('image/'):
            return JsonResponse({
                'success': False,
                'error': 'Apenas arquivos de imagem são permitidos'
            }, status=400)
        
        # Verificar tamanho do arquivo (máximo 10MB)
        max_size = 10 * 1024 * 1024  # 10MB
        if uploaded_file.size > max_size:
            return JsonResponse({
                'success': False,
                'error': 'Arquivo muito grande. Máximo permitido: 10MB'
            }, status=400)
        
        # Criar diretório de uploads se não existir
        upload_dir = os.path.join('media', 'uploads', 'temp')
        os.makedirs(upload_dir, exist_ok=True)
        
        # Gerar nome único para o arquivo
        import uuid
        file_extension = os.path.splitext(uploaded_file.name)[1]
        unique_filename = f"{uuid.uuid4()}{file_extension}"
        file_path = os.path.join(upload_dir, unique_filename)
        
        # Salvar arquivo
        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        image, nome_arquivo = import_img(file_path)
        cut_image(image, nome_arquivo)
        return JsonResponse({
            'success': True,
            'message': 'Arquivo enviado com sucesso',
            'file_name': uploaded_file.name,
            'file_size': uploaded_file.size,
            'file_path': file_path
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': f'Erro interno do servidor: {str(e)}'
        }, status=500)    