from django.contrib import admin
from .models import Post, Category, User, Comment

class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('title_post', 'author', 'time_in')
    list_filter = ('author', 'time_in')
    search_fields = ('author', 'time_in')

# admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
# admin.site.register(User)
admin.site.register(Comment)

# Register your models here.
