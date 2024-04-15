from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


# create Beep model
class Beep(models.Model):
    user = models.ForeignKey(
        User, related_name="Beeps",
        on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="Beep_like", blank=True)

    # Keep track or count of likes
    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.body}..."
        )


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Profile(models.Model):
    INVESTOR = 'Investor'
    ENTREPRENEUR = 'Entrepreneur'
    PROFILE_TYPE_CHOICES = [
        (INVESTOR, 'Investor'),
        (ENTREPRENEUR, 'Entrepreneur'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)
    Bio = models.TextField(max_length=1000, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
    Industry = models.CharField(max_length=100, null=True, blank=True)
    investment_preference = models.CharField(max_length=100, null=True, blank=True)
    profile_type = models.CharField(max_length=20, choices=PROFILE_TYPE_CHOICES, null=True, blank=True)

    date_modified = models.DateField(auto_now=True, )

    def __str__(self):
        return self.user.username


# Create Profile when new user Signs Up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()


post_save.connect(create_profile, sender=User)


class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('Contribution', 'Contribution'),
        ('Distribution', 'Distribution'),
    ]

    user = models.ManyToManyField(User, related_name='transactions')
    contract_No = models.CharField(max_length=10, null=True, blank=True)
    transaction_type = models.CharField(max_length=4000, choices=TRANSACTION_TYPE_CHOICES)
    shares = models.DecimalField(max_digits=100, decimal_places=2)
    price_per_share = models.DecimalField(max_digits=1000, decimal_places=2)
    transaction_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.ticker.symbol}"
