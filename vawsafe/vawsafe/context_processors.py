from django.utils import timezone

def current_datetime(request):
    print("context processor called at", timezone.now())
    return {
        'current_datetime': timezone.now()
    }