"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    #  path('admin/', admin.site.urls),
    # path('', views.hello, name='hello'),
    # path('display/', views.display),
    # path('welcome/', views.welcome),
    # path('student/<int:id>/', views.student,name="student"),
    # path('student/<int:id>/<str:name>/',views.studentname,name="student"),
    # path('students/', views.students, name="students"),
    
    # day 2
    #path('studentsprofile/', views.studentprofile,name="student"),
    
    # day  3
    #path('studentform/',views.studentform,name="studentform"),
    #path('studentformget/',views.studentformget,name="studentformget"),
    
    # day 7
    
    path("",views.student_list,name="students"),
    path("create/",views.create_student,name="create"),
    path("update/<int:id>/",views.update_student,name="update"),
    path("delete/<int:id>/",views.delete_student,name="delete"),
   
   
    
    
    
   
   
    
]


