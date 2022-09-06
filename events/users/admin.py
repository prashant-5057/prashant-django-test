from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name','is_superuser', ]
    
    exclude = ('groups', 'created_at', 'user_permissions', 'date_joined', 'last_login', 'is_active')
    search_fields = ('email','first_name', 'last_name')

    # def get_email(self, obj):
    #     return obj.email if obj.email else "Guest user"
    # get_email.short_description = "Email"

    # def save_model(self, request, obj, form, change):
    #     # Override this to set the password to the value in the field if it's
    #     obj.is_staff = True
    #     if obj.pk:
    #         orig_obj = User.objects.get(pk=obj.pk)
    #         if obj.password != orig_obj.password:
    #             obj.set_password(obj.password)
    #     else:
    #         obj.set_password(obj.password)
    #     obj.save()



admin.site.site_header = "Sapid App Admin"
admin.site.site_title = "Sapid App Admin"
admin.site.index_title = "Sapid App Admin"

