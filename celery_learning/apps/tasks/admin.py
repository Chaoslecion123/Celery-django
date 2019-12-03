from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.tasks.tasks import send_emails_users
from django.contrib.auth.models import User

# Register your models here.

class UserAdmin(UserAdmin):
    actions = ['envio_de_correos',]

    def envio_de_correos(self,request,queryset):
        send_emails_users.delay()
        filas_actualizadas = queryset.update(is_staff=True)

        return True

admin.site.unregister(User)
admin.site.register(User,UserAdmin)