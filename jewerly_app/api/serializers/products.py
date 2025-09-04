from rest_framework import serializers
from jewerly_app.models import *
from jewerly_app.services.upload_image import s3_service


class ProductReadSerializer(serializers.ModelSerializer):
    article = serializers.CharField(source='article_code', read_only=True)
    picture_url = serializers.URLField(source='photo_url', read_only=True, required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'article', 'picture_url', 'is_archived']


class ProductUpdateSerializer(serializers.ModelSerializer):
    article = serializers.CharField(source='article_code')
    picture_url = serializers.URLField(source='photo_url', required=False, allow_null=True)
    picture_base_64 = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Product
        fields = ['name', 'article', 'picture_url', 'picture_base_64', 'is_archived']

    def create(self, validated_data):
        picture_base_64 = validated_data.pop("picture_base_64", None)
        product = super().create(validated_data)

        if picture_base_64:
            product.photo_url = s3_service.upload_image_to_s3(picture_base_64, product.id)
            product.save(update_fields=["photo_url"])

        return product

    def update(self, instance, validated_data):
        picture_base_64 = validated_data.pop("picture_base_64", None)
        product = super().update(instance, validated_data)

        if picture_base_64:
            product.photo_url = s3_service.upload_image_to_s3(picture_base_64, product.id)
            product.save(update_fields=["photo_url"])

        return product
