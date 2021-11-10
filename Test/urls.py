"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import json
from django import urls
from django.contrib import admin
from django.http import response
from django.http.response import HttpResponse, JsonResponse
from django.urls import path
from django.http import request

def view(request):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }

    r = request.get("https://www.uuidtools.com/api/generate/v1/count/100")
    r.status_code == 200
    response.raise_for_status()  # raises exception when not a 2xx response
    if response.status_code != 204:
        return response.json()
    # if r.status_code == 200: 
    #     data = r.json()

    # else:
    #     data = {"success": "false"}
       
    # return JsonResponse(data = data,status=200,safe=False)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",view)
]