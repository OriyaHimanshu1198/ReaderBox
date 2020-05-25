from django.urls import path 
from . import views


urlpatterns = [
    path('',views.index, name='home'),
    path('Blog/',views.blogView, name='Blog'),
    path('<slug:slug>/',views.blog_Single, name='blog-single'),
    path('ContactUs',views.contect, name='contact'),
    
    #path('dash',views.dashboard, name='dash'),
    #path('createPost',views.createPost, name='postCreate'),
    #path('updatePost/<slug:slug>/',views.updatePost, name='updatePost'),
    #path('deletePost/<slug:slug>/',views.deletePost, name='deletePost'),
    #path('<slug:slug>/',views.blog_Single.as_view(), name='blog-single'),
    #path('',views.AdminView, name= 'dashboard'),
    #path('main',views.main.as_view(), name= 'dashboard'),
    #path('Blog/',views.blogView.as_view(), name='Blog'),
    
]