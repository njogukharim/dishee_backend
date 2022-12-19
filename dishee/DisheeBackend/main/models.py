from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from PIL import Image


def getFileExtension(filename):
    return filename.split('.')[-1]

def imageUpload(image,filename):
    return f'recipe/images/{timezone.now()}.{getFileExtension(filename)}'

def videoUpload(video,filename):
    return f'recipe/videos/{timezone.now()}.{getFileExtension(filename)}'

# Id
# first name
# last name
# email
# password

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, verbose_name='Email Address')
    phone_no = models.CharField(max_length=13)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    def __str__(self) -> str:
        return f'User\'s name {self.username}'


# RECIPE MODEL
# Id
# meal name
# meal Image
# meal description
# meal video
# recipe author
# time/date created/posted
# comments.

class Recipe(models.Model):
    id = models.AutoField(null=False, primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    image = models.ImageField(upload_to=imageUpload)
    video = models.FileField(upload_to=videoUpload, max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE, null=False, blank=False, related_name="recipes")
    price = models.IntegerField(null=False, default=0)
    date_time_published = models.DateTimeField(auto_now_add=True)
    #category = models.

    def __str__(self) -> str:
        return f'{self.author.username}\'s Recipe.'
    
    def save(self, *args, **kwarg) -> None:
        super().save(*args, **kwarg)
        img = Image.open(self.image.path)
        if img.height > 400 or img.width > 400:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


# ORDERS
# Id.
# recipe name.
# user_name
# comments.
# order date

class Order(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    recipe_name = models.CharField(max_length=255,null=False,blank=False)
    order_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name="orders")
    Order_date = models.DateTimeField(auto_now_add=True)
    #recipe_owner = models.

# Id
# recipe referenced
# date_created
# body
# actiate - Boolean field.


class Comment(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    #commenter = models.g
    body = models.TextField(max_length=500, blank=False)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        order_with_respect_to = 'pub_date'

    def __str__(self) -> str:
        return f'Comment {self.id} by {self.recipe.author}'

class Category(models.Model):
    name = models.CharField(max_length=20,null=False)
    description = models.TextField(null=False, blank=False)
    