from django.urls import path

from api import views


urlpatterns = [
    path('v1/articles/', views.create_article),
    path('v1/articles/<int:pk>/comments', views.get_article_comments_or_add_new),
    path('v1/comments/<int:pk>/replies', views.get_comment_replies_or_add_new),
]

