#render - встроенный шаблонизатор, который производит его обработку
#шаблон - конструкция для отображения информации
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .forms import AddPostForm
from .models import *

menu = [{'title':"О сайте", 'url_name': 'about'}, 
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная ствязь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]

def index(request): #ссылка на класс, которая содержит всю информацию
    posts = Women.objects.all() #все записи в бд
    context = {'posts': posts, 
               'menu': menu,
               'title': 'Главная страница',
               'cat_selected': 0,}
    
    return render(request, 'women/index.html', context=context) #в индекс будет предстляться то, что есть в файле индекс

def about(request): 
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})

def addpage(request): 
    form = AddPostForm()
    return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title':'Добавление статьи'})

def contact(request): 
    return HttpResponse("Обратная ствязь")

def login(request):
    return HttpResponse("Авторизация")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {'post': post, #прочитанный пост
               'menu': menu, #главное меню
               'title': post.title, #заголовок статьи
               'cat_selected': post.cat_slug,} #номер рубрики
    
    return render(request, 'women/post.html', context=context)

def show_category(request, cat_slug):
    posts = Women.objects.filter(cat_id=Category.objects.get(slug=cat_slug)) #все записи в бд

    if len(posts) == 0:
        raise Http404

    context = {'posts': posts, 
               'menu': menu,
               'title': 'Отображение по рубрикам',
               'cat_selected': cat_slug,}
    
    return render(request, 'women/index.html', context=context) 