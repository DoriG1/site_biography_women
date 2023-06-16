from django.db import models
from django.urls import reverse

#класс модель - название таблицы, ее атрибуты - строки таблицы в бд
class Women(models.Model): #поле id автоматически есть в классе
    title = models.CharField(max_length=255) #определяет тектовое поле с максимальной длинной
    content = models.TextField(blank=True)   #расширенное текстовое поле
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/") #хранит ссылку на нашу фотографию поста, аплоуд говорит о том, в какой каталог будет идти наше фото
    time_create = models.DateTimeField(auto_now_add=True) #время создания постаБ авто тру будет принимать в себя значение времени и никогда не будет меняться 
    time_update = models.DateTimeField(auto_now=True) #полу будет меняться каждый раз, когда мы меняем время записи
    is_published = models.BooleanField(default=True) #тру, фолс
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})