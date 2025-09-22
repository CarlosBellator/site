from django.shortcuts import render

# Create your views here.
def index(request):
    # Detecta user agent para mobile
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    is_mobile = any(device in user_agent for device in ['mobile', 'android', 'iphone'])
    print(f"User Agent: {user_agent}, Is Mobile: {is_mobile}")
    if is_mobile:
        return render(request, 'home/index-mobile.html')
    else:
        return render(request, 'home/index-desktop.html')