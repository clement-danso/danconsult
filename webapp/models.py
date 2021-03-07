from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
class company(models.Model):
	name = models.CharField(max_length=50, verbose_name='Name of Company')
	date_established = models.DateField(verbose_name='Date of Establishment')
	Telephone1 = models.CharField(max_length=20, verbose_name='Primary Contact Number')
	Telephone2 = models.CharField(max_length=20, verbose_name='Secondary Contact Number', blank=True)
	Email1 = models.CharField(max_length=50, verbose_name='Primary Email', blank=True)
	Email2 = models.CharField(max_length=50,verbose_name='Secondary Email')
	Address= models.CharField(max_length=100,verbose_name='Physical Address')
	facebook_handle = models.CharField(max_length=50)
	instagram_handle = models.CharField(max_length=50)
	twitter_handle = models.CharField(max_length=50)
	linkedin_handle =models.CharField(max_length=50)
	youtube_channel = models.CharField(max_length=50)
	Logo = models.ImageField(upload_to='company/')
	Favicon = models.ImageField(upload_to='company/')
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	
	class Meta:
		verbose_name_plural = 'Company'
	
	def __str__(self):
		return self.name
		
		
class founder(models.Model):
	Name = models.CharField(max_length=50, verbose_name='Name of Founder')
	Founder_photo = models.ImageField(upload_to='founder/')
	Founder_description = models.CharField(max_length=500)
	contact_number = models.CharField(max_length=15)
	facebook_handle = models.CharField(max_length=50)
	instagram_handle = models.CharField(max_length=50)
	twitter_handle = models.CharField(max_length=50)
	linkedin_handle = models.CharField(max_length=50)
	youtube_channel = models.CharField(max_length=50)
	
	class Meta:
		verbose_name_plural = 'Founder'
	
	def __str__(self):
		return self.Name
	
class Team_members(models.Model):
	Name = models.CharField(max_length=50, verbose_name='Name of Member')
	Member_photo = models.ImageField(upload_to='Team_members/')
	Member_description = models.CharField(max_length=500)
	facebook_handle = models.CharField(max_length=50)
	instagram_handle = models.CharField(max_length=50)
	twitter_handle = models.CharField(max_length=50)
	linkedin_handle = models.CharField(max_length=50)
	youtube_channel = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural = 'Team Members'
	
	def __str__(self):
		return self.Name
		
class Partners(models.Model):
	name = models.CharField(max_length=50, verbose_name='Name of Partner')
	relationship = models.CharField(max_length=200)
	logo = models.ImageField(upload_to='Partners/')
	
	class Meta:
		verbose_name_plural = 'Partners'
	
	def __str__(self):
		return self.name
	
class careers(models.Model):
	Education = (
			 ('High School.', 'High School'),
			 ('Diploma.', 'Diploma'),
			 ("Bachelor's Degree", "Bachelor's Degree"),
			 ("Master's Degree", "Master's Degree"),
			 ("PhD", "PhD"),
			
			 )

	Position = models.CharField(max_length=50)
	Job_description = models.CharField(max_length=500)
	Required_education = models.CharField(max_length=10, choices=Education)
	Education_fields = models.CharField(max_length=100)
	Desired_qualifications = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'Careers'
	
	def __str__(self):
		return self.Position

class onlineshop(models.Model):
	name = models.CharField(max_length=50)
	
	class Meta:
		verbose_name_plural = 'Online Shops'
	
	def __str__(self):
		return self.name
		
class products(models.Model):
	name = models.CharField(max_length=50)
	product_description = models.CharField(max_length=200)
	product_picture = models.ImageField(upload_to='Products/')
	product_price = models.CharField(max_length=50)
	onlineshop = models.ForeignKey(onlineshop, null=True, on_delete=models.SET_NULL)
	product_url = models.CharField(max_length=50)
	
	class Meta:
		verbose_name_plural = 'Products'
	
	def __str__(self):
		return self.name
	
class services(models.Model):
	name = models.CharField(max_length=50)
	service_description = models.CharField(max_length=200)
	service_icon = models.ImageField(upload_to='Services/')
	
	class Meta:
		verbose_name_plural = 'Services'
	
	def __str__(self):
		return self.name

class features(models.Model):
	name = models.CharField(max_length=50)
	feature_icon = models.ImageField(upload_to='Features/')
	feature_description = models.CharField(max_length=200)
	
	class Meta:
		verbose_name_plural = 'Features'
	
	def __str__(self):
		return self.name
	
class testimomials(models.Model):
	client_name = models.CharField(max_length=50)
	review_comment = models.CharField(max_length=200)
	
	class Meta:
		verbose_name_plural = 'Testimonials'
	
	def __str__(self):
		return self.client_name
	
class quoterequest(models.Model):
	sender_email = models.CharField(max_length=50)
	sender_name = models.CharField(max_length=50)
	service_request = models.CharField(max_length=200)
	urgency = models.CharField(max_length=200)
	due_date = models.DateField()
	project_description = models.CharField(max_length=200)
	
	class Meta:
		verbose_name_plural = 'Quote Requests'
	
	def __str__(self):
		return self.sender_name
