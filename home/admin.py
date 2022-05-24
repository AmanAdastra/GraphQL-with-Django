from django.contrib import admin
from home.models import Quiz
# Register your models here.

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):  
    list_display = ('name', 'description', 'created_at', 'updated_at')