from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Cat, Category, Color, Gender, CustomUser


# Register your models here.

class CatAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'gender', 'color','category', 'created', 'author', 'views', 'get_photo']
    list_filter = ['created', 'author', 'views', 'category']
    search_fields = ['name', 'description']
    list_editable = ['author', 'category', 'gender', 'color', 'age']
    list_display_links = ['id', 'name']

    def get_photo(self, obj):
        if obj.photo:
            img_url = obj.photo.url
        else:
            img_url = 'https://th.bing.com/th/id/R.b0c7ab518af5603f5a1c810fb1ea624e?rik=TdtmlXKQaswPmg&pid=ImgRaw&r=0'
        return mark_safe(f'<img src="{img_url}" width="75px"')
    get_photo.short_description = 'Photo'


admin.site.register(Cat, CatAdmin)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Gender)
admin.site.register(CustomUser)

