from django.db import models
from neomodel import   StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo, BooleanProperty



# Create your models here.

class User(StructuredNode):
    u_id = UniqueIdProperty()
    name = StringProperty(index=True)
    age = IntegerProperty(index=True, default=0)
    email = StringProperty(unique_index=True, default=0)
    password = StringProperty(index=True, default=0)