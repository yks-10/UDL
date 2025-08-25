import secrets

from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.timezone import now

from common.constants import *

from django.utils import timezone
from datetime import timedelta, date
import uuid
import random
from django.core.exceptions import ValidationError


class User(AbstractUser):
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=255, unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True, default='')
    user_type = models.CharField(max_length=255, choices=USER_CHOICES, default=CONSUMER, blank=False, null=False)
    image = models.ManyToManyField('File', related_name='user', blank=True)
    address = models.TextField(blank=True, null=True)
    address_line = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.PositiveIntegerField(default=0,blank=True, null=True)
    verified = models.BooleanField(default=False)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=ACTIVE)


    is_available = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_agree = models.BooleanField(null=True, default=None)
    unique_id = models.CharField(max_length=255, unique=True, blank=True, null=True)


    last_active_time = models.DateTimeField(null=True, blank=True, default=now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'self', on_delete=models.SET_NULL, related_name="user_created_by",
        null=True, blank=True
    )
    updated_by = models.ForeignKey(
        'self', on_delete=models.SET_NULL, related_name="user_updated_by",
        null=True, blank=True
    )
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",
        blank=True
    )



    def save(self, *args, **kwargs):
        if not self.unique_id  and self.first_name and self.last_name and self.phone_number:
            fn = (self.first_name[:3] if self.first_name else "XXX").upper()
            ln = (self.last_name[:3] if self.last_name else "XXX").upper()
            phn = self.phone_number[-4:] if len(self.phone_number) >= 4 else "XXXX"
            rand = uuid.uuid4().hex[:4].upper()
            self.unique_id = f"{fn}{ln}{phn}-{rand}"
        super().save(*args, **kwargs)

    class Meta:
        db_table = "user"
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created_at']



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="%(class)s_created_by", null=True, blank=True
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="%(class)s_updated_by", null=True, blank=True
    )
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

class File(BaseModel):
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=500)
    content_type = models.CharField(max_length=255, blank=True, null=True)
    access_control = models.CharField(max_length=255, blank=False, null=False, default='public-read')
    module = models.CharField(max_length=255, blank=False, null=False, choices=FILE_MODULES, default=AGENT)

    class Meta:
        db_table = "file"
        verbose_name = 'File'
        verbose_name_plural = 'Files'
        ordering = ['-pk']

    def get_url(self):
        if self.access_control == 'public-read':
            return f'{EnvironmentVariable.AWS_S3_BASE_URL}{self.file_path}'
        return FileUtils.get_signed_url(self.file_path)

    def __str__(self):
        return f'{self.module}: {self.file_name}'



class Blocklist(models.Model):
    token = models.CharField(max_length=500, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token



class PasswordResetRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=255)  # 6-digit unique code
    token = models.CharField(max_length=255)  # Unique token for resetting password
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    @staticmethod
    def generate_reset_code():
        """Generate a 6-digit unique code."""
        return f"{secrets.randbelow(900000) + 100000}"

    @staticmethod
    def create_reset_request(user):
        """Creates or updates a password reset request for the user."""
        raw_reset_code = PasswordResetRequest.generate_reset_code()  # Generate plain reset code
        hashed_reset_code = make_password(raw_reset_code)  # Hash before saving
        token = str(uuid.uuid4())
        expiration_time = timezone.now() + timedelta(minutes=10)  # Valid for 10 minutes

        # Update or create a reset request
        reset_request, created = PasswordResetRequest.objects.update_or_create(
            user=user,
            defaults={
                "reset_code": hashed_reset_code,  # Store hashed code
                "token": token,
                "expires_at": expiration_time
            }
        )

        return reset_request, raw_reset_code

    def verify_reset_code(self, input_code):
        """Verify if the provided reset code matches the stored hashed reset code."""
        return check_password(input_code, self.reset_code)

