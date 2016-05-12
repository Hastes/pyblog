from firstapp.models import Poll, Choice
from django.contrib import admin

#Добавления связанных объектов (отобразим Choice)
#Варианты отображения TabularInline и StackedInline
class ChoiceInline(admin.TabularInline):
#class ChoiceInline(admin.StackedInline):
    model = Choice
	#Показать 3 формы для добавления вариантов ответа.
    extra = 3

#Изменим порядок полей в админке
#fieldsets - название группы полей.
#Во второй строке класс "collapse", отображает группу полей изначально скрытой.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Тут дата кароч',   {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    #Варианты ответов редактируются на странице вопроса.
    inlines = [ChoiceInline]
    #Отображение доп.полей в отображении списка вопросов
    list_display = ('question', 'pub_date')
    #Добавим поле поиска(будет искать по указанному полю):
    search_fields = ['question']
    #Заголовок админки
    admin.AdminSite.site_header = "I'm AMDIN mothefucker bitch"


admin.site.register(Poll, QuestionAdmin)

#admin.site.register(Poll)