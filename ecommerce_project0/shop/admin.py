from django.contrib import admin

# Register your models here.
from . models import category,product



class categoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_Field={'slug':('name',)}
admin.site.register(category,categoryAdmin)
class productAdmin (admin.ModelAdmin):
    list_display = ['name','stock','price','available','created','update',]
    list_editable = ['price','stock','available',]
    prepopulated_Field = {'slug': ('name',)}
    list_per_page = 20
admin.site.register(product,productAdmin)

