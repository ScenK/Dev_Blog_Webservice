# from ws.handlers import *
#
# urls = [
#     (r'/v2/diary/list/([0-9]+)', DiaryListHandler),
#     (r'/v2/diary/detail/([0-9a-zA-Z]+)', DiaryDetailHandler),
#
#     (r'/v2/category/list', CategoryListHandler),
#     (r'/v2/category/detail/([0-9a-zA-Z]+)', CategoryDetailHandler),
#
#     (r'/v2/tag/list', TaglListlHandler),
#     (r'/v2/tag/detail/([0-9a-zA-Z_%^\s]+)', TagDetailHandler),
#
#     (r'/v2/gallery/list', GalleryListHandler),
#     (r'/v2/gallery/detail/([0-9a-zA-Z]+)', GalleryDetailHandler),
#
#     (r'/v2/user/profile', UserProfileHandler),
#
#     (r'/v2/comment/add', CommentAddHandler),
# ]
from .handlers.diary import DiaryListHandler

urls = [
    (r'/v2/diary/list/([0-9]+)', DiaryListHandler),
]
