from django.contrib import admin

# Register your models here.

from .models import courses,callback

class courseAdmin(admin.ModelAdmin):
    list_display=('name','lang','price','image')

admin.site.register(courses,courseAdmin)

class callbackAdmin(admin.ModelAdmin):
    list_display=('name','phone','datetime')

admin.site.register(callback,callbackAdmin)
