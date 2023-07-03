from django import template
from Blog.models import *

register = template.Library()


@register.inclusion_tag("inc/get_recent_reviews.html")
def get_recent_reviews(cnt=4):
    recent_reviews = Review.objects.order_by("-created_at")[:cnt]
    return {"recent_reviews": recent_reviews, "cnt": cnt}


@register.inclusion_tag("inc/get_most_popular_review.html")
def get_most_popular_reviews(cnt=1):
    popular_reviews = Review.objects.order_by("-views")[:cnt]
    return {"popular_reviews": popular_reviews, "cnt": cnt}


@register.inclusion_tag("inc/get_recent_reviews_blog.html")
def get_recent_reviews_blog(cnt=4):
    recent_reviews = Review.objects.order_by("-created_at")[:cnt]
    return {"recent_reviews": recent_reviews, "cnt": cnt}
