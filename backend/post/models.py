from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.utils.text import slugify
import string
from django.utils.crypto import get_random_string
from django.core.validators import MinValueValidator

def unique_slugify(instance, slug):         #tworzenie unikalnego slugu opartego na nazwie
    model = instance.__class__
    unique_slug = slug
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = slug + get_random_string(length=3)
    return unique_slug


class Post(models.Model):
    deleted = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True) #dodawanie zdjęć do folderu uploads
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True) #miniaturka zdjęcia

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('-date_added',) #odwrócenie segregacji po dacie dodania

    def get_absolute_url(self):                 #url dla postu z nazwą
        return f'/{self.slug}/'


    def save(self, *args, **kwargs):            #przy zapisie tworzy slug z nazwy (jeśli występował wykorzystuje metode unique_slugify)
        if not self.slug:
            slug = slugify(self.name)
            self.slug = unique_slugify(self, slug)
        super(Post, self).save(*args, **kwargs)

    def get_image(self):                        #zwraca zdjęcie główne w lepszej jakości
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    def make_thumbnail(self, image, size=(300,200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail

    

