import base64, boto3, uuid
from django.conf import settings
from django.core.files.base import ContentFile


def upload_image_to_s3(picture_base_64: str, product_id: int, folder: str = "products") -> str:
    if "," in picture_base_64:
        picture_base_64 = picture_base_64.split(",")[1]

    decoded_file = base64.b64decode(picture_base_64)
    file_ext = "png"
    s3_filename = f"{folder}/product_{product_id}_{uuid.uuid4()}.{file_ext}"

    s3 = boto3.client(
        "s3",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME,
    )

    s3.upload_fileobj(
        Fileobj=ContentFile(decoded_file),
        Bucket=settings.AWS_STORAGE_BUCKET_NAME,
        Key=s3_filename,
        ExtraArgs={"ContentType": "image/png"},
    )

    return f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{s3_filename}"
