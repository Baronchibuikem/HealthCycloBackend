from django.db import models
from django.utils import timezone


class RequestData(models.Model):
    prefix = models.CharField(max_length=7)
    first_name =  models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    affilation = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    street_address = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=300, null=True, blank=True)
    state = models.CharField(max_length=300, null=True, blank=True)
    zip_code = models.PositiveIntegerField()
    country = models.CharField(max_length=300)
    email = models.EmailField()
    phone_number = models.PositiveIntegerField()
    purpose = models.TextField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    description = models.TextField()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class SubmitData(models.Model):
    prefix = models.CharField(max_length=7, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    research_topic = models.CharField(max_length=100)
    research_location = models.CharField(max_length=100)
    geographical_coverage = models.CharField(max_length=100)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    study_design = models.CharField(max_length=100)
    study_population = models.PositiveIntegerField()
    sample_size = models.PositiveIntegerField(null=True, blank=True)
    sampling_technique = models.CharField(max_length=100)
    sampling_unit = models.CharField(max_length=100)
    data_collection_tools = models.CharField(max_length=100, null=True, blank=True)
    key_variables = models.CharField(max_length=100, null=True, blank=True)
    key_indicators = models.TextField()
    # For private Investigator
    name = models.CharField(max_length=100, null=True, blank=True)
    affilation = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.PositiveIntegerField()
    email = models.EmailField()
    sponsor = models.CharField(max_length=100)
    data_codebook = models.FileField(null=True, blank=True)
    questionaire = models.FileField(null=True, blank=True)
    upload_data = models.FileField(null=True, blank=True)
    permission = models.BooleanField(default=False)
    date_submitted = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Articles(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('restricted', 'Restricted'),
    )
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    content = models.TextField()
    access = models.CharField(max_length=20, choices=STATUS_CHOICES, default="open")
    images = models.ImageField(upload_to="images")
    file = models.FileField(upload_to="files")
    date_created = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title