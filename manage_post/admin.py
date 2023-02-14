from django.contrib import admin
from manage_post.models import Category, Article, Rating
from django.contrib.auth import get_user_model
User = get_user_model()
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    # Devolver artículos relacionados con el usuario
    def get_queryset(self, request):
        if request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(user_id=request.user)

    # Devolver nombre de usuario relacionado con el usuario autenticado
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if (request.user.is_superuser) and (db_field.name == "user_id"):
            kwargs['queryset'] = User.objects.filter(is_staff=1)
        else:
            kwargs['queryset'] = User.objects.filter(id=request.user.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Rating)