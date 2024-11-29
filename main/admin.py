from django.contrib import admin

from main.models import House, House_info, Renting, Payment

# Register your models here.
admin.site.site_header = 'house management system'
admin.site.site_title = 'house management system'

class HouseAdmin(admin.ModelAdmin):
    list_display = ['name','type','location','house_no','plot_no']
    search_fields = ['name','type','location','house_no','plot_no']
    list_per_page = 30


class House_infoAdmin(admin.ModelAdmin):
    list_display = ['name','type','door_no','location','year']
    search_fields = ['name','type','door_no','location','year']
    list_per_page = 30




class RentingAdmin(admin.ModelAdmin):
    list_display = ['house','name','status','expected_rent_date']
    search_fields = ['house','name','status','expected_rent_date']
    list_per_page = 30




class PaymentAdmin(admin.ModelAdmin):
    list_display = ['renting','code','amount','status','created_at']
    search_fields = ['renting','code','amount','status']
    list_per_page = 30

admin.site.register(House, HouseAdmin)
admin.site.register(House_info, House_infoAdmin)
admin.site.register(Renting, RentingAdmin)
admin.site.register(Payment, PaymentAdmin)



