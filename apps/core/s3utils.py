"""
We need this module when storing files in S3 as the S3BotoStorage backend
always uses the bucket name as the root by default, but we don't want to create
two separate buckets for static and media files.

We basically want:
    /bucket-name/media/ for media files
    /bucket-name/static/ for static files

Source: http://stackoverflow.com/questions/10390244/how-to-set-up-a-django-\
        project-with-django-storages-and-amazon-s3-but-with-diff
"""

from django.conf import settings

from storages.backends.s3boto import S3BotoStorage


MediaRootS3BotoStorage = lambda: S3BotoStorage(
    location=settings.MEDIA_ROOT,
    file_overwrite=False
)

StaticRootS3BotoStorage = lambda: S3BotoStorage(
    location=settings.STATIC_ROOT
)