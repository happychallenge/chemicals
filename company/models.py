# company/models.py
import csv
from django.db import models

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
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.en_name

	# def get_absolute_url(self):
	# 	return reverse('company:post_detail', args=[self.id])


class CompanyProduct(models.Model):
	"""docstring for CompanyProduct"""
	""" 설명 """
	USD = 'D'
	RMB = 'R'
	CATEGORY = (
		(USD, 'US$'),
		(RMB, 'RMB'),
	)
	company = models.ForeignKey(Company)
	product = models.ForeignKey(Product)
	currency = models.CharField(max_length=1,choices=CATEGORY, default=RMB)
	price = models.FloatField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{} {}'.format(self.company, self.product)


	# def get_absolute_url(self):
	# 	return reverse('myapp:post_detail', args=[self.id])