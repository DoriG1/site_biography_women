#render - встроенный шаблонизатор, который производит его обработку
#шаблон - конструкция для отображения информации
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = [{'title':"О сайте", 'url_name': 'about'}, 
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная ствязь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]

def index(request): #ссылка на класс, которая содержит всю информацию
    posts = Women.objects.all() #все записи в бд
    cats = Category.objects.all()
    context = {'posts': posts, 
               'cats': cats, 
               'menu': menu,
               'title': 'Главная страница',
               'cat_selected': 0}
    
    return render(request, 'women/index.html', context=context) #в индекс будет предстляться то, что есть в файле индекс

def about(request): 
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})

def addpage(request): 
    return HttpResponse("Добавление статьи")

def contact(request): 
    return HttpResponse("Обратная ствязь")

def login(request):
    return HttpResponse("Авторизация")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id) #все записи в бд
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404

    context = {'posts': posts, 
               'cats': cats, 
               'menu': menu,
               'title': 'Отображение по рубрикам',
               'cat_selected': cat_id}
    
    return render(request, 'women/index.html', context=context) 