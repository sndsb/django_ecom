from generalSetting.models import GeneralSetting

def general_setting(request):
    generalSetting = GeneralSetting.objects.first()
    
    context = {
        'general_setting' : generalSetting
    }
    
    return context