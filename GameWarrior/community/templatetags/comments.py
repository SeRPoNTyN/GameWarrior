from django import template
from community.models import *

register = template.Library()


@register.inclusion_tag("inc/get_count_of_comments.html")
def get_count_of_comments():
    cnt = Comments.objects.count()
    return {"cnt": cnt}


@register.inclusion_tag("inc/get_recent_comments.html")
def get_recent_comments(cnt=4):
    recent_comments = Comments.objects.order_by("-created_at")[:cnt]
    return {"recent_comments": recent_comments, "cnt": cnt}

