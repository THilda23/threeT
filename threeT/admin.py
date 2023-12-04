from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Question, Choice, UserChoice, Type

class QuestionAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Question, QuestionAdmin)

class ChoiceAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Choice, ChoiceAdmin)

class UserChoiceAdmin(ImportExportModelAdmin):
    pass

admin.site.register(UserChoice, UserChoiceAdmin)

class TypeAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Type, TypeAdmin)
