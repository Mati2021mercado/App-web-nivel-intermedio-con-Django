from django.contrib import admin
from .models import Category, Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
class PostAdmin(admin.ModelAdmin):
    #solo lectura
    readonly_fields = ('created', 'updated')
    #columnas que queremos mostrar
    list_display = ('title','author','published')
    #ordenar por
    ordering = ('author', 'published')
    #campos de busqueda
    search_fields = ('title','content','author__username','categories__name')
    #navegacion 
    date_hierarchy = 'published'
    #filtro
    list_filter = ('author__username','categories__name')
    
    def post_categories(self,obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorias"
    
    
    #registramos lo cambios en el administrador
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)