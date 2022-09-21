"""genericviews URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from Books import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('api',views.Studentviewset,basename='student')

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include(router.urls)),


]







# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/',views.StudentList.as_view()),
#     path('add/',views.StudentCreate.as_view()),
#     path('retrieve/<int:pk>/',views.StudentRetrieve.as_view()),
#     path('update/<int:pk>/',views.StudentUpdate.as_view()),
#     path('destroy/<int:pk>/',views.StudentDestroy.as_view()),
#     path('listcreate',views.Studentlistcreate.as_view()),
#     path('retriveupdate/<int:pk>/',views.Studentretriveupdate.as_view()),
#     path('retrivedesrtoy/<int:pk>/',views.Studentretrivedestroy.as_view()),
#     path('retriveupdatedesrtoy/<int:pk>/',views.Studentretriveupdatedestroy.as_view()),
# ]
