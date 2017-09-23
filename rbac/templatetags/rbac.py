#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Sam"
# Date: 2017/9/22

import re
import os
from django.template import Library
from django.conf import settings
from django.utils.safestring import mark_safe

register = Library()

def process_menu_data(request):
    '''
    生成菜单相关数据
    :param request: 
    :return: 
    '''

    menu_permission_list = request.session.get(settings.SESSION_PERMISSION_MENU_URL_KEY)
    menu_list = menu_permission_list[settings.ALL_MENU_KEY]
    permission_list = menu_permission_list[settings.PERMISSION_MENU_KEY]

    all_menu_dict = {}

    # 循环全部的菜单，给每个字典加上三组键值对
    for item in menu_list:
        item['children'] = []  # 用来保存子菜单
        item['status'] = False  # status用来标识是否需要在菜单上显示
        item['open'] = False  # open 用来标识是否为默认展开
        all_menu_dict[item['id']] = item

    # 循环用户的权限列表，匹配用户当前访问的url
    for per in permission_list:
        per['status'] = True
        pattern = settings.URL_REGEX.format(per['url'])
        if re.match(pattern, request.path_info):  # 如果匹配成功，改为展开状态
            per['open'] = True
        else:
            per['open'] = False

        all_menu_dict[per['menu_id']]['children'].append(per)  # 把权限添加到对应的菜单中

        # 把所有父级的显示标识改为True
        pid = per['menu_id']
        while pid:
            all_menu_dict[pid]['status'] = True
            pid = all_menu_dict[pid]['parent_id']

        # 如果权限的为默认展开状态，那么把所有的父级标签的默认展开也设为True
        if per['open']:
            ppid = per['menu_id']
            while ppid:
                all_menu_dict[ppid]['open'] = True
                ppid = all_menu_dict[ppid]['parent_id']

    result = []  # 最终的结果列表

    # 循环所有的菜单的字典，筛选出根菜单，并把子菜单添加到对应的父级菜单中
    for k, v in all_menu_dict.items():
        if not v.get('parent_id'):
            result.append(v)
        else:
            parent_id = v['parent_id']
            all_menu_dict[parent_id]['children'].append(v)

    return result


def process_menu_html(menu_list):
    '''
    生成菜单的html
    :param menu_list: 
    :return: 
    '''
    # 菜单样式
    tpl1 = """
                <div class='rbac-menu-item'>
                    <div class='rbac-menu-header'>{0}</div>
                    <div class='rbac-menu-body {2}'>{1}</div>
                </div>
            """
    # 权限样式
    tpl2 = """
                <a href='{0}' class='{1}'>{2}</a>
            """

    html = ""

    for item in menu_list:
        if not item['status']:
            continue
        if item.get('url'): # 如果有url，就表示是权限，
            html += tpl2.format(item['url'], 'rbac-active' if item['open'] else '',item['title'])
        else:
            # 菜单
            html += tpl1.format(item['caption'],process_menu_html(item['children']),'' if item['open'] else 'rbac-hide')

    return html


@register.simple_tag
def rbac_menus(request):
    # 数据库取到菜单相关数据
    result = process_menu_data(request)
    # 生成HTML
    html = process_menu_html(result)

    return mark_safe(html)

@register.simple_tag
def rbac_css():
    file_path = os.path.join('rbac','theme','rbac.css')
    if os.path.exists(file_path):
        return mark_safe(open(file_path,'r',encoding='utf-8').read())
    else:
        raise Exception('rbac主题CSS文件不存在')


@register.simple_tag
def rbac_js():
    file_path = os.path.join('rbac', 'theme', 'rbac.js')
    if os.path.exists(file_path):
        return mark_safe(open(file_path, 'r', encoding='utf-8').read())
    else:
        raise Exception('rbac主题JavaScript文件不存在')