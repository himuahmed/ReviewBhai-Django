from django.contrib import admin
from.models import Review,Tag,Item, RestaurentOrPlace, Star
# Register your models here.
admin.site.register(Review)



class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','type','food_or_travel','date_added')
    search_fields = ('name','type','food_or_travel','date_joined')
    read_only = ('date_added')

    fieldsets = ()
    filter_horizontal = ()
    list_filter = ()

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name','foods_or_travel','date_added')
    search_fields = ('tag_name','foods_or_travel','date_joined')
    read_only = ('date_added')

    fieldsets = ()
    filter_horizontal = ()
    list_filter = ()

class RestaurentAdmin(admin.ModelAdmin):
    list_display = ('name','location','restaurent_place','created_at')
    search_fields = ('name','location','restaurent_place','created_at')
    read_only = ('created_at')

    fieldsets = ()
    filter_horizontal = ()
    list_filter = ()


class RatingsAdmin(admin.ModelAdmin):
    list_display = ('post_id','food','environment','service','cleanliness')
    search_fields = ('post_id','food','environment','service','cleanliness')
    read_only = ('post_id')

    fieldsets = ()
    filter_horizontal = ()
    list_filter = ()


admin.site.register(Tag,TagAdmin)
admin.site.register(Item,ItemAdmin)
admin.site.register(RestaurentOrPlace,RestaurentAdmin)
admin.site.register(Star,RatingsAdmin)