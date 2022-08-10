"""app_demo models."""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from image_optimizer.fields import OptimizedImageField


class Post(models.Model):
    """
    Post model.

    This model represents a Blog Post with a few fields including a `photo`
    field which is an OptimizedImageField instance without any optional
    argument. This means that out Post photo would keep source image original
    size.
    """

    title = models.CharField(
        max_length=100
    )
    photo =  models.ImageField("Photo", upload_to="media")
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Collaborator(models.Model):
    """
    Collaborator model.

    This model represents a Blog Collaborator(a.k.a. Writter) with a few
    fields including a `profile_image` field which is an OptimizedImageField
    instance with `optimized_image_output_size` and
    `optimized_image_resize_method` arguments set.

    This means that our Collaborator profile_image would be a resized
    version of the source image, meant to keep a given screen resolution,
    in this case (400, 300) pixels.
    """

    name = models.CharField(
        max_length=100
    )
    profile_image = models.ImageField("Profile Image", upload_to="media")
    # profile_image = OptimizedImageField(
    #     upload_to='uploads/collaborators/%Y/%m/%d',
    #     optimized_image_output_size=(400, 300),
    #     optimized_image_resize_method='cover'  # 'thumbnail' or 'cover'
    # )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
