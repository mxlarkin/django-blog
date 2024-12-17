from django.contrib import admin

from blogging.models import Post, Category

# from myproject.admin_site import custom_admin_site

# Register your models here.


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]


admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)


admin.site.register(Category, CategoryAdmin)
