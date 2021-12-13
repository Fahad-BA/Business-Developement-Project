from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone
from django.db import models
import random, string

#Values
def ran():
    x = 'GI'+''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return x

def status():
    status = (('Just Registered.', 'Just Registered.'), ('Ready to delievry', 'Ready to delievry'),('At Warehouse','At Warehouse'), ('On its way to the customer','On its way to the customer'), ('Delivered','Delivered'), ('Canceled','Canceled'))
    return status

def City():
    City = (('R', 'Riyadh.'), ('K', 'Kharj.'), ('J','Jeddah.'), ('M','Medina.'), ('D','Dammam.'), ('Kh','Khobar.'))
    return City

def Pick():
    Pick = (('R',"Riyadhs office"), ('W', "West offices"), ("E","East Offices"), ("D","Home Delivery"))
    return Pick

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Account(AbstractBaseUser):
	email = models.EmailField(verbose_name="email", max_length=60, unique=True)
	username = models.CharField(max_length=30, unique=True)
	Address_1 = models.CharField(max_length=256)
	Address_2 = models.CharField(max_length=256)
	date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = MyAccountManager()

	def __str__(self):
		return self.username

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True

#Branches
class Office(models.Model):
    ID = models.IntegerField(primary_key=True, editable=False)
    Name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.Name)

class Bracnh(models.Model):
    ID = models.IntegerField(primary_key=True, editable=False)
    Name = models.CharField(max_length=30)
    Office = models.ForeignKey(Office, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Name)

class Warehouse(models.Model):
    ID = models.IntegerField(primary_key=True, editable=False)
    Name = models.CharField(max_length=30)
    Office = models.ForeignKey(Office, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Name)

#Packages model
class Package(models.Model):
	ID = models.IntegerField(primary_key=True, unique=True, editable=False)
	Packs = models.CharField(max_length=60)
	Description = models.TextField(editable=True, default='Description')

	def __str__(self):
		return str(self.Packs)

class Orders(models.Model):
    ID = models.IntegerField(primary_key=True, editable=False)
    Link = models.CharField(max_length=500, blank=True, editable=True)
    Quantity = models.IntegerField(default=10)
    Order_Date = models.DateTimeField(auto_now_add=True)
    City = models.CharField(max_length=50, choices=City(), default=City)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    Package = models.ForeignKey(Package, on_delete=models.CASCADE, default=1)
    Warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.ID)

class Tracking(models.Model):
    Shipment_Number = models.CharField(primary_key=True, max_length=12, editable=False, default=ran, null=False)
    Shipping_Date = models.DateTimeField(auto_now_add=True)
    Arrive_Date = models.DateTimeField(null=True, blank=True)
    Updated = models.DateTimeField(auto_now=True)
    Pickup_Location = models.CharField(max_length=50, choices=Pick(), default=Pick)
    Status = models.CharField(max_length=30, choices=status(), default=status)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    Package = models.ForeignKey(Package, on_delete=models.CASCADE, editable=True)


    def __str__(self):
        return str(self.Shipment_Number)
