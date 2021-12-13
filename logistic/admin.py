from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import *


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_active', 'Address_1', 'Address_2')
    search_fields = ('email','username', 'Address_1')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class TrackingAdmin(admin.ModelAdmin):
    readonly_fields = ('Shipment_Number',)
    list_display = ('Shipment_Number', 'order', 'Package', 'Status','Arrive_Date', 'Pickup_Location', 'Updated')

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)
    list_display = ('ID', 'user','Package', 'Order_Date')
    
class PackageAdmin(admin.ModelAdmin):
    list_display = ('ID', 'Packs', 'Description')

class BranchesAdmin(admin.ModelAdmin):
    list_display=('Name','Office')


admin.site.register(Account, AccountAdmin)
admin.site.register(Tracking, TrackingAdmin)
admin.site.register(Orders, OrderAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(Bracnh, BranchesAdmin)
admin.site.register(Office)
admin.site.register(Warehouse)