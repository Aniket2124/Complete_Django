"""view_class_advanced URL Configuration

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
from django.urls import path
from school import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('home1/',views.HomeView.as_view(),name='home1'),
    path('about/',views.about,name='about'),
    path('about1/',views.AboutClassView.as_view(),name='about1'),
    path('contact/',views.contactform,name='contact'),
    path('contact1/',views.ContactClassView.as_view(),name='contact1'),
    # path('news/',views.newsfunction,name='news'),
    path('news/',views.newsfunction,{'template_name':'school/news.html'},name='news'),
    path('news2/',views.newsfunction,{'template_name':'school/news2.html'},name='news2'),
    # path('newscl/',views.NewsClassView.as_view(),name='newscl'),
    path('newscl/',views.NewsClassView.as_view(template_name='school/news.html'),name='newscl'),
    path('newscl2/',views.NewsClassView.as_view(template_name='school/news2.html'),name='newscl2'),
]
