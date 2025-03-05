from django.contrib import admin
# from unfold.admin import admin.ModelAdmin
from carts.admin import CartTabAdmin
from orders.admin import OrderTabulareAdmin
from users.models import User

#admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    #exclude=['slug',] # fields = [,]
    #exclude=[] # fields = [,]
    prepopulated_fields={'slug':('first_name','last_name',)} 
#     list_display=['username','first_name','last_name','email','image','familyName','name','secondName','enterprise','dateOfBirth','address','telephones','photo','note','slug']
#     list_editable=['first_name','last_name','email','image','familyName','name','secondName','enterprise','dateOfBirth','address','telephones','photo','note','slug']
#     search_fields=['username','first_name','last_name','email','image','familyName','name','secondName','enterprise','dateOfBirth','address','telephones','photo','note','slug']
#     list_filter=['username','first_name','last_name','email','image','familyName','name','secondName','enterprise','dateOfBirth','address','telephones','photo','note','slug']
#     fields=['username','first_name','last_name','email','image','familyName','name','secondName','enterprise','dateOfBirth','address','telephones','photo','note','slug']

    inlines=[CartTabAdmin,OrderTabulareAdmin] 