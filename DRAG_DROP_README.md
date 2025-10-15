# Sistema de Upload com Drag and Drop

## Funcionalidades Implementadas

### 1. Drag and Drop (Arrastar e Soltar)
- **Arrastar arquivos**: Você pode arrastar arquivos de imagem diretamente para a área de upload
- **Feedback visual**: A área muda de cor quando você arrasta um arquivo sobre ela
- **Validação**: Apenas arquivos de imagem são aceitos

### 2. Clique para Selecionar
- **Upload tradicional**: Clique na área de upload para abrir o seletor de arquivos
- **Compatibilidade**: Funciona em todos os navegadores

### 3. Preview da Imagem
- **Visualização**: Mostra uma prévia da imagem selecionada
- **Informações**: Exibe o nome do arquivo
- **Remoção**: Botão para remover o arquivo selecionado

### 4. Validações de Segurança
- **Tipo de arquivo**: Apenas imagens são aceitas (jpg, png, gif, etc.)
- **Tamanho**: Limite máximo de 10MB por arquivo
- **Proteção CSRF**: Token de segurança incluído

### 5. Feedback ao Usuário
- **Indicador de progresso**: Spinner durante o upload
- **Mensagens de sucesso**: Confirmação quando o upload é concluído
- **Mensagens de erro**: Alertas em caso de problemas

## Como Usar

### 1. Arrastar e Soltar
1. Abra a página inicial do EduVision IA
2. Arraste uma imagem do seu computador
3. Solte sobre a área azul "Envie uma foto"
4. Aguarde o upload ser concluído

### 2. Clique para Selecionar
1. Clique na área "Envie uma foto"
2. Selecione uma imagem no seletor de arquivos
3. Aguarde o upload ser concluído

### 3. Remover Arquivo
- Clique no botão "×" no canto superior direito da prévia
- A área voltará ao estado inicial

## Arquivos Criados/Modificados

### JavaScript
- `static/js/home.js` - Lógica principal do drag and drop

### CSS
- `static/styles/style.css` - Estilos para drag and drop, preview e mensagens

### Python
- `home/views.py` - View para processar o upload
- `home/urls.py` - Rota para o upload

### HTML
- `templates/home/index-desktop.html` - Inclusão do script e token CSRF

### Estrutura de Diretórios
- `media/uploads/temp/` - Pasta para arquivos temporários

## Configurações de Segurança

### Validações Implementadas
- Verificação de tipo MIME
- Limite de tamanho (10MB)
- Nomes únicos para arquivos (UUID)
- Token CSRF obrigatório

### Tipos de Arquivo Aceitos
- JPEG (.jpg, .jpeg)
- PNG (.png)
- GIF (.gif)
- WebP (.webp)
- BMP (.bmp)

## Próximos Passos Sugeridos

1. **Integração com IA**: Conectar o upload com o sistema de análise de gráficos
2. **Histórico**: Salvar arquivos no histórico do usuário
3. **Múltiplos arquivos**: Permitir upload de vários arquivos simultâneos
4. **Compressão**: Reduzir tamanho das imagens automaticamente
5. **Banco de dados**: Salvar informações dos uploads no banco

## Estrutura do Código

### Fluxo de Upload
1. Usuário seleciona/arrasta arquivo
2. JavaScript valida tipo e tamanho
3. Exibe preview da imagem
4. Envia arquivo para Django via AJAX
5. Django processa e salva o arquivo
6. Retorna resposta JSON
7. JavaScript exibe feedback ao usuário

### Eventos JavaScript
- `dragenter`, `dragover`: Destacar área de drop
- `dragleave`, `drop`: Remover destaque
- `drop`: Processar arquivo solto
- `change`: Processar arquivo selecionado

### Estilos CSS
- `.drag-drop-area`: Estilo base da área
- `.drag-over`: Estilo quando arquivo está sendo arrastado
- `.has-file`: Estilo quando arquivo foi selecionado
- `.file-preview`: Layout do preview da imagem

## Suporte a Mobile

O sistema funciona tanto no desktop quanto no mobile:
- **Desktop**: Drag and drop + clique
- **Mobile**: Clique para abrir câmera/galeria

## Testando o Sistema

1. Inicie o servidor Django: `python manage.py runserver`
2. Acesse a página inicial
3. Teste arrastar uma imagem
4. Teste clicar na área para selecionar
5. Verifique se mensagens aparecem corretamente