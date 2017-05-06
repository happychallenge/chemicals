# company/models.py
import csv
from django.db import models

USD = 'D'
RMB = 'R'
PAYMENT = (
	(USD, 'US$'),
	(RMB, 'RMB'),
)

class Address(models.Model):
	"""docstring for Address"""
	""" Address """
	large = models.CharField(max_length=30)
	middle = models.CharField(max_length=30)
	small = models.CharField(max_length=30, blank=True, null=True)

	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['id']

	def __str__(self):
		return '{} {}'.format(self.large, self.middle)

def read_region_data():
	with open('china_city.csv', 'r') as file:
		reader = csv.DictReader(file, delimiter=',')

		for index,row in enumerate(reader):
			large = row.get('large')
			middle = row.get('middle')
			small = row.get('small')
			print(index, large, middle, small)

			large = large.strip()
			middle = middle.strip()
			small = small.strip()
			reg, created = Address.objects.get_or_create(large=large, middle=middle, small=small)


# Create your models here.
class Company(models.Model):
	"""docstring for Company"""
	""" Company """
	TRADE = 'T'
	PRODUCTION = 'P'
	MIX = 'M'
	CATEGORY = (
		(TRADE, '무역'),
		(PRODUCTION, '생산'),
		(MIX, '생산무역겸임'),
	)
	name = models.CharField(max_length=30, verbose_name='중문이름')
	en_name = models.CharField(max_length=50, verbose_name='영문이름')
	category = models.CharField(max_length=1, choices=CATEGORY, 
					default=PRODUCTION, verbose_name='생산여부')
	homepage = models.URLField(max_length=100, blank=True, null=True)
	location = models.ForeignKey(Address, blank=True, null=True)
	contact = models.CharField(max_length=50, blank=True, null=True)
	tel = models.CharField(max_length=50, blank=True, null=True)
	fax = models.CharField(max_length=50, blank=True, null=True)
	email = models.EmailField(max_length=50, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	# def get_absolute_url(self):
	# 	return reverse('company:company_detail', args=[self.id])


class Factory(models.Model):
	"""docstring for Factory"""
	""" Factory """
	name = models.CharField(max_length=30)
	location = models.ForeignKey(Address, null=True, blank=True)
	company = models.ForeignKey(Company)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Product(models.Model):
	"""docstring for Product"""
	""" Product """
	en_name = models.CharField(max_length=30, verbose_name='영문이름')
	cn_name = models.CharField(max_length=50, verbose_name='중문이름')
	casno = models.CharField(max_length=30, verbose_name='CAS No.')
	hscode = models.CharField(max_length=30, verbose_name='HS CODE')
	chemical_atomic = models.CharField(max_length=50, verbose_name='화학식')
	atomic_amount = models.FloatField(verbose_name='분자량')
	image = models.ImageField(verbose_name='구조식', upload_to="chemical/")
	usage = models.TextField(verbose_name='용도', null=True, blank=True)
	including = models.CharField(max_length=1000, null=True, blank=True,
					verbose_name='成分含量')
	appearance1 = models.CharField(max_length=1000, null=True, blank=True,
					verbose_name='乌洛托品请注明外观')
	appearance2 = models.CharField(max_length=1000, null=True, blank=True,
					verbose_name='6-己内酰胺请注明外观')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.en_name

	# def get_absolute_url(self):
	# 	return reverse('company:post_detail', args=[self.id])


class CompanyProduct(models.Model):
	"""docstring for CompanyProduct"""
	""" 설명 """

	company = models.ForeignKey(Company)
	product = models.ForeignKey(Product)
	currency = models.CharField(max_length=1,choices=PAYMENT, default=RMB)
	price = models.FloatField(null=True, blank=True)
	exchange_rate = models.FloatField(null=True, blank=True)
	rmb_price = models.FloatField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{} {}'.format(self.company, self.product)


class Customer(models.Model):
	"""docstring for Customer"""
	""" 설명 """
	en_name = models.CharField(max_length=30, verbose_name='영문이름')
	address = models.CharField(max_length=200)
	tel = models.CharField(max_length=20, null=True, blank=True)
	fax = models.CharField(max_length=20, null=True, blank=True)
	email = models.CharField(max_length=50, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.en_name


class SalesContract(models.Model):
	"""docstring for SalesContract"""
	""" 설명 """
	name = models.CharField(max_length=30)
	customer = models.ForeignKey(Customer)
	product = models.ForeignKey(Product)
	sales_amount = models.IntegerField()
	unitprice = models.FloatField()
	currency = models.CharField(max_length=1,choices=PAYMENT, default=USD)
	packaging = models.CharField(max_length=100)

	portofloading = models.CharField(max_length=100, verbose_name='선적항구')
	portofdestination = models.CharField(max_length=100, verbose_name='도착항구')

	devliveryrequest = models.CharField(max_length=50, null=True, blank=True,
						verbose_name='기타요구사항')

	shipping_at = models.DateField(verbose_name='선적일자')
	actualshipping_at = models.DateField(verbose_name='실제선적일자',
						null=True, blank=True)
	contracted_at = models.DateField(verbose_name='계약일자')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class PurchaseContract(models.Model):
	"""docstring for SalesContract"""
	""" 설명 """
	name = models.CharField(max_length=30)
	salescontract = models.ForeignKey(SalesContract,null=True, blank=True)
	company = models.ForeignKey(Company)
	product = models.ForeignKey(Product)
	sales_amount = models.IntegerField()
	unitprice = models.FloatField()
	currency = models.CharField(max_length=1,choices=PAYMENT, default=RMB)
	packaging = models.CharField(max_length=100)

	portofdestination = models.CharField(max_length=100, verbose_name='도착항구')

	shipping_at = models.DateField(verbose_name='출발일자')
	actualshipping_at = models.DateField(verbose_name='실제출발일자',
						null=True, blank=True)

	predictdelivery_at = models.DateField(verbose_name='도착예정일자')
	actualdelivery_at = models.DateField(verbose_name='실제도착일자',
						null=True, blank=True)

	contracted_at = models.DateField(verbose_name='계약일자')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class AllProcess(models.Model):
	"""docstring for AllProcess"""
	""" 설명 """
	name = models.CharField(max_length=30)

	# 我 《== ==》 客户（GP）
	sales_contract = models.ForeignKey(SalesContract)
	sales_filename = models.CharField(verbose_name='销售合同名字', max_length=50)
	send_sales_contrat = models.BooleanField(default=False, verbose_name='传送销售合同')

	# 我 《== ==》 供应商
	make_purchase_contract = models.BooleanField(default=False, verbose_name='确认购买合同')
	purchase_filename = models.CharField(verbose_name='购买合同名字', max_length=50, null=True, blank=True)
	send_purchase_contrat = models.BooleanField(default=False)

	# 我 ==》 供应商
	send_purchase_money = models.BooleanField(default=False, verbose_name='购买付款')

	# 客户 ==》 我 ==》 供应商
	confirm_packing_marking = models.BooleanField(default=False, verbose_name='传送包装和Marking')

	# 我 ==》 物流公司
	make_commercial_invoice = models.BooleanField(default=False, verbose_name='做好 Invoice&Packing List')
	commercial_invoice_filename = models.CharField(verbose_name='Invoice 文档名字', max_length=50, null=True, blank=True)
	send_commercial_invoice = models.BooleanField(default=False, verbose_name='传送 Invoice')

	# 物流公司 ==》 我 ==》 供应商
	received_warehouse_confirm = models.BooleanField(default=False, verbose_name='从物流公司收到进仓单')
	send_warehouse_confirm_provider = models.BooleanField(default=False, verbose_name='向供应商提供进仓单')

	# 我 ==》 物流公司 
	make_material = models.BooleanField(default=False, verbose_name='准备 非危险品证明书 产品说明书 MSDS')
	not_danger_doc_filename = models.CharField(verbose_name='非危险品证明书文档', max_length=50, null=True, blank=True)
	product_explain_filename = models.CharField(verbose_name='产品说明书文档', max_length=50, null=True, blank=True)
	MSDS_filename = models.CharField(verbose_name='MSDS文档', max_length=50, null=True, blank=True)
	send_MSDS = models.BooleanField(default=False, verbose_name='传送MSDS文档')
	send_material = models.BooleanField(default=False, verbose_name='传送 非危险品证明书 产品说明书 MSDS')

	# 供应商 ==》 我 ==》 物流公司
	pallet_cbm = models.CharField(verbose_name='包装后托盘和CBM', max_length=100, null=True, blank=True)
	send_pallet_cbm = models.BooleanField(default=False, verbose_name='传送包装后托盘和CBM信息')

	# 供应商 ==》 我 ==》 客户
	picture_of_packing1 = models.FileField(verbose_name='包装后照片1', max_length=50, null=True, blank=True)
	picture_of_packing2 = models.FileField(verbose_name='包装后照片2', max_length=50, null=True, blank=True)
	picture_of_packing3 = models.FileField(verbose_name='包装后照片3', max_length=50, null=True, blank=True)
	CoA_filename = models.CharField(verbose_name='CoA', max_length=50, null=True, blank=True)
	send_pictures_CoA = models.BooleanField(default=False, verbose_name='传送照片和CoA')

	# 物流公司 ==》 我 ==》 物流公司
	send_baoguandan = models.BooleanField(default=False, verbose_name='寄过去报关单')
	send_postcode_number = models.BooleanField(default=False, verbose_name='传送顺丰的号码')
	
	# 我 ==》 供应商
	send_product_name = models.BooleanField(default=False, verbose_name='为了发票传送报关单上的产品名字')

	# 物流公司 ==》 我 ==》 客户（GP）
	received_bill_of_lading = models.BooleanField(default=False, verbose_name='从物流公司收到B/L')
	send_bill_of_lading = models.BooleanField(default=False, verbose_name='向客户提供B/L')

	# 我 ==》 客户（GP）
	make_FTF_original = models.FileField(verbose_name='原产地证明', max_length=50, null=True, blank=True)
	send_file_for_confirm = models.BooleanField(default=False, verbose_name='为了证明传送文档')
	send_result_file = models.BooleanField(default=False, verbose_name='传送证明书')

	# 我 ==》 海关
	apply_tax_refund = models.DateField(null=True, blank=True, verbose_name='申请退税')
	get_tax_refund = models.DateField(null=True, blank=True, verbose_name='退税日子')

	all_cleared  = models.BooleanField(default=False, verbose_name='项目结束')

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
