from django.contrib import admin

from .models import Category, Course, Lesson, Comment


# The inline thing, will take all comments that are related to the id of lesson
class LessonCommentInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['lesson']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'status',
                    'lesson_type']  # Adds pretty table
    list_filter = ['status', 'lesson_type']  # Adds filtering
    search_fields = ['title', 'short_description',
                     'long_description']  # Adds a search bar
    inlines = [LessonCommentInline]  # Will implement the inline


admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Comment)
