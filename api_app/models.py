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
    name = models.CharField(max_length=255, null=False, unique=False, name="Name")
    degree = models.CharField(max_length=255, null=False, unique=False, name="Degree")
    type = models.CharField(max_length=255, null=False, unique=False, choices=[
        ('P', 'Prescriber'),
        ('D', 'Dispenser'),
        ('B', 'Both'),
    ], name="Type"
                              )
    support_category = models.CharField(max_length=255, null=False, unique=False, choices=[
        ('A+', 'A+'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    ], name="Support Category")

    class Meta:
        ordering = ['Name']

    def __str__(self):
        return self.name


class ARC(models.Model):
    name = models.CharField(max_length=255, null=False, unique=False, name="Retailer Name")
    person_in_charge = models.CharField(max_length=255, null=False, unique=False, name="Person in Charge")
    business_type = models.CharField(max_length=255, null=False, unique=False, choices=[
        ('RETAIL', 'Retail'),
        ('WHOLESALE', 'Wholesale'),
        ('BOTH', 'Both'),
    ], name="Business Type")
    sitting_doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, name="Select Sitting Doctor")
    products_under_support = models.ManyToManyField(Product, name='Products Under Support')

    class Meta:
        ordering = ['Retailer Name']

    def __str__(self):
        return self.name


class Chemist(models.Model):
    name = models.CharField(max_length=255, null=False, unique=False, name="Chemist Name")
    person_in_charge = models.CharField(max_length=255, null=False, unique=False, name="Person in Charge")
    business_type = models.CharField(max_length=255, null=False, unique=False, choices=[
        ('RETAIL', 'Retail'),
        ('WHOLESALE', 'Wholesale'),
        ('BOTH', 'Both'),
    ], name="Business Type")
    sitting_doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, name="Select Sitting Doctor")
    products_under_support = models.ManyToManyField(Product, name='Products Under Support')

    class Meta:
        ordering = ['Chemist Name']

    def __str__(self):
        return self.name


class MSO(models.Model):
    name = models.CharField(max_length=255, null=False, unique=False, name="Name")
    hq = models.ForeignKey(HQ, on_delete=models.CASCADE, name="HQ", default='N/A')
    territory = models.CharField(max_length=255, null=False, unique=False, name="Territory")
    connected_doctors = models.ManyToManyField(Doctor, name="Connected Doctors")
    connected_arc = models.ManyToManyField(ARC, name="Connected ARCs")
    connected_chemists = models.ManyToManyField(Chemist, name="Connected Chemists")

    class Meta:
        ordering = ['Name']

    def __str__(self):
        return self.name
