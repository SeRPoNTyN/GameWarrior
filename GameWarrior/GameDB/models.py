from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    slug = models.SlugField(max_length=300, unique=True, verbose_name="Url")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse("categories", kwargs={"slug": self.slug})


class Tags(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    slug = models.SlugField(max_length=300, unique=True, verbose_name="Url")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['title']

    def get_absolute_url(self):
        return reverse("tags", kwargs={"slug": self.slug})


class Game(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    slug = models.SlugField(max_length=300, unique=True, verbose_name='Url')
    description = models.TextField(verbose_name='Description')
    developer = models.CharField(max_length=150, verbose_name='Developer')
    image = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Image')
    created_at = models.DateField(verbose_name='Publication Date')
    rating = models.FloatField(default=0, verbose_name='Rating')
    views = models.IntegerField(default=0, verbose_name='Rating')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='Games')
    tag = models.ManyToManyField(Tags, related_name='Games')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated Date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
        ordering = ['rating', 'title']

    def get_absolute_url(self):
        return reverse("single", kwargs={"slug": self.slug})
