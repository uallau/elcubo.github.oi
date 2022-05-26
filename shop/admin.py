from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import Shop

@admin.register(Shop)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('product',), }
    fields = ('product','price','overview','material','posted','photo','slug', 'user')
    list_filter = (
    ('posted', DateFieldListFilter),
  )
    list_display = ('product','price','overview','material','posted','photo')