# company/admin.py
from django.contrib import admin
from .models import Factory, Company, Address
from .models import Product, CompanyProduct, Customer, SalesContract



class FactoryInline(admin.TabularInline):
    model = Factory

class CompanyProductInline(admin.TabularInline):
    model = CompanyProduct

# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
	# class Meta:
	# 	model = Company
	list_display = ['name', 'category', 'homepage', 'contact']
	inlines = [ CompanyProductInline, FactoryInline ]

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
	class Meta:
		model = Address
	list_display = ['large', 'middle', 'small', 'created_at']
	list_per_page = 1000

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	class Meta:
		model = Product
	list_display = ['en_name', 'cn_name', 'casno', 'hscode']
	inlines = [ CompanyProductInline ]

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	class Meta:
		model = Customer
	list_display = ['en_name', ]

@admin.register(SalesContract)
class SalesContractAdmin(admin.ModelAdmin):
	class Meta:
		model = SalesContract
	list_display = ['name', 'customer', 'product', 'sales_amount', 'unitprice']

