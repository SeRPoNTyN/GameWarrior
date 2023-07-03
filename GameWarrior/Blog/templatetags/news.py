from django import template
from Blog.models import *

register = template.Library()


@register.inclusion_tag("inc/get_recent_news.html")
def get_recent_news(cnt=3):
    recent_news = News.objects.order_by("-created_at")[:cnt]
    return {"recent_news": recent_news, "cnt": cnt}


@register.inclusion_tag("inc/get_recent_bottom.html")
def get_recent_news_bottom(cnt=3):
    recent_news_bottom = News.objects.order_by("-created_at")[:cnt]
    return {"recent_news_bottom": recent_news_bottom, "cnt": cnt}


