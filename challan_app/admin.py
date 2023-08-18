from django.contrib import admin
from challan_app.models import Universal,Police,Payment,Challan,Contact
# Register your models here.

# admin.site.register(Universal)
# admin.site.register(Police)
# admin.site.register(Payment)
# admin.site.register(Challan)

@admin.register(Universal)
class universalAdmin(admin.ModelAdmin):
    list_display = ['Name','License_number','Vehicle_number','Phone_number','Mail','Insurance_number','Registration_number','Address']

@admin.register(Police)
class PoliceAdmin(admin.ModelAdmin):
    list_display = ['Name','Id','Phone_number','Rank']

@admin.register(Challan)
class ChallanAdmin(admin.ModelAdmin):
    list_display = ['Challan_number','Offense_date','Offense_time','Payment_status','Fees','Offences','Vehicle_number','Police_id','Location']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['Challan_number','Account_number','IFSC','Upi','Transaction_id']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['Name','Mail','Phone_number','Message','Date']