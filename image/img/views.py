from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.http.response import HttpResponseBase
# Create your views here.
from django.views import View

from img.models import Img


class Index(View):
    def get(self, request):
        return render(request, 'index.html')



class UploadImg(View):
    def get(self, request):

        return render(request, 'imgupload.html')

    def post(self,request): # 图片上传函数
        img_url = request.FILES.get('img')
        print(img_url)
        img = Img(img_url=img_url)
        img.save()
        return render(request, 'imgupload.html')


class ShowImg(View):
    def get(self, request):
        imgs = Img.objects.all()  # 从数据库中取出所有的图片路径
        context = {
            'imgs': imgs
        }
        return render(request, 'showimg.html', context)


