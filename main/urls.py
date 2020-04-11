from django.urls import path

from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home'),
    url(r'^relative/$', views.relative, name = 'relative'),
    url(r'^other/$', views.other, name = 'other'),
]
