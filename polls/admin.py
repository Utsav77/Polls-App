from django.contrib import admin

# Register your models here.
from .models import Question, Choice
'''
admin.site.register(Question)
admin.site.register(Choice)
'''

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)