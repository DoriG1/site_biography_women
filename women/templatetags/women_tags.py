from django import template
from women.models import *

#регистрация собственных шаблонов 
register = template.Library()

#создаем тег из функции ниже
@register.simple_tag()
#выбор всех записей из таблицы категории
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

#включающий тег
@register.inclusion_tag('women/list_categories.html')
#чтение всех категорий и возвращение словаря, параметр возвращения атоматические передается параметру list_categories.html
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}