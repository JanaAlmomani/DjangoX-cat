from django.contrib import admin
# Register your models here.
from .models import Cat

class CustomCatAdmin(admin.ModelAdmin):
    model = Cat
    list_display = ['name', 'purchaser', 'cat_type',]
    fieldsets= (
        ('Owner',{
            'fields':('purchaser',
            )}
        ),
        ('cat info',{
            'fields':('name','cat_type',
            )}
        )
    )

    
admin.site.register(Cat, CustomCatAdmin)