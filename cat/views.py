from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import Cat, Category, Color, Gender, CustomUser, Comment
from .forms import CatForm, LoginForm, RegisterForm, CommentForm
from django.contrib.auth.decorators import permission_required

# Create your views here.

def all_cats(request):
    cats = Cat.objects.all()
    categories = Category.objects.all()
    colors = Color.objects.all()
    genders = Gender.objects.all()
    context = {
        'cats': cats,
        'title': 'All Cats',
        'categories': categories,
        'colors': colors,
        'genders': genders,
    }
    return render(request, 'cat/index.html', context)


def all_cats_by_category(request, category):
    categories = Category.objects.all()
    category = Category.objects.get(name=category)
    cats = Cat.objects.filter(category=category)
    colors = Color.objects.all()
    genders = Gender.objects.all()
    context = {
        'cats': cats,
        'title': 'Cat by Category',
        'categories': categories,
        'colors': colors,
        'genders': genders,
    }

    return render(request, 'cat/index.html', context)


def all_cats_by_color(request, color):
    colors = Color.objects.all()
    color = Color.objects.get(name=color)
    cats = Cat.objects.filter(color=color)
    categories = Category.objects.all()
    genders = Gender.objects.all()
    context = {
        'cats': cats,
        'title': 'Cat by Category',
        'categories': categories,
        'colors': colors,
        'genders': genders,
    }
    return render(request, 'cat/index.html', context)

def all_cats_by_gender(request, gender):
    colors = Color.objects.all()
    gender = Gender.objects.get(name=gender)
    cats = Cat.objects.filter(gender=gender)
    categories = Category.objects.all()
    genders = Gender.objects.all()
    context = {
        'cats': cats,
        'title': 'Cat by Category',
        'categories': categories,
        'colors': colors,
        'genders': genders,
    }
    return render(request, 'cat/index.html', context)

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    comments = Comment.objects.filter(post_id=cat_id)
    cat.views += 1
    cat.save()
    context = {
        'cat': cat,
        'form': CommentForm,
        'title': 'Cat Detail',
        'comments': comments
    }
    return render(request, 'cat/cat_detail.html', context)


def cat_create(request):
    form = CatForm(request.POST, files=request.FILES)
    if form.is_valid():
        cat = form.save(commit=False)
        cat.author = request.user
        cat.save()
        return redirect('index')
    context = {
        'form': form,
        'title': 'Cat Create',
    }
    return render(request, 'cat/cat_form.html', context)

def cat_update(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    form = CatForm(request.POST or None, instance=cat, files=request.FILES or None)
    if form.is_valid():
        cat = form.save(commit=False)
        cat.author = request.user
        cat.save()
        return redirect('index')
    context = {
        'form': form,
        'title': 'Cat Update',
    }
    return render(request, 'cat/cat_form.html', context)

def cat_delete(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    if request.method == 'POST':
        cat.delete()
        return redirect('index')
    context = {
        'cat': cat,
        'title': 'Cat Delete',
    }
    return render(request, 'cat/cat_delete.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome to cats planet, {user.username}!')
            return redirect('index')
        if form.errors:
            for error in form.error_messages.values():
                messages.error(request, f'{error}')

    form = LoginForm()
    return render(request, 'cat/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.warning(request, f' You logged out of the site!')
    return redirect('login')

def user_register(request):
    form = RegisterForm(data=request.POST)
    if form.is_valid():
        user = form.save()
        messages.success(request, f'User created successfully, now, login {user.username}!')
        return redirect('login')

    form = RegisterForm()
    context = {
        'form': form,
        'title': 'Register'
    }
    return render(request, 'cat/register.html', context)



def user_profile(request, username):
    if request.user.username == username or request.user.is_superuser:

        user = User.objects.get(username=username)
        cats = Cat.objects.filter(author=user)
        context = {
            'user': user,
            'title': 'Profile',
            'cats': cats
        }
        try:
            custom_user = CustomUser.objects.get(user=user)
            context['custom_user'] = custom_user
        except:
            pass
        return render(request, 'cat/profile.html', context)
    return HttpResponse('page not found')

def comment(request, cat_id):
    if request.method == 'POST':
        cat = Cat.objects.get(pk=cat_id)
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = cat
            comment.commentator = request.user
            comment.save()
            messages.success(request, 'Comment added!')
            return redirect('cat_detail', cat_id)
    return HttpResponse('Page not found')


def test(request):
    print(request, '--------------------------------------------------')


































def contact(request):
    return render(request, 'cat/contact.html')