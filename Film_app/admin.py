from django.contrib import admin
from .models import Dawrat ,Comments,PostMainHome,Offre,Command

# Register your models here.


class AdminOffre(admin.ModelAdmin):

    list_display = ('status','price')




class AdminDawrat(admin.ModelAdmin):

    list_display = ('title','price','date')




class Admincomment(admin.ModelAdmin):

    list_display = ('name','email','date')




class Admincommand(admin.ModelAdmin):

    list_display = ('prenom','name','num','email','date')



admin.site.register(Comments,Admincomment)
admin.site.register(Dawrat,AdminDawrat)
admin.site.register(Offre,AdminOffre)
admin.site.register(Command,Admincommand)
admin.site.register(PostMainHome)