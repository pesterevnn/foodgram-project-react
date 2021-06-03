from django.conf import settings
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .models import Recipes, Purchases, Follows, Ingredients_Recipe


def index(request):
    curent_user = request.user
    recipes = Recipes.objects.all()
    if request.user.is_authenticated:
        purchases = Purchases.objects.filter(customer = curent_user)
        purchases_count = purchases.count()
    else:
        purchases_count = 0
    paginator = Paginator(recipes, settings.PAGINATOR_PAGE_SIZE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    section = request.resolver_match.url_name
    context = {
        'page': page,
        'recipes': recipes,
        'paginator': paginator,
        'user': curent_user,
        'purchases_count': purchases_count,
        'section': section,
    }
    return render(request, 'index.html', context)

def favorite(request):
    curent_user = request.user
    recipes = Recipes.objects.filter(favorite_authors__user=curent_user)
    if request.user.is_authenticated:
        purchases = Purchases.objects.filter(customer = curent_user)
        purchases_count = purchases.count()
    else:
        purchases_count = 0
    paginator = Paginator(recipes, settings.PAGINATOR_PAGE_SIZE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    section = request.resolver_match.url_name
    context = {
        'page': page,
        'recipes': recipes,
        'paginator': paginator,
        'user': curent_user,
        'purchases_count': purchases_count,
        'section': section,
    }
    return render(request, 'favorite.html', context)

def profile(request, username):
    curent_user = request.user
    user = get_object_or_404(get_user_model(), username=username)
    recipes = Recipes.objects.filter(author=user)
    if request.user.is_authenticated:
        purchases = Purchases.objects.filter(customer = curent_user)
        purchases_count = purchases.count()
    else:
        purchases_count = 0
    paginator = Paginator(recipes, settings.PAGINATOR_PAGE_SIZE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    section = request.resolver_match.url_name
    context = {
        'page': page,
        'recipes': recipes,
        'paginator': paginator,
        'user': curent_user,
        'author': user,
        'purchases_count': purchases_count,
        'section': section,
    }
    return render(request, 'authorRecipe.html', context)    

def follow(request):
    curent_user = request.user
    follows = Follows.objects.filter(subscriber=curent_user)
    if request.user.is_authenticated:
        purchases = Purchases.objects.filter(customer = curent_user)
        purchases_count = purchases.count()
    else:
        purchases_count = 0
    paginator = Paginator(follows, settings.PAGINATOR_PAGE_SIZE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    section = request.resolver_match.url_name
    context = {
        'page': page,
        'paginator': paginator,
        'user': curent_user,
        'follows': follows,
        'purchases_count': purchases_count,
        'section': section,
    }
    return render(request, 'myFollow.html', context)

def shoplist(request):
    curent_user = request.user
    if curent_user.is_authenticated:
        purchases = Purchases.objects.filter(customer = curent_user)
        purchases_count = purchases.count()
    else:
        purchases = None
        purchases_count = 0
    section = request.resolver_match.url_name
    context = {
        'user': curent_user,
        'purchases_count': purchases_count,
        'purchases': purchases,
        'section': section,
    }
    return render(request, 'shopList.html', context)

def recipe(request, recipe_id):
    curent_user = request.user
    recipe = Recipes.objects.get(pk=recipe_id)
    ingredients = Ingredients_Recipe.objects.filter(recipe=recipe)
    section = request.resolver_match.url_name
    if curent_user.is_authenticated:
        purchases = Purchases.objects.filter(customer = curent_user)
        purchases_count = purchases.count()
    else:
        purchases_count = 0
    context = {
        'user': curent_user,
        'purchases_count': purchases_count,
        'section': section,
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(request, 'singlePage.html', context)

def create_recipe(request):
    curent_user = request.user
    section = request.resolver_match.url_name
    if curent_user.is_authenticated:
        purchases = Purchases.objects.filter(customer = curent_user)
        purchases_count = purchases.count()
    else:
        purchases_count = 0
    context = {
        'user': curent_user,
        'section': section,
        'purchases_count': purchases_count,
    }
    return render(request, 'formRecipe.html', context)


@login_required
def profile_follow(request, username):
    author = get_object_or_404(get_user_model(), username=username)
    user = request.user
    if not author == user:
        Follows.objects.get_or_create(subscriber=user, author=author)
    return redirect('follow')


@login_required
def profile_unfollow(request, username):
    author = get_object_or_404(get_user_model(), username=username)
    user = request.user
    follow = get_object_or_404(Follows, subscriber=user, author=author)
    follow.delete()
    return redirect('follow')


def del_purchase(request, recipe_id):
    user = request.user
    recipe = get_object_or_404(Recipes, pk=recipe_id)
    purchase = get_object_or_404(Purchases, customer=user, recipe=recipe)
    purchase.delete()
    return redirect('shoplist')


def add_purchase(request, recipe_id):
    user = request.user
    recipe = get_object_or_404(Recipes, pk=recipe_id)
    Purchases.objects.get_or_create(customer=user, recipe=recipe)
    return redirect('shoplist')
