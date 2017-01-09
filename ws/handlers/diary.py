from ws.base import APIHandler
from ws.models import *


class DiaryListHandler(APIHandler):
    def get(self, page_num):
        """Diary List handler.
        Also support paging.

        Args:
            page_num: int

        Return:
            diaries: json
        """
        diaries = Diary.objects.order_by('-publish_time')[
                  (int(page_num) - 1) * 10:int(page_num) * 10]
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
