
from django.contrib import admin
from .models import Renthouse,Renthouseimage

# Register your models here.

class RenthouseimageAdmin(admin.StackedInline):
    model = Renthouseimage

@admin.register(Renthouse)
class RenthouseAdmin(admin.ModelAdmin):
    inlines = [RenthouseimageAdmin]
    
    class Meta:
        model = Renthouse
