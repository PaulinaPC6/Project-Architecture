from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse  
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("DJANGO 🚀 The install worked successfully! Congratulations!")

def health_check(request):
    return JsonResponse({"status": "healthy", "service": "backend"})

urlpatterns = [
    path('', home_view, name='home'),
    path('health/', health_check, name='health_check'),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
]
