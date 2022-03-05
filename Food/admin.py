from django.contrib import admin
from .models import Foods, FoodPlan, FoodCategory, FoodPlanItems
from django.utils.html import format_html
# Register your models here.
@admin.register(Foods)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('show_image', 'food_name', 'food_category')
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (('food_name', 'food_image', 'food_category'),),
        }
        ),)

    def show_image(self, obj):
        if (obj.food_image):
            return format_html('<img src="{}" width=50 height=50/>', obj.food_image.url)
        return '-'


@admin.register(FoodPlanItems)
class FoodPlanItemsAdmin(admin.ModelAdmin):
    list_display = ('food_plan' , 'foods' , 'days')
    fieldsets = (
        (None, {
            "classes" : 'wide' ,
            "fields": (
                ('food_plan' , 'foods' , 'count' , 'days') , 'food_details'
            ),
        }),
    )
    

@admin.register(FoodPlan)
class FoodPlanAdmin(admin.ModelAdmin):
    list_display = ('athlete', 'start_date', 'end_date', 'status')
    fieldsets = (
        (None, {
            "classes": ('wide', ),
            "fields": (
                ('status', 'athlete', 'end_date'),
            ),
        }),
    )


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('show_image', 'title', 'parent')
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (('title', 'image', 'parent'),),
        }
        ),)

    def show_image(self, obj):
        if (obj.image):
            return format_html('<img src="{}" width=50 height=50/>', obj.image.url)
        return '-'
