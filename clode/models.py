from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date, datetime
# Create your models here.

class USERS(AbstractUser):
    location = models.CharField(max_length=150, null=False)
    profile_picture = models.ImageField(upload_to='media/profile_pictures/', null=True)
    trust_score = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    user_type = models.CharField(max_length=50, null=False, default='usuario')

    def __str__(self) -> str:
        return self.username
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
    )
    
class USER_PREFERENCES(models.Model):
    user = models.OneToOneField(USERS, on_delete=models.RESTRICT, related_name='user_preferences')
    prefered_free_hours = models.CharField(max_length=80, null=False)
    prefered_location = models.CharField(max_length=150, null=False)
    prefered_size = models.CharField(max_length=30, null=False)
    prefered_size_shoes = models.DecimalField(max_digits=2, decimal_places=1, null=False)
    prefered_colors = models.CharField(max_length=50, null=True)
    prefered_style = models.CharField(max_length=100, null=False)

    def __str__(self) -> str:
        return self.prefered_location

class GARMENTS(models.Model):
    user = models.ForeignKey(USERS, on_delete=models.CASCADE, related_name='user_garments')
    title = models.CharField(max_length=80, null=False)
    garment_image = models.ImageField(upload_to='media/garment_images', null=False)
    description = models.CharField(max_length=350, null=False)
    size = models.CharField(max_length=30, null=False)
    condition = models.CharField(max_length=100, null=False)
    brand = models.CharField(max_length=120, null=False)
    category = models.CharField(max_length=80, null=False)
    upload_date = models.DateField(null=False, auto_now_add=True)
    is_available = models.SmallIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(1)])

    def __str__(self) -> str:
        return self.title

class GARMENT_TAGS(models.Model):
    garment = models.ForeignKey(GARMENTS, on_delete=models.RESTRICT, related_name='tags')
    tag_name = models.CharField(max_length=100, null=False)

    def __str__(self) -> str:
        return self.tag_name
    
class EXCHANGE(models.Model):
    garment_sender = models.ForeignKey(GARMENTS, on_delete=models.CASCADE, related_name='sent_exchanges')
    garment_receiver = models.ForeignKey(GARMENTS, on_delete=models.CASCADE, related_name='received_exchanges')
    sender_user = models.ForeignKey(USERS, on_delete=models.CASCADE, related_name='sent_exchanges')
    receiver_user = models.ForeignKey(USERS, on_delete=models.CASCADE, related_name='received_exchanges')
    status = models.CharField(max_length=45)
    suggested_location = models.CharField(max_length=255, null=False)
    match_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Exchange between {self.sender_user.username} and {self.receiver_user.username}"
    
class SCORES(models.Model):
    exchange = models.OneToOneField(EXCHANGE, on_delete=models.CASCADE, null=False, related_name='score')
    rater_user = models.ForeignKey(USERS, on_delete=models.CASCADE, null=False, related_name='ratings_given')
    rated_user = models.ForeignKey(USERS, on_delete=models.CASCADE, null=False, related_name='ratings_received')
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(max_length=250, null=True)
    rating_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Rating by {self.rater_user.username} for {self.rated_user.username}"