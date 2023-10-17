from django.urls import path
from . import views
# from django import views
urlpatterns = [
    path("",views.base,name="base"),
    path('login_user',views.login_user,name="login_user"),
    path("upload_data",views.upload_data,name="upload_data"),
    path("query_builder",views.query_builder,name="query_builder"),
    path("users",views.users,name="users"),
    path("add_user",views.add_user,name="add_user"),
    path('upload',views.upload,name="upload")

]
