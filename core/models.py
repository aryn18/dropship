from distutils.command.upload import upload
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
import uuid
 
#Create your models here.
class Customer(models.Model):
  user=models.OneToOneField(User, on_delete=models.CASCADE)
  avatar=models.ImageField(upload_to='customer/avatars/', blank=True, null=True)
  phone_number = models.CharField(max_length=50, blank=True)
  stripe_customer_id = models.CharField(max_length=255, blank=True);
  stripe_payment_method_id = models.CharField(max_length=255, blank=True);
  stripe_card_last4 = models.CharField(max_length=255, blank=True);
  
  def _str_(self):
    return self.user.get_full_name ()

class Category(models.Model):
  slug = models.CharField(max_length=255, unique=True)
  name = models.CharField(max_length=255)

  def __str__(self):
      return self.name

class Job(models.Model):
  SMALL_SIZE = "small"
  MEDIUM_SIZE = "medium"
  LARGE_SZIE = "large"

  SIZES= (
    (SMALL_SIZE, 'Small'),
    (MEDIUM_SIZE, 'Medium'),
    (LARGE_SZIE, 'Large'),
  )

  CREATING_STATUS = 'creating'
  PROCESSING_STATUS = 'processing'
  PICKING_STATUS = 'picking'
  DELIVERING_STATUS = 'delivering'
  COMPLETED_STATUS = 'completed'
  CANCELED_STATUS = 'canceled'
  STATUSES = (
    (CREATING_STATUS, 'Creating'),
    (PROCESSING_STATUS, 'Processing'),
    (PICKING_STATUS, 'Picking'),
    (DELIVERING_STATUS, 'Delivering'),
    (COMPLETED_STATUS, 'Completed'),
    (CANCELED_STATUS, 'Canceled'),
  )

  #step1
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
  size = models.CharField(max_length=20, choices=SIZES, default=MEDIUM_SIZE)
  quantity = models.IntegerField(default=1)
  photo = models.ImageField(upload_to='job/photos/')
  status = models.CharField(max_length=20, choices=STATUSES, default=CREATING_STATUS)
  created_at = models.DateTimeField(default=timezone.now)
  
  #step2
  pickup_address = models.CharField(max_length=255, blank=True)
  pickup_lat = models.FloatField(default=0)
  pickup_lng = models.FloatField(default=0)
  pickup_name = models.CharField(max_length=255, blank=True)
  pickup_phone = models.CharField(max_length=50, blank=True)

  #step3
  delivery_address = models.CharField(max_length=255, blank=True)
  delivery_lat = models.FloatField(default=0)
  delivery_lng = models.FloatField(default=0)
  delivery_name = models.CharField(max_length=255, blank=True)
  delivery_phone = models.CharField(max_length=50, blank=True)

  #Step4
  duration=models.IntegerField(default=0)
  distance = models.FloatField(default=0)
  price=models.FloatField(default=0)

  # Exrea info
  pickup_photo = models.ImageField(upload_to='job/pickup_photos/',null=True,blank=True)
  pickedup_at = models.DateTimeField(null=True,blank=True)

  delivery_photo = models.ImageField(upload_to='job/delivery_photos/',null=True,blank=True)
  delivered_at = models.DateTimeField(null=True,blank=True)

  def __str__(self):
    return self.description 

class Transaction(models.Model):
  stripe_payment_intent_id=models.CharField(max_length=255,unique=True)
  job=models.ForeignKey(Job,on_delete=models.CASCADE)
  amount=models.FloatField(default=0)
  created_at=models.DateTimeField(default=timezone.now)
  
  def _str_(self):
    return self.stripe_payment_intent_id
