from django.contrib import admin
from blog.models import Post , blogcomment
# Register your models here.


admin.site.register((blogcomment))
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)