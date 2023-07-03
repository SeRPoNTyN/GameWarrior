from django import template
from GameDB.models import *
from Blog.models import News

register = template.Library()


@register.inclusion_tag("inc/get_recent_games.html")
def get_recent_games(cnt=3):
    recent_games = Game.objects.order_by("-created_at").select_related("category").prefetch_related("tag")[:cnt]
    return {"recent_games": recent_games, "cnt": cnt}


@register.inclusion_tag("inc/get_recent_games_single.html")
def get_recent_games_single(cnt=3):
    recent_games_single = Game.objects.order_by("-created_at").select_related("category").prefetch_related("tag")[:cnt]
    return {"recent_games_single": recent_games_single, "cnt": cnt}


@register.inclusion_tag("inc/get_popular_games.html")
def get_popular_games(cnt=3):
    popular_games = Game.objects.order_by("-views").select_related("category").prefetch_related("tag")[:cnt]
    return {"popular_games": popular_games, "cnt": cnt}


@register.inclusion_tag("inc/get_popular_games_single.html")
def get_popular_games_single(cnt=1):
    popular_games = Game.objects.order_by("-views").select_related("category").prefetch_related("tag")[:cnt]
    return {"popular_games": popular_games, "cnt": cnt}
