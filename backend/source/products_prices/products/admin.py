from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price")
    readonly_fields = ("created_at", "updated_at", "created_by", "last_modified_by")

    def get_form(self, request, obj=None, **kwargs):
        Product.created_by = request.user
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.last_modified_by = request.user
        obj.save()
