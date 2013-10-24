# -*- coding: utf-8 -*-
import datetime
from mongoengine import *

connect('dev_blog2')

class User(Document):
    name         = StringField(max_length=50, required=True)
    password     = StringField()
    email        = StringField()
    avatar       = StringField()
    signature    = StringField()
    created_at   = DateTimeField(default=datetime.datetime.now, required=True)

class Diary(Document):
    title        = StringField(required=True)
    old_id       = IntField()
    content      = StringField()
    summary      = StringField()
    html         = StringField()
    category     = StringField(default=u'未分类')
    author       = ReferenceField(User)
    tags         = SortedListField(StringField())
    comments     = SortedListField(EmbeddedDocumentField('CommentEm'))
    publish_time = DateTimeField(default=datetime.datetime.now, required=True)
    update_time  = DateTimeField(default=datetime.datetime.now, required=True)

    meta = {'allow_inheritance': True}

class Gallery(Document):
    title        = StringField(required=True)
    index        = StringField()
    description  = StringField()
    content      = SortedListField(EmbeddedDocumentField('PhotoEm'))
    publish_time = DateTimeField(default=datetime.datetime.now, required=True)

class Tag(Document):
    name         = StringField(max_length=120, required=True)
    diaries      = SortedListField(ReferenceField(Diary))
    publish_time = DateTimeField(default=datetime.datetime.now, required=True)

    meta = {
        'indexes': ['name']
    }

class Category(Document):
    name         = StringField(max_length=120, required=True)
    diaries      = SortedListField(ReferenceField(Diary))
    publish_time = DateTimeField(default=datetime.datetime.now, required=True)

class Comment(Document):
    content      = StringField(required=True)
    author       = StringField(max_length=120, required=True)
    email        = EmailField()
    diary        = ReferenceField(Diary)
    publish_time = DateTimeField(default=datetime.datetime.now, required=True)

class Page(Document):
    url          = StringField(required=True, unique=True)
    title        = StringField(required=True)
    content      = StringField()
    summary      = StringField()
    html         = StringField()
    author       = ReferenceField(User)
    comments     = SortedListField(EmbeddedDocumentField('CommentEm'))
    publish_time = DateTimeField(default=datetime.datetime.now, required=True)
    update_time  = DateTimeField(default=datetime.datetime.now, required=True)

    meta = {'allow_inheritance': True}

class StaticPage(Page):
    pass

class CommentEm(EmbeddedDocument):
    content      = StringField(required=True)
    author       = StringField(max_length=120, required=True)
    email        = EmailField()
    publish_time = DateTimeField(default=datetime.datetime.now, required=True)

class PhotoEm(EmbeddedDocument):
    path         = StringField(required=True)
    title        = StringField()
    description  = StringField()
    publish_time = DateTimeField(default=datetime.datetime.now, required=True)
