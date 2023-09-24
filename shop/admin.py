from django.contrib import admin

# Register your models here.
from .models import Category, Product, Course, Person, Department,Material


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Product,ProductAdmin)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Person)
admin.site.register(Material)