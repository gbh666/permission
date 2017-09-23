#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Sam"
# Date: 2017/9/21

from django.conf import settings
from .. import models


def init_permission(request, user_obj):
    '''
    初始化用户权限
    :param request: 
    :param user_obj: 
    :return: 
    '''

    permission_item_list = user_obj.roles.values('permissions__title', 'permissions__url',
                                                 'permissions__menu_id').distinct()

    # 保存当前用户有权访问的URL
    permission_url_list = []

    # 保存当前用户有权访问且需要在菜单上显示的url
    permission_menu_list = []

    for item in permission_item_list:
        permission_url_list.append(item["permissions__url"])
        # 把需要在菜单上显示的权限添加到权限菜单列表中
        if item["permissions__menu_id"]:
            temp = {'title': item['permissions__title'], 'url': item['permissions__url'],
                    'menu_id': item['permissions__menu_id']}
            permission_menu_list.append(temp)

    # 所有菜单
    menu_list = list(models.Menu.objects.values('id','caption', 'parent_id'))

    # 把菜单写到session中
    request.session[settings.SESSION_PERMISSION_URL_KEY] = permission_url_list

    request.session[settings.SESSION_PERMISSION_MENU_URL_KEY] = {
        settings.PERMISSION_MENU_KEY: permission_menu_list,
        settings.ALL_MENU_KEY: menu_list
    }
