"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.crud_a, name='crud_a'),
    path('adddata_crud_a',views.adddata_crud_a,name='adddata_crud_a'),
    path('editdata_crud_a/<int:id>',views.editdata_crud_a,name='editdata_crud_a'),
    path('deletedata_crud_a/<int:id>',views.deletedata_crud_a,name='deletedata_crud_a'),

    path('crud_b', views.crud_b, name='crud_b'),
    path('adddata_crud_b', views.adddata_crud_b, name='adddata_crud_b'),
    path('editdata_crud_b/<int:id>', views.editdata_crud_b, name='editdata_crud_b'),
    path('deletedata_crud_b/<int:id>', views.deletedata_crud_b, name='deletedata_crud_b'),

    path('crud_c', views.crud_c, name='crud_c'),
    path('adddata_crud_c',views.adddata_crud_c,name='adddata_crud_c'),
    path('editdata_crud_c/<int:id>',views.editdata_crud_c,name='editdata_crud_c'),
    path('deletedata_crud_c/<int:id>',views.deletedata_crud_c,name='deletedata_crud_c'),

    path('crud_d', views.crud_d, name='crud_d'),
    path('adddata_crud_d',views.adddata_crud_d,name='adddata_crud_d'),
    path('editdata_crud_d/<int:id>',views.editdata_crud_d,name='editdata_crud_d'),
    path('deletedata_crud_d/<int:id>',views.deletedata_crud_d,name='deletedata_crud_d')
    
]
