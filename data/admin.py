from django.contrib import admin
from data.models import SubmitData, RequestData, Category, Articles


class SubmitDataAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'research_topic',
    'research_location',)

admin.site.register(SubmitData, SubmitDataAdmin)

class RequestDataAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','designation', 'email', 'phone_number')

admin.site.register(RequestData, RequestDataAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
admin.site.register(Category, CategoryAdmin)

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'access', 'category', 'date_created')
admin.site.register(Articles, ArticlesAdmin)
