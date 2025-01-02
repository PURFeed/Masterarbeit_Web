#Author: Phillipp Gohlke
#Last Edit: 02.01.2025
#View for the Web-Application

"""
URL configuration for Masterarbeit_Mitre_Attack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from oberflaeche import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'), #Path for the Home-Page

    path('index/', views.index, name='index'), #Path for the Saved Index

    path('index_result/', views.index_result, name='index_result'), #Path for the Index-Entry

    path('results/', views.results_for_keyword, name='results'), #Path for the Search Results

    path('import/', views.import_data, name='import') #Path to Import the Data Entries

]
