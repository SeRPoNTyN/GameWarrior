from django.db.models import F
from django.contrib.auth import logout, login
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = UserLoginForm()
    return render(request, "Community/login.html", {'form': form})


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserRegisterForm()
    return render(request, "Community/register.html", {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')


class Forum(ListView):
    template_name = "Community/forum.html"
    model = Comments
    context_object_name = "comments"
    paginate_by = 10


def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("forum")
    else:
        form = CommentForm()
    return render(request, 'Community/add_comment.html', {'form': form})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data["subject"], form.cleaned_data["content"], "nector16@mail.ru", ["serpontynfunny@mail.ru"], fail_silently=False)
            if mail:
                messages.success(request, "Письмо отправлено!")
                return redirect("home")
            else:
                messages.error(request, "Ошибка отправки.")
                return redirect("contact")
        else:
            messages.error(request, "Ошибка валидации.")
    else:
        form = ContactForm()
    return render(request, "Community/contact.html", {"form": form})


def del_comment(request, pk):
    if Comments.objects.get(pk=pk):
        Comments.objects.get(pk=pk).delete()
        return redirect('forum')
    else:
        return redirect("home")


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return HttpResponse(ip)

