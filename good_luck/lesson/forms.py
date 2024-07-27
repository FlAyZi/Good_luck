from django import forms
from .models import Lesson, Category


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
