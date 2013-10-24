# -*- coding: utf-8 -*-
from webservice.handlers import *

urls = [
    (r'/v1/diary/list/([0-9]+)', DiaryListHandler),
    (r'/v1/diary/detail/([0-9a-zA-Z]+)', DiaryDetailHandler),

    (r'/v1/category/list', CategoryListHandler),
    (r'/v1/category/detail/([0-9a-zA-Z]+)', CategoryDetailHandler),

    (r'/v1/tag/list', TaglListlHandler),
    (r'/v1/tag/detail/([0-9a-zA-Z_%^\s]+)', TagDetailHandler),

    (r'/v1/gallery/list', GalleryListHandler),
    (r'/v1/gallery/detail/([0-9a-zA-Z]+)', GalleryDetailHandler),

    (r'/v1/user/profile', UserProfileHandler),
]
