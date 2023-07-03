from django.db import models
from django.contrib.auth.models import *
from django.urls import reverse


# Create your models here.


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Автор комментария")
    content = models.TextField(verbose_name="Содержимое комментария")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания комментария")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def delete_comment(self):
        return reverse("del_comment", kwargs={"pk": self.pk})

