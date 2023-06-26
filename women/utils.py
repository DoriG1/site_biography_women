from .models import *
from django.db.models import Count

menu = [{'title':"О сайте", 'url_name': 'about'}, 
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]

class DataMixin:
    def get_user_context(self, **kwargs): #формирует нужный контекст по умолчанию
        context = kwargs #сформируем начальный словарь из тех параметров, которые были переданы функции
        cats = Category.objects.annotate(Count('women'))
        
        user_menu = menu.copy()
        if not self.request.user.is_authenticated: # если пользователь незареган, то не показывает вкладку добавить статью
            user_menu.pop(1)
        
        context['menu'] = user_menu        # контекст для меню

        context['cats'] = cats        # контекст для рубрик
        if 'cat_selected' not in context: # если ключ кваргов определяется в контекстеБ то он отображается, если не присутствует, то по умолчанию будте ноль
            context['cat_selected'] = 0
        return context