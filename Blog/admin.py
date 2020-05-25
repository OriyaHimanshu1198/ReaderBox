# Register your models here.
from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group


admin.site.unregister(Group)

admin.site.site_header = "ReaderBox Admin"
admin.site.site_title = "ReaderBox Admin Portal"
admin.site.index_title = "Welcome to  Admin Portal"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/tinyInject.js',)
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','subject')
      
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):    
    list_display = ('content', 'email','name')



