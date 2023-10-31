from django.urls import path , include
from blog import views
urlpatterns = [
    path('postComment/',views.postComment,name="postcomment"),
    path('', views.blogHome, name='blogHome'),
    path('<str:slug>', views.blogpost, name='blogpost'),
    # API to post a comment
]
