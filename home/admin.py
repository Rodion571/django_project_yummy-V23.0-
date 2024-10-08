from django.contrib import admin
from .models import Category, Dish, Gallery, Contact, Reservation, FooterItems


admin.site.register(FooterItems)
admin.site.register(Reservation)
admin.site.register(Gallery)
admin.site.register(Contact)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible', 'sort', 'created_at', 'updated_at')
    list_editable = ('is_visible', 'sort')
    list_filter = ('is_visible', 'created_at', 'updated_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'


admin.site.register(Dish)
