from django.contrib import admin
from buyproperty.models import *



class HouseImageAdmin(admin.StackedInline):
    model = HouseImage


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    inlines = [HouseImageAdmin]

    class Meta:
        model = House

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    class Meta:
        model = Comment

