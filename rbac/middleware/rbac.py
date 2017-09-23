#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Sam"
# Date: 2017/9/21
from django.shortcuts import render,HttpResponse,redirect
from django.conf import settings
import re

class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response

class Rbacmiddleware(MiddlewareMixin):
    '''
    用户权限验证中间件
    '''

    def process_request(self,request):
        print(request.path_info)
        # 看用户请求的路径是不是在白名单里
        for url in settings.PASS_URL_LIST:
            if re.match(url,request.path_info):
                return None

        permission_url_list = request.session.get(settings.SESSION_PERMISSION_URL_KEY)

        # 如果没有权限，跳到登录页面
        if not permission_url_list:
            return redirect(settings.LOGIN_URL)

        # 标志位来判断是否有权访问路径
        flag = False

        for db_url in permission_url_list:
            pattern = settings.URL_REGEX.format(db_url)
            if re.match(pattern,request.path_info):
                flag = True
                break

        if not flag:

            if settings.DEBUG:
                url_html = "<br>".join(permission_url_list)
                return HttpResponse("无权访问当前页面,但你可以访问%s" %url_html)

            else:
                return HttpResponse('无权访问')

