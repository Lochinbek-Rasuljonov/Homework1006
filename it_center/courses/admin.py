
from django.contrib import admin
from .models import Course, Lesson

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('title', 'description')

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
