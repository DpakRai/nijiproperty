
from django.contrib import admin
from .models import Sellhouse,Sellhouseimage

# Register your models here.

class SellhouseimageAdmin(admin.StackedInline):
    model = Sellhouseimage

@admin.register(Sellhouse)
class SellhouseAdmin(admin.ModelAdmin):
    inlines = [SellhouseimageAdmin]
    class Meta:
        model = Sellhouse
