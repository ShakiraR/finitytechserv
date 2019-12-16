from django.contrib import admin
from finity_techserv_portfolio_website_app.models import CustomUser,Contact,Career,Quotation

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ("FirstName","LastName", "PhoneNo","Email", "Message")

class CareerAdmin(admin.ModelAdmin):
    list_display = ("Name","Email", "PhoneNo","Resume", "Message")

class QuotationAdmin(admin.ModelAdmin):
    list_display = ("Name","Email", "PhoneNo","BusinessSector", "Message")    


admin.site.register(CustomUser)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Career, CareerAdmin)
admin.site.register(Quotation, QuotationAdmin)