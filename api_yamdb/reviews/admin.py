from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
    )


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
    )


class TitleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "year",
        "description",
        "category",
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "text",
        "pub_date",
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "title",
        "text",
        "score",
        "pub_date",
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Title, TitleAdmin)
