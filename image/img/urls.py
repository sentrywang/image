from django.urls import path

from . import views

urlpatterns = [
    path('uploadimg/', views.UploadImg.as_view()),
    path('showimg/', views.ShowImg.as_view()),

]