from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^users.html$', views.users),
    url(r'^user/add.html$', views.user_add),
    url(r'^user/edit/(\d+).html$', views.user_edit),
    url(r'^user/del/(\d+).html$', views.user_del),
    url(r'^roles.html$', views.roles),
    url(r'^role/add.html$', views.role_add),
    url(r'^role/edit/(\d+).html$', views.role_edit),
    url(r'^role/del/(\d+).html$', views.role_del),
    url(r'^permissions.html$', views.permissions),
    url(r'^permission/add.html$', views.permission_add),
    url(r'^permission/edit/(\d+).html$', views.permission_edit),
    url(r'^permission/del/(\d+).html$', views.permission_del),
    url(r'^menus.html$', views.menus),
    url(r'^menu/add.html$', views.menu_add),
    url(r'^menu/edit/(\d+).html$', views.menu_edit),
    url(r'^menu/del/(\d+).html$', views.menu_del),
]
