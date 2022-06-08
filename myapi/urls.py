from django.conf.urls import url
from myapi.views import *
from django.urls import path
urlpatterns = [
    path('',inscription),
    path('login',login),
    path('updateUser',updateUser),
    path("removeUser",removeUser),
    path("addPost",addPost),
    path("likePost",likePost),
    path("unlikePost",unlikePost),
    path("updatePost",updatePost),
    path("removePost",removePost),

]
