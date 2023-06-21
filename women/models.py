from django.db import models
from django.urls import reverse

#класс модель - название таблицы, ее атрибуты - строки таблицы в бд
class Women(models.Model): #поле id автоматически есть в классе
    title = models.CharField(max_length=255, verbose_name="Заголовок") #определяет тектовое поле с максимальной длинной
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL") #отображение статей по слагу
    content = models.TextField(blank=True, verbose_name="Текст статьи")   #расширенное текстовое поле
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото") #хранит ссылку на нашу фотографию поста, аплоуд говорит о том, в какой каталог будет идти наше фото
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания") #время создания постаБ авто тру будет принимать в себя значение времени и никогда не будет меняться 
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения") #полу будет меняться каждый раз, когда мы меняем время записи
    is_published = models.BooleanField(default=True, verbose_name="Публикация") #тру, фолс
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
    
    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['-time_create', 'title']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
    
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категория'
        ordering = ['id']