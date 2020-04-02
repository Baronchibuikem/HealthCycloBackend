from django.contrib import admin
from accounts.models import CustomUser, ContactUs, Subscribe


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'organization',
                    'designation', 'purpose_of_data', ]
    list_filter = ['organization', 'purpose_of_data']
    search_fields = ['organization', 'purpose_of_data']
    list_per_page = 50


admin.site.register(CustomUser, CustomUserAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['email', 'subject']
    list_filter = ['email']
    search_fields = ['email', 'subject', 'content']


admin.site.register(ContactUs, ContactUsAdmin)


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ["email"]
    list_filter = ["email"]
    search_fields = ['email']


admin.site.register(Subscribe, SubscribeAdmin)
