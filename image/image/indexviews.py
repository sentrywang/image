from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.http.response import HttpResponseBase
# Create your views here.
from django.views import View
import os



class Index(View):
    def get(self, request):
        context = {}
        for imgs in os.walk('media/img'):
            
            context = {
                'imgs': imgs
            }
        return render(request, 'index.html', context)
