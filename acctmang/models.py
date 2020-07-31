from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.utils.timezone import now
import datetime
from decimal import Decimal
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Valid email should be provided")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Valid email should be provided")
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_superuser'] = True
        extra_fields['is_staff'] = True

        wallet_id = self.normalize_email(email)

        if extra_fields.get('is_superuser') and extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must have is_superuser and is_staff=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    account_number = models.CharField(max_length=10, blank=True)
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )
    date_joined = models.DateTimeField(
        _('date joined'), default=datetime.datetime.now)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField(_('active'), default=True)
    last_visit = models.DateTimeField(default=datetime.datetime.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def email_user(self):
        return self.email

    def account_no(self):
        return self.account_no

    def __str__(self):
        return self.email


PROFILE_TYPE = (
    ('01', 'INIDIVDUAL'),
    ('02', 'BUSINESS')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=30, blank=True)
    full_name = models.CharField(max_length=50, blank=True)
    account_type = models.CharField(
        max_length=10, choices=PROFILE_TYPE, default="01")

    def __str__(self):
        return str(self.user)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_in_view = kwargs['instance']
        user_profile = Profile.objects.create(user=user_in_view)
        # update User account number
        user_in_view.account_number = "PTS" + str(user_in_view.id).zfill(4)
        user_in_view.save(update_fields=["account_number", ])


post_save.connect(create_profile, sender=User)


class UserEarnings(models.Model):
    class Meta:
        verbose_name = "User Earnings"
        verbose_name_plural = "User Earnings"

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    transaction_ref = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)
    amount_earned = models.DecimalField(
        _('Amount Earned'),
        default=0,
        max_digits=12,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal('0.00')),
        ])

    def __str__(self):
        return "{}: {}".format(self.user.email, self.transaction_ref)


def create_transaction_record(sender, **kwargs):
    if kwargs['created']:
        user_transaction = UserTransactionRecord.objects.create(
            user=kwargs['instance'].user,
            transaction_type="CR",
            amount=kwargs['instance'].amount_earned
        )

        # Update User Balance
        user = kwargs['instance'].user
        user.balance = user.balance + kwargs['instance'].amount_earned

        user.save(update_fields=["balance"])


post_save.connect(create_transaction_record, sender=UserEarnings)


TRANSACTION_TYPE = (
    ("CR", "CREDIT"),
    ("DR", "DEBIT")
)


class UserTransactionRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    transaction_type = models.CharField(max_length=2, choices=TRANSACTION_TYPE)
    amount = models.CharField(max_length=10)
    datetime = models.DateTimeField(auto_now_add=True)
    metadata = models.CharField(max_length=100, blank=True, null=True)
