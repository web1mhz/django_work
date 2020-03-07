from django.contrib import admin
from blog.models import Post

# Register your models here.

#admin.site.register(Post)
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links=['title']

