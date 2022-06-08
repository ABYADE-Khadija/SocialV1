from datetime import datetime

from django.db import models
from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo, BooleanProperty, \
    StructuredRel, DateTimeProperty

# Create your models here.
from myapi.models import Post

class LikingDate(StructuredRel):
   liking_date = DateTimeProperty(datetime.now())

class CreationDate(StructuredRel):
   creationDate = DateTimeProperty(datetime.now())

class User(StructuredNode):
    u_id = UniqueIdProperty()
    name = StringProperty(index=True)
    age = IntegerProperty(index=True, default=0)
    email = StringProperty(unique_index=True, default=0)
    password = StringProperty(index=True, default=0)

    posts = RelationshipTo(Post, 'posts',model=CreationDate)
    likes = RelationshipTo(Post, 'likes', model=LikingDate)

