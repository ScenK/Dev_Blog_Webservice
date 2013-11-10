:Info: The dev_blog web-service, powered by Tornado and Mongoengine.
:Repository: https://github.com/ScenK/dev_blog_webservice
:Author: Scen.K (http://tuzii.me).
:License: MIT License.


文件目录结构:
---------
::

    Dev_blog_Webseivece/
        .
        ├── config.py.sample
        ├── __init__.py
        ├── LICENSE
        ├── models.py
        ├── README.md
        ├── runserver.py
        ├── urls.py
        └── webservice
            ├── base.py
            ├── exceptions.py
            ├── handlers.py
            ├── __init__.py
            ├── mail.py
            ├── static
            │   └── robots.txt
            └── tasks
                ├── email_tasks.py
                └── __init__.py

+ Api文档(V1):

================================== ========= ================================= ======== ====
参数                               意义      地址                              返回类型 备注
page_num                           日志列表  /v1/diary/list/<page_mun>         Array    JSONP-Callback
diary_id                           日志详情  /v1/diary/detail/<diary_id>       Object   JSONP-Callback
diary_id, username, email, content 文章评论  /v1/comment/add                   Object   JSONP-Callback
None                               分类列表  /v1/category/list                 Object   JSONP-Callback
category_id                        分类详情  /v1/category/detail/<category_id> Object   JSONP-Callback
None                               标签列表  /v1/tag/list                      Object   JSONP-Callback
tag_id                             标签详情  /v1/tag/detail/<tag_id>           Object   JSONP-Callback
None                               影集列表  /v1/gallery/list                  Object   JSONP-Callback
album_id                           影集详情  /v1/gallery/detail/<album_id>     Object   JSONP-Callback
None                               博主信息  /v1/user/profile                  Object   JSONP-Callback
================================== ========= ================================= ======== ====

*Do it yourself and make joy :)



