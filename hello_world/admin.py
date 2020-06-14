from django.contrib import admin
from hello_world.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
