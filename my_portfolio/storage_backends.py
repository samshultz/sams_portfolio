from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False


class StaticS3Storage(S3Boto3Storage):
   location = settings.AWS_LOCATION
   default_acl = 'public-read'