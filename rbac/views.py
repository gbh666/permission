from django.shortcuts import render,redirect
from . import models



from django.forms import ModelForm
from django.forms import Widget as wit
from django.forms import fields as fld

class UserModelForm(ModelForm):

    class Meta:
        model = models.UserInfo
        fields = "__all__"
        labels = {
            'username':'用户名',
            'nickname':'昵称',
            'password':'密码',
            'email':'邮箱',
            'roles':'角色'
        }

class RoleModelForm(ModelForm):
    class Meta:
        model = models.Role
        fields = "__all__"
        labels = {
            'name':'角色名',
            'permissions':'权限'
        }

class PermissionModelForm(ModelForm):
    class Meta:
        model = models.Permission
        fields = "__all__"

class MenuModelForm(ModelForm):
    class Meta:
        model = models.Menu
        fields = "__all__"

def users(request):
    '''
    全部角色
    :param request: 
    :return: 
    '''

    user_list = models.UserInfo.objects.all()

    return render(request,'rbac/users.html',{'user_list':user_list})

def user_add(request):
    '''
    添加用户
    :param request: 
    :return: 
    '''
    if request.method == "GET":
        model_form = UserModelForm()
        return render(request,'rbac/user_add.html',{'model_form':model_form})
    else:
        model_form = UserModelForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            return redirect('/rbac/users.html')

    return render(request,'rbac/user_add.html',{"model_form":model_form})

def user_edit(request,pk):
    '''编辑用户'''

    user_obj = models.UserInfo.objects.filter(pk=pk).first()
    if not user_obj:
        return redirect('/rbac/users.html')
    if request.method == 'GET':
        model_form = UserModelForm(instance=user_obj)
        return render(request,'rbac/user_edit.html',{"model_form":model_form})
    else:
        model_form = UserModelForm(request.POST,instance=user_obj)
        if model_form.is_valid():
            model_form.save()
            return redirect('/rbac/users.html')

        return render(request,'rbac/user_edit.html')

def user_del(request,pk):
    '''
    删除用户
    :param request: 
    :param pk: 
    :return: 
    '''
    models.UserInfo.objects.filter(pk=pk).first().delete()

    return redirect('/rbac/users.html')

def roles(request):

    role_list = models.Role.objects.all()

    return render(request,'rbac/roles.html',{'role_list':role_list})

def role_add(request):
    '''
    添加角色
    :param request: 
    :return: 
    '''
    if request.method == "GET":
        model_form = RoleModelForm()
        return render(request,'rbac/role_add.html',{'model_form':model_form})
    else:
        model_form = RoleModelForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            return redirect('/rbac/roles.html')

    return render(request,'rbac/role_add.html',{"model_form":model_form})

def role_edit(request,pk):
    '''编辑角色'''

    role_obj = models.Role.objects.filter(pk=pk).first()
    if not role_obj:
        return redirect('/rbac/roles.html')
    if request.method == 'GET':
        model_form = RoleModelForm(instance=role_obj)
        return render(request,'rbac/role_edit.html',{"model_form":model_form})
    else:
        model_form = RoleModelForm(request.POST,instance=role_obj)
        if model_form.is_valid():
            model_form.save()
            return redirect('/rbac/roles.html')

        return render(request,'rbac/role_edit.html')

def role_del(request,pk):
    '''
    删除角色
    :param request: 
    :param pk: 
    :return: 
    '''
    models.Role.objects.filter(pk=pk).first().delete()

    return redirect('/rbac/roles.html')

def permissions(request):
    permission_list = models.Permission.objects.all()

    return render(request,'rbac/permissions.html',{'permission_list':permission_list})

def permission_add(request):
    '''
    添加权限
    :param request: 
    :return: 
    '''
    if request.method == "GET":
        model_form = PermissionModelForm()
        return render(request,'rbac/permission_add.html',{'model_form':model_form})
    else:
        model_form = PermissionModelForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            return redirect('/rbac/permissions.html')

    return render(request,'rbac/permission_add.html',{"model_form":model_form})

def permission_edit(request,pk):
    '''编辑权限'''

    permission_obj = models.Permission.objects.filter(pk=pk).first()
    if not permission_obj:
        return redirect('/rbac/permissions.html')
    if request.method == 'GET':
        model_form = PermissionModelForm(instance=permission_obj)
        return render(request,'rbac/permission_edit.html',{"model_form":model_form})
    else:
        model_form = PermissionModelForm(request.POST,instance=permission_obj)
        if model_form.is_valid():
            model_form.save()
            return redirect('/rbac/permissions.html')

        return render(request,'rbac/permission_edit.html')

def permission_del(request,pk):
    '''
    删除权限
    :param request: 
    :param pk: 
    :return: 
    '''
    models.Permission.objects.filter(pk=pk).first().delete()

    return redirect('/rbac/permissions.html')


def menus(request):
    menu_list = models.Menu.objects.all()

    return render(request, 'rbac/menus.html', {'menu_list': menu_list})


def menu_add(request):
    '''
    添加菜单
    :param request: 
    :return: 
    '''
    if request.method == "GET":
        model_form = MenuModelForm()
        return render(request, 'rbac/menu_add.html', {'model_form': model_form})
    else:
        model_form = MenuModelForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            return redirect('/rbac/menus.html')

    return render(request, 'rbac/menu_add.html', {"model_form": model_form})


def menu_edit(request, pk):
    '''编辑菜单'''

    menu_obj = models.Menu.objects.filter(pk=pk).first()
    if not menu_obj:
        return redirect('/rbac/menus.html')
    if request.method == 'GET':
        model_form = MenuModelForm(instance=menu_obj)
        return render(request, 'rbac/menu_edit.html', {"model_form": model_form})
    else:
        model_form = MenuModelForm(request.POST, instance=menu_obj)
        if model_form.is_valid():
            model_form.save()
            return redirect('/rbac/menus.html')

        return render(request, 'rbac/menu_edit.html')


def menu_del(request, pk):
    '''
    删除菜单
    :param request: 
    :param pk: 
    :return: 
    '''
    models.Menu.objects.filter(pk=pk).first().delete()

    return redirect('/rbac/menus.html')