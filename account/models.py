from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, UserManager

from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from datetime import timedelta

class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        """Create and return a regular user with the given phone and password."""
        if not phone:
            raise ValueError("The Phone field must be set")
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        """Create and return a superuser with the given phone and password."""
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_admin") is not True:
            raise ValueError("Superuser must have is_admin=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(phone, password, **extra_fields)





class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="آدرس ایمیل",
        max_length=255,
        null=True,
        blank=True,
        unique=True,
    )
    fullname = models.CharField(max_length=50, verbose_name="نام کامل")
    phone = models.CharField(max_length=12, unique=True, verbose_name="شماره تلفن")
    is_admin = models.BooleanField(default=False, verbose_name="ادمین")

    objects = CustomUserManager()  # Use the custom manager

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return self.fullname

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin


class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.fullname} - {self.ip_address}"




class Otp(models.Model):
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=15)
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)  # Set default to current time

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=5)  # OTP expires in 5 minutes










class NewsMessage(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    date = models.DateField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    body = models.TextField(verbose_name="متن پیام")
    detail_link = models.URLField(blank=True, null=True, verbose_name="لینک جزئیات")

    class Meta:
        verbose_name = "پیام خبری"
        verbose_name_plural = "پیام‌های خبری"

    def __str__(self):
        return self.title



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')
    first_name = models.CharField(max_length=100, verbose_name='نام')
    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='شماره تلفن')
    gender = models.CharField(max_length=10, choices=[('male', 'مرد'), ('female', 'زن')], null=True, blank=True, verbose_name='جنسیت')
    about_me = models.TextField(null=True, blank=True, verbose_name='درباره من')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True, verbose_name='عکس پروفایل')

    def __str__(self):
        return f"{self.user.fullname}'s Profile"


    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل ها'