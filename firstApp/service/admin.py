from django.contrib import admin
from service.models import Author,Category,BlogPost
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date','content_display','categories_display')

    
    def content_display(self, obj):
        # Displaying a truncated version of the content for brevity
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content

    def categories_display(self, obj):
        return ', '.join([category.name for category in obj.categories.all()])

    content_display.short_description = 'Content'
    categories_display.short_description = 'Categories'

 
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
 
