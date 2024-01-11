from django.contrib import admin
from .models import Services
# Register your models here.


class ServicesAdmin(admin.ModelAdmin):
    #creo campos de solo lectura con readonly_fields
    readonly_fields = ('created', 'updated')
    
#registro el servicio y su configuracion
admin.site.register(Services,ServicesAdmin)