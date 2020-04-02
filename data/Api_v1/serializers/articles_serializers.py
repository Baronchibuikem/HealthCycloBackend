from rest_framework import serializers
from data.models import Articles


class ArticlesSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(
        source='category.name',
        read_only=True
    )
    class Meta:
        model = Articles
        fields = ("category","category_name", "title", "content", "access", "images", "file", "date_created")
