# ============================================================================================================ #
#   kkk      kkk      ooooo       dddddddd         eeeeeeeeee   kkk      kkk      ooooo            ooooo       #
#   kkk     kkk     ooooooooo     ddddddddddd      eeeeeeeeee   kkk     kkk     ooooooooo        ooooooooo     # 
#   kkk    kkk     ooo     ooo    ddd      ddd     eee          kkk    kkk     ooo     ooo      ooo     ooo    #
#   kkk   kkk     oooo     oooo   ddd       ddd    eee          kkk   kkk     oooo     oooo    oooo     oooo   #
#   kkk  kkk      oooo     oooo   ddd        ddd   eee          kkk  kkk      oooo     oooo    oooo     oooo   #
#   kkkkkkkk      oooo     oooo   ddd        ddd   eeeeeeeeee   kkkkkkkk      oooo     oooo    oooo     oooo   #
#   kkk  kkk      oooo     oooo   ddd        ddd   eee          kkk  kkk      oooo     oooo    oooo     oooo   #
#   kkk   kkk     oooo     oooo   ddd       ddd    eee          kkk   kkk     oooo     oooo    oooo     oooo   #
#   kkk    kkk     ooo     ooo    ddd      ddd     eee          kkk    kkk     ooo     ooo      ooo     ooo    #
#   kkk     kkk     ooooooooo     dddddddddd       eeeeeeeeee   kkk     kkk     ooooooooo        ooooooooo     #
#   kkk      kkk      ooooo       ddddddd          eeeeeeeeee   kkk      kkk      ooooo            ooooo       #
# ============================================================================================================ #


from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User

from django.core.urlresolvers import reverse

from ckeditor_uploader.fields import RichTextUploadingField

from ckeditor.fields import RichTextField

from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_post')
    # body = models.TextField() -> Change to CKEditor Text Field !
    body = RichTextField(config_name='kdk_ckeditor')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'), self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)