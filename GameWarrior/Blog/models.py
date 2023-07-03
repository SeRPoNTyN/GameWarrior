from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.db.models import F
from GameDB.models import *
# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    game = models.ManyToManyField(Game, blank=True, verbose_name="Game")
    views = models.IntegerField(default=0, verbose_name="Views")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Publication Date")
    slug = models.SlugField(max_length=300, unique=True, verbose_name="Url")
    content = models.TextField(verbose_name="Content")
    image = models.ImageField(verbose_name="Image", upload_to="photos/%Y/%m/%d", blank=True)
    tag = models.ManyToManyField(Tags, blank=True, related_name="News_Tag")
    author = models.CharField(max_length=150, verbose_name="Author")
    likes = models.IntegerField(default=0, verbose_name="Likes")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="News_Category")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at", "title"]
        verbose_name = "News"
        verbose_name_plural = "News"

    def get_absolute_url(self):
        return reverse("news", kwargs={"slug": self.slug})


class Review(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    game = models.ForeignKey(Game, on_delete=models.PROTECT, verbose_name="Review_Game", db_index=False)
    views = models.IntegerField(default=0, verbose_name="Views")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Publication Date")
    slug = models.SlugField(max_length=300, unique=True, verbose_name="Url")
    content = models.TextField(verbose_name="Content")
    tag = models.ManyToManyField(Tags, blank=True, related_name="Review_Tag")
    author = models.CharField(max_length=150, verbose_name="Author")
    likes = models.IntegerField(default=0, verbose_name="Likes")
    score = models.FloatField(default=0, verbose_name="Score")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at", "title"]
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def get_absolute_url(self):
        return reverse("review", kwargs={"slug": self.slug, "game_slug": self.game.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

