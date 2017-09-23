from django.db import models

class Menu(models.Model):
    '''
    菜单表
    '''

    caption = models.CharField(max_length=32)
    parent = models.ForeignKey('self',null=True,blank=True)

    def __str__(self):
        caption_list = [self.caption,]
        p = self.parent
        while p:
            caption_list.insert(0,p.caption)
            p = p.parent

        return '-'.join(caption_list)

class UserInfo(models.Model):
    '''
    用户信息表
    '''

    nickname = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.EmailField()

    roles = models.ManyToManyField('Role')

    def __str__(self):

        return  self.nickname



class Role(models.Model):
    '''
    角色表
    '''

    name = models.CharField(max_length=32)
    permissions = models.ManyToManyField('Permission')

    def __str__(self):

        return self.name


class Permission(models.Model):
    '''
    权限表
    '''

    title = models.CharField(max_length=32)
    url = models.CharField(max_length=255)
    menu = models.ForeignKey("Menu",null=True,blank=True)

    def __str__(self):

        return  "%s--%s" %(self.title,self.menu)