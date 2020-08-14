from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from homepage.models import Recipe, Author
from homepage.forms import RecipeForm, AuthorForm, LoginForm, SignupForm

# Create your views here.


def index(request):
    my_recipes = Recipe.objects.all()
    return render(request, "index.html", {"Recipes": my_recipes, "welcome_name": "fellows"})


def post_detail(request, post_id):
    my_recipe = Recipe.objects.filter(id=post_id).first()
    return render(request, "post_detail.html", {"post": my_recipe})


@login_required
def author_form_view(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))
    form = AuthorForm()
    return render(request, "generic_form.html", {"form": form})


@login_required
def recipe_form_view(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data.get('title'),
                description=data.get('description'),
                author=request.user.author,
                time_required=data.get('time_required'),
                instructions=data.get('instructions'),
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = RecipeForm()
    return render(request, "generic_form.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                "username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
            # if not user:
            #     return HttpResponseRedirect(reverse("loginview"))

    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(username=data.get(
                "username"), password=data.get("password"))
            Author.objects.create(name=data.get("username"), user=new_user)
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))

    form = SignupForm()
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
