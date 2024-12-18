from django import forms
from .models import Course, Lesson

class CourseForm(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        "placeholder": "Kurs nomi",
        'class': "form-control"
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "Kurs tavsifi",
        'class': "form-control",
        "rows": 3
    }))

    def create(self):
        course = Course.objects.create(**self.cleaned_data)
        return course

class LessonForm(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        "placeholder": "Dars nomi",
        'class': "form-control"
    }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "Dars matni",
        'class': "form-control",
        "rows": 3
    }))
    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(attrs={
        "class": "form-select"
    }))

    def create(self):
        lesson = Lesson.objects.create(**self.cleaned_data)
        return lesson