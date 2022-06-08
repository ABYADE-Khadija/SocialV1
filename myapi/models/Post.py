from django.db import models
from neomodel import   StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo, BooleanProperty, ArrayProperty, DateTimeProperty



# Create your models here.

class Post(StructuredNode):
    Post_id = UniqueIdProperty()
    caption = StringProperty(index=True)
    is_hidden = BooleanProperty(index=True)
    #likes = ArrayProperty(index=True)
    date = DateTimeProperty(index=True)

