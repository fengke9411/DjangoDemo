from django.contrib import admin
from TestModel.models import Test, Article, Category,User,Avatar,Project,WorkExperience,Skill


# Register your models here.

class CategoryStyle(admin.ModelAdmin):
    list_display=('id','name')

class UserStyle(admin.ModelAdmin):
    list_display=('id','username','password','nickname','loginAddress','integral','birthday','mobile','email')



admin.site.register([Test, Article,Avatar,Project,WorkExperience,Skill])
admin.site.register(Category, CategoryStyle)
admin.site.register(User, UserStyle)


