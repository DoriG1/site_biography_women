from django import forms
from .models import *

#класс формы добавления с полями для заполния пользователем
class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs): #конструктор
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана" # меняем свойство empty_label для cat

    class Meta:
        model = Women #связь с моделью
        # fields = '__all__' #все поля показывает, кро тех, что заполняются автоматически
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat'] #показывает только эти поля в Добавить статью
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}), #стиль оформления
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    #пользовательский валидатор
    def clean_title(self):
        title = self.cleaned_data('title')
        if len(title) > 200:
            raise forms.ValidationError('Длина превышает 200 символов')
        
        return title