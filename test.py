#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Sam"
# Date: 2017/9/22


all_menu_dict = {
    1:{'id': 1, 'caption': '用户管理', 'parent_id': None, 'children': [], 'status': False, 'open': False},
    2:{'id': 2, 'caption': '订单管理', 'parent_id': None, 'children': [], 'status': False, 'open': False},
    3:{'id': 3, 'caption': '其他', 'parent_id': None, 'children': [], 'status': False, 'open': False},
    4:{'id': 4, 'caption': '退货', 'parent_id': 2, 'children': [], 'status': False, 'open': False},
    5:{'id': 5, 'caption': '换货', 'parent_id': 2, 'children': [], 'status': False, 'open': False}
}


permission_list = [
    {'title': '权限1', 'url': '/test/', 'menu_id': 1},
    {'title': '权限2', 'url': '/test/', 'menu_id': 1},
    {'title': '权限3', 'url': '/test/', 'menu_id': 4},
    {'title': '权限4', 'url': '/test/', 'menu_id': 5}
]



for per in permission_list:
    temp = []
    all_menu_dict[per['menu_id']]['status'] = True
    if all_menu_dict[per['menu_id']].get('parent_id', 0):
        parent_id = all_menu_dict[per['menu_id']].get('parent_id')
        all_menu_dict[parent_id]['status'] = True

print(all_menu_dict)