from django.urls import path

from api import views


urlpatterns = [
    path('v1/articles/', views.create_article),
    path('v1/articles/<int:pk>/add_comment', views.add_comment_to_article), # TODO move article id to path
]

