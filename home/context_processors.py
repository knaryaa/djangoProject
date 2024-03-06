from .models import Setting

def setting(request):
    setting = Setting.objects.get(pk=1)
    if setting:
        return {'settings': setting}