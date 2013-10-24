# -*- coding: utf-8 -*-
import json
from operator import attrgetter

from webservice.base import APIHandler
from models import *

class DiaryListHandler(APIHandler):
    def get(self, page_num):
        """Diary List handler.
        Also support paging.

        Args:
            page_num: int

        Return:
            diaries: json
        """
        diaries = Diary.objects.order_by('-publish_time')[(int(page_num) - 1)*5
                                                          :int(page_num) * 5]
        d = diaries.to_json()
        self.finish(d)


class DiaryDetailHandler(APIHandler):
    def get(self, diary_id):
        """Diary Detail handler.

        Args:
            diary_id: ObjectID

        Return:
            diary: json
        """
        diary = Diary.objects(pk=diary_id).first()

        d = diary.to_json()
        self.finish(d)


class CategoryListHandler(APIHandler):
    def get(self):
        """Category List handler.

        Args:
            none

        Return:
            categories: json
        """
        categories = Category.objects.order_by('-publish_time')

        d = categories.to_json()
        self.finish(d)


class CategoryDetailHandler(APIHandler):
    def get(self, category_id):
        """Category Detail handler.

        Args:
            category_id: ObjectID

        Return:
            category: json
        """
        category = Category.objects(pk=category_id).first()

        d = category.to_json()
        self.finish(d)


class TaglListlHandler(APIHandler):
    def get(self):
        """Tag List handler.

        Args:
            none

        Return:
            tags: json
        """
        tags = Tag.objects.order_by('-publish_time')

        d = tags.to_json()
        self.finish(d)


class TagDetailHandler(APIHandler):
    def get(self, tag_name):
        """Tag Detail handler.

        Args:
            tag_name: String

        Return:
            tag: json
        """
        tag = Tag.objects(name=tag_name).first()

        d = tag.to_json()
        self.finish(d)


class GalleryListHandler(APIHandler):
    def get(self):
        """Gallery List handler.

        Args:
            none

        Return:
            gallery: json
        """
        albums = Gallery.objects.order_by('-publish_time')

        d = albums.to_json()
        self.finish(d)


class GalleryDetailHandler(APIHandler):
    def get(self, gallery_id):
        """Gallery Detail handler.

        Args:
            gallery_id: ObjectID

        Return:
            gallery: json
        """
        gallery = Gallery.objects(pk=gallery_id).first()

        d = gallery.to_json()
        self.finish(d)


class UserProfileHandler(APIHandler):
    def get(self):
        """User handler.
        Get all user profile except hashed password.

        Args:
            none

        Return:
            profile: json
        """
        user = User.objects().first()

        d = json.loads(user.to_json())
        del d['password']

        self.finish(d)
