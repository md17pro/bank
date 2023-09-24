from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('shop:products_by_category',args=[self.slug])
    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product',blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('shop:prodCatdetail',args=[self.category.slug,self.slug])

    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        return '{}'.format(self.name)


class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
class Material(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=124)
    dob = models.DateField()
    age = models.IntegerField()
    Gender_CHOICES = (
        ('M', 'Male'), ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=Gender_CHOICES)
    phone = models.CharField(max_length=200)
    mail = models.EmailField()
    address = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    Purpose_CHOICES = (
        ('A','Enquiry'),('B','Place Order'),('C','Return'),('D','Payment Issues'),
    )
    purpose = models.CharField(max_length=1,choices=Purpose_CHOICES)
    # Material_CHOICES = (
    #     ('A','Debit Note Book'),('B','Pen'),('C','Exam Papers'),
    # )
    # materials = models.CharField(max_length=255)
    debit_notebook = models.BooleanField(default=False)
    pen = models.BooleanField(default=False)
    exam_papers = models.BooleanField(default=False)

# class Details(models.Model):
#     name = models.ForeignKey(Person,on_delete=models.SET_NULL,blank=True,null=True)
#     dob = models.DateField()
#     age = models.IntegerField()
#     Gender_CHOICES = (
#         ('M', 'Male'), ('F', 'Female'),
#     )
#     gender = models.CharField(max_length=1, choices=Gender_CHOICES)
#     phone = models.IntegerField()
#     mail = models.EmailField()
#     address = models.CharField(max_length=200, blank=True)



    def __str__(self):
        return self.name