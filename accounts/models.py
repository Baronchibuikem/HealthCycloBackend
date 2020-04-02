from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password


class CustomUser(AbstractUser):
    """
    This model instance extends the Django user model instance, which means you can add
    extra fields you as suits your requirement to the User instance.

    Remember to run makemigrations and migrate for the app(app_enrollment) if you want to
    keep using this customuser against the default django user
    """
    fullname = models.CharField(max_length=100)
    username = models.CharField(unique=False, max_length=100)
    organization = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    purpose_of_data = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to="profile_pictures", null=True, blank=True)
    email = models.EmailField(unique=True)
    date_registered = models.DateField(default=timezone.now)
    terms_and_conditions = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['fullname', 'username',
                       'organization', 'designation', 'purpose_of_data', ]

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.fullname}"


class ContactUs(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    content = models.TextField()
    sent_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.email


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
