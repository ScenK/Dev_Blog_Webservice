# -*- coding: utf-8 -*-
import json
from operator import attrgetter

from webservice.base import APIHandler
from webservice.tasks.email_tasks import send_email_task
from config import SETTINGS
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
        diaries = Diary.objects.order_by('-publish_time')[(int(page_num) - 1)*10
                                                          :int(page_num) * 10]
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

        category_json = json.loads(category.to_json())

        diaries = []

        for c in category_json['diaries']:
            diary = Diary.objects(pk=c['$oid']).first()

            diaries.append(json.loads(diary.to_json()))

        category_json['diaries'] = diaries

        d = category_json

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


class CommentAddHandler(APIHandler):
    """ Comment Add AJAX Post Action.

    designed for ajax post and send reply email for admin

    Args:
        username: guest_name
        did: diary ObjectedId
        email: guest_email
        content: comment content

    Return:
        email_status: success
    """
    def get(self, *args):
        did = self.get_argument('did')
        name = self.get_argument('username')
        email = self.get_argument('email')
        content = self.get_argument('comment')


        diary = Diary.objects(pk=did)
        diary_title = diary[0].title

        commentEm = CommentEm(
                    author = name,
                    content = content,
                    email = email
                )
        diary.update_one(push__comments=commentEm)

        comment = Comment(content=content)
        comment.diary = diary[0]
        comment.email = email
        comment.author = name
        comment.save(validate=False)

        try:
            send_email_task(SETTINGS['EMAIL'],
                            SETTINGS['MAIN_TITLE'] + u'收到了新的评论, 请查收',
                            content, did, name, diary_title)

            response = json.dumps({'success': 'true'})
            self.finish(response)
        except Exception as e:
            return str(e)

