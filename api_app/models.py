from django.db import models


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


class MSO(models.Model):
    name = models.CharField(max_length=255, null=False, unique=False)
    hq = models.ForeignKey(HQ, on_delete=models.CASCADE, default='N/A')
    territory = models.CharField(max_length=255, null=False, unique=False)
    connected_doctors = models.ManyToManyField(Doctor)
    connected_arc = models.ManyToManyField(ARC)
    connected_chemists = models.ManyToManyField(Chemist)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
