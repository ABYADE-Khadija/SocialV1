from django.http import JsonResponse, HttpResponse
from django.template import RequestContext

from django.views.decorators.csrf import csrf_exempt
import json

from neomodel import DateTimeProperty, ArrayProperty

from user import models
from user.models import User
from myapi.models import Post
from datetime import datetime

@csrf_exempt
def addPost(request):
    if request.method == 'POST':
        # create a post
        json_data = json.loads(request.body)
        caption = json_data['caption']
        is_hidden = bool(json_data['is_hidden'])
        date = datetime.now()
        u_id = json_data['u_id']
        try:
            user = User.nodes.get(u_id=u_id)
            likes = []
            post = Post(caption=caption, is_hidden=is_hidden, date=date, likes= likes)
            post.save()
            res = user.posts.connect(post)
            response = {
                "post_id": post.id,
                "caption": post.caption,
                "is_hidden": post.is_hidden,
                "date": post.date,
            }
            return JsonResponse(response)
        except Exception as e:
            print(e)
            response = {"error":"error occured while creating post"}
            return JsonResponse(response, safe=False)

@csrf_exempt
def likePost(request):
    if request.method == 'POST':
        # like a post
        json_data = json.loads(request.body)
        post_id = json_data['post_id']
        date = datetime.now()
        u_id = json_data['u_id']
        try:
            user = User.nodes.get(u_id=u_id)
            post = Post.nodes.get(Post_id=post_id)
            #cd = CurrentDate()
            res = user.likes.connect(post)
            response = {
                "u_id": user.u_id,
                "post_id": post.Post_id,
                "u_name": user.name,
                "post_caption": post.caption,
                "relation_date": res.liking_date
            }
            return JsonResponse(response)
        except Exception as e:
            print(e)
            response = {"error":"error occured while liking post"}
            return JsonResponse(response, safe=False)

@csrf_exempt
def unlikePost(request):
    if request.method == 'POST':
        # like a post
        json_data = json.loads(request.body)
        post_id = json_data['post_id']
        date = datetime.now()
        u_id = json_data['u_id']
        try:
            user = User.nodes.get(u_id=u_id)
            post = Post.nodes.get(Post_id=post_id)
            #cd = CurrentDate()
            res = user.likes.disconnect(post)
            response = {
                "u_id": user.u_id,
                "post_id": post.Post_id,
                "u_name": user.name,
                "post_caption": post.caption,
                "creation_date": res
            }
            return JsonResponse(response)
        except Exception as e:
            print(e)
            response = {"error":"error occured while unliking post"}
            return JsonResponse(response, safe=False)


@csrf_exempt
def updatePost(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            caption = json_data['caption']
            is_hidden = bool(json_data['is_hidden'])
            Post_id = json_data['Post_id']
            date = datetime.now()
            #get Post
            post = Post.nodes.get(Post_id=Post_id)
            #update Post
            post.caption = caption
            post.is_hidden = is_hidden
            post.date = date
            post.save()
            response = {
                "Post_id": post.Post_id,
                "caption": post.caption,
                "is_hidden": post.is_hidden,
                "updating_date" : post.date
            }
            return JsonResponse(response)
        except Exception as e:
            print(e)
            response = {"error": "error occured while updating post"}
            return JsonResponse(response, safe=False)

@csrf_exempt
def removePost(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            Post_id = json_data['Post_id']
            post = Post.nodes.get(Post_id=Post_id)
            post.delete()
            response = {"resullt": "Post deleted succefully"}
            return JsonResponse(response)
        except Exception as e:
            print(e)
            response = {"error": "error occured while deleting post"}
            return JsonResponse(response, safe=False)
