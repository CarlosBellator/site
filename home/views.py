from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from contas.models import userProfile

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