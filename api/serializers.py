from rest_framework import serializers

from blog.models import Article, Comment


class ArticleCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'text')


class CommentCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('article', 'text')

    def create(self, validated_data):
        comment = super().create(validated_data)
        comment.parent_path = '/'

        return comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

