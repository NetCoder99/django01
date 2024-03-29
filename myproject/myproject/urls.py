from django.contrib import admin
from django.contrib.auth import views as auth_views

#from django.conf.urls import url
from django.urls import re_path as url
from django.urls import path
from boards import views as boards_views
from accounts import views as accounts_views

urlpatterns = [
    url(r'^$', boards_views.home, name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),    
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^boards/(?P<pk>\d+)/$', boards_views.board_topics, name='board_topics'),    
    url(r'^boards/(?P<pk>\d+)/new/$', boards_views.new_topic, name='new_topic'),    
    path('admin/', admin.site.urls),
]
