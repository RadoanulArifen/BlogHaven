from django.contrib import admin
from .models import Post,Category
# Register your models here.
admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'category', 'created_at')
    search_fields = ('title', 'content', 'category__name')