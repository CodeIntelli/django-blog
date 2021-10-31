from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Post

# for configuring categories model


class CategoryModel(admin.ModelAdmin):
    list_display = ("title", "description", "url", "image_show", "add_date")
    # summernote_fields = "description"
    # for search field this command is used
    search_fields = ("title", "url", "add_date")
    list_per_page = 10


# class PostModel(SummernoteModelAdmin):


class PostModel(admin.ModelAdmin):
    list_display = ("title", "content", "url", "image_show", "cat")
    # summernote_fields = "content"
    # for pagination this command use`
    list_per_page = 10
    # for filter this command is used
    list_filter = ("cat",)

    class Media:
        js = (
            'https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)
        # css = ('css/adminStyle.css',)


# Register your models here.
admin.site.register(Category, CategoryModel)
admin.site.register(Post, PostModel)
