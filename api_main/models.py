from django.db import models
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User as authUser


# Create your models here.

class HQ(models.Model):
    name = models.CharField(max_length=255, null=False)
    pincode = models.CharField(max_length=10, null=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, null=False, unique=False)
    size = models.CharField(max_length=255, null=False, unique=False)
    price = models.FloatField(null=True)
    # capsule / oil / syrup / tablet
    type = models.CharField(max_length=255, null=False, unique=False, choices=[('CAPSULE', 'Capsule'),
                                                                               ('OIL', 'Oil'),
                                                                               ('SYRUP', 'Syrup'),
                                                                               ('TABLET', 'Tablet')
                                                                               ])

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} - {self.size} - {self.type}'


class Sample(models.Model):
    name = models.CharField(max_length=255, null=False, unique=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class POP(models.Model):
    name = models.CharField(max_length=255, null=False, unique=False)


class Doctor(models.Model):
    name = models.CharField(max_length=255, null=False, unique=False)
    degree = models.CharField(max_length=255, null=False, unique=False)
    type = models.CharField(max_length=255, null=False, unique=False, choices=[
        ('P', 'Prescriber'),
        ('D', 'Dispenser'),
        ('B', 'Both'),
    ]
                            )
    support_category = models.CharField(max_length=255, null=False, unique=False, choices=[
        ('A+', 'A+'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    ])

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class ARC(models.Model):
    name = models.CharField(max_length=255, null=False, unique=False)
    person_in_charge = models.CharField(max_length=255, null=False, unique=False)
    business_type = models.CharField(max_length=255, null=False, unique=False, choices=[
        ('RETAIL', 'Retail'),
        ('WHOLESALE', 'Wholesale'),
        ('BOTH', 'Both'),
    ])
    sitting_doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    products_under_support = models.ManyToManyField(Product)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Chemist(models.Model):
    name = models.CharField(max_length=255, null=False, unique=False)
    person_in_charge = models.CharField(max_length=255, null=False, unique=False)
    business_type = models.CharField(max_length=255, null=False, unique=False, choices=[
        ('RETAIL', 'Retail'),
        ('WHOLESALE', 'Wholesale'),
        ('BOTH', 'Both'),
    ])
    sitting_doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    products_under_support = models.ManyToManyField(Product)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Stockist(models.Model):
    name = models.CharField(max_length=255, null=False, unique=False)
    mobile = models.CharField(max_length=255, null=False, unique=False)
    gstin = models.CharField(max_length=255, null=False, unique=False)
    address = models.TextField(null=False, unique=False)
    person_in_charge = models.CharField(max_length=255, null=False, unique=False)
    stockist_type = models.CharField(max_length=255, null=False, unique=False, choices=[
        ('ALLOPATH', 'Allopath'),
        ('ABSOLUTE_AYURVEDA', 'Absolute Ayurveda'),
        ('GENERALS', 'Generals'),
    ])
    business_type = models.CharField(max_length=255, null=False, unique=False, choices=[
        ('RETAIL', 'Retail'),
        ('WHOLESALE', 'Wholesale'),
        ('BOTH', 'Both'),
    ])

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.business_type} - {self.name}'


class MSO(models.Model):
    name = models.CharField(max_length=255, null=False, unique=False)
    hq = models.ForeignKey(HQ, on_delete=models.CASCADE, default='N/A')
    territory = models.CharField(max_length=255, null=False, unique=False)
    connected_doctors = models.ManyToManyField(Doctor)
    connected_arc = models.ManyToManyField(ARC)
    connected_chemists = models.ManyToManyField(Chemist)
    connected_stockists = models.ManyToManyField(Stockist)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class User(models.Model):
    user = models.ForeignKey(authUser, on_delete=models.CASCADE)
    mso = models.ForeignKey(MSO, on_delete=models.CASCADE, null=True)


class SBLR(models.Model):
    """
       EXAMPLE:
       {
       'mso': mso_id,
       'date': "YYYY-MM-DD",
       'data': {
           'current_day_doctors': [
               {
                   id1: {
                       'samples': [sample_id1, sample_id2, sample_id3....] (product_id),
                       'POP' : [pop_id1, pop_id2, pop_id3.....] (pop_model),
                       'booking' {
                           prod_id1: qty,
                           prod_id2: qty,
                           prod_id3: qty,
                           prod_id4: qty,
                       },
                   },
               },
               {
                   id2: {
                       'samples': [sample_id1, sample_id2, sample_id3....] (product_id),
                       'POP' : [pop_id1, pop_id2, pop_id3.....] (pop_model),
                       'booking' {
                           prod_id1: qty,
                           prod_id2: qty,
                           prod_id3: qty,
                           prod_id4: qty,
                       },
                   }
               },
           ]


           'current_day_arcs': [
               {
                   id1: {
                       'samples': [sample_id1, sample_id2, sample_id3....] (product_id),
                       'POP' : [pop_id1, pop_id2, pop_id3.....] (pop_model),
                       'booking' {
                           prod_id1: qty,
                           prod_id2: qty,
                           prod_id3: qty,
                           prod_id4: qty,
                       },
                   },
               },
               {
                   id2: {
                       'samples': [sample_id1, sample_id2, sample_id3....] (product_id),
                       'POP' : [pop_id1, pop_id2, pop_id3.....] (pop_model),
                       'booking' {
                           prod_id1: qty,
                           prod_id2: qty,
                           prod_id3: qty,
                           prod_id4: qty,
                       },
                   }
               },
           ]


           'current_day_chemists': [
               {
                   id1: {
                       'samples': [sample_id1, sample_id2, sample_id3....] (product_id),
                       'POP' : [pop_id1, pop_id2, pop_id3.....] (pop_model),
                       'booking' {
                           prod_id1: qty,
                           prod_id2: qty,
                           prod_id3: qty,
                           prod_id4: qty,
                       },
                   },
               },
               {
                   id2: {
                       'samples': [sample_id1, sample_id2, sample_id3....] (product_id),
                       'POP' : [pop_id1, pop_id2, pop_id3.....] (pop_model),
                       'booking' {
                           prod_id1: qty,
                           prod_id2: qty,
                           prod_id3: qty,
                           prod_id4: qty,
                       },
                   }
               },
           ]

       }
    }
       """
    mso = models.ForeignKey(MSO, on_delete=models.CASCADE, default='N/A')
    data = models.JSONField()
    date = models.DateField()

    class Meta:
        ordering = ['mso']

    def __str__(self):
        return self.mso.name, self.date
