from django.shortcuts import render
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from api import serializers
from blog.models import Comment


@api_view(http_method_names=['POST'])
def create_article(request):
    data = JSONParser().parse(request)
    serializer = serializers.ArticleCreationSerializer(data=data)
    if serializer.is_valid():
        article = serializer.save()
        article_response = serializer.data
        article_response['id'] = article.pk
        return Response(article_response)

    return Response({'message': 'article data is not valid'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['POST'])
def add_comment_to_article(request, pk):
    data = JSONParser().parse(request)
    data['article'] = pk
    serializer = serializers.CommentCreationSerializer(data=data)
    if serializer.is_valid():
       comment_reponse = serializers.CommentSerializer(serializer.save())
       return Response(comment_reponse.data)

    return Response({'message': 'comment data is invalid'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['POST'])
def add_comment_reply(request, pk):
    parent_comment = Comment.objects.get(pk=pk)

    data = JSONParser().parse(request)
    data['article'] = parent_comment.article.pk
    data['parent_path'] = f'{parent_comment.parent_path}{parent_comment.pk}/'
    data['level'] = parent_comment.level + 1
    
    serializer = serializers.CommentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response({'message': 'reply data is invalid'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['GET'])
def get_article_comments(request, pk):
    comments = Comment.objects.filter(article__pk=pk).filter(level__lte=3).order_by('parent_path', 'time_posted')
    serializer = serializers.CommentSerializer(comments, many=True)

    return Response(serializer.data)

