from django.db.models import F
from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import ListView, DetailView
from .models import *


class GetRevs(ListView):
    template_name = "Blog/Blogmain.html"
    model = Review
    context_object_name = "reviews"
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Reviews"
        return context

    def get_queryset(self):
        return Review.objects.all()


def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ReviewForm()
    return render(request, 'blog/create_review.html', {'form': form})


class GetReview(DetailView):
    template_name = "Blog/single_review.html"
    model = Review
    context_object_name = "review"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F("views") + 1
        self.object.save()
        self.object.refresh_from_db()
        return context

    def get_queryset(self):
        return Review.objects.filter(slug=self.kwargs["slug"])


