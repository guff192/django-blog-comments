from django.shortcuts import render
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from api import serializers


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
    data["article"] = pk
    serializer = serializers.CommentCreationSerializer(data=data)
    if serializer.is_valid():
       comment_reponse = serializers.CommentSerializer(serializer.save())

       return Response(comment_reponse.data)

    return Response({'message': 'comment data is invalid'}, status=status.HTTP_400_BAD_REQUEST)

