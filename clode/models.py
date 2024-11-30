from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Users(AbstractUser):
    profile_picture = models.ImageField(upload_to='media/profile_pictures/', null=True)
    trust_score = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    user_type = models.CharField(max_length=50, null=False, default='usuario')
    liter_counter = models.FloatField(default=0)

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
    
class UserPreferences(models.Model):
    user = models.OneToOneField(Users, on_delete=models.RESTRICT, related_name='user_preferences')
    prefered_free_hours = ArrayField(models.CharField(max_length=300, null=False, default=list))
    prefered_size = models.CharField(max_length=30, null=False)
    prefered_size_shoes = models.DecimalField(max_digits=2, decimal_places=1, null=False)
    prefered_colors = models.CharField(max_length=50, null=True)
    prefered_style = models.CharField(max_length=100, null=False)

    def __str__(self) -> str:
        return self.prefered_location

class Garments(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_Garments')
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

class GarmentTags(models.Model):
    garment = models.ForeignKey(Garments, on_delete=models.RESTRICT, related_name='tags')
    tag_name = models.CharField(max_length=100, null=False)

    def __str__(self) -> str:
        return self.tag_name
    
class Exchange(models.Model):
    garment_sender = models.ForeignKey(Garments, on_delete=models.CASCADE, related_name='sent_exchanges')
    garment_receiver = models.ForeignKey(Garments, on_delete=models.CASCADE, related_name='received_exchanges')
    sender_user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='sent_exchanges')
    receiver_user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='received_exchanges')
    status_choices = [
        ('Agendado', 'Agendado'),
        ('En proceso', 'En proceso'),
        ('Entregado', 'Entregado'),
        ('Imposible entregar', 'Imposible entregar'),
        ('Cancelado', 'Cancelado')
    ]
    status = models.CharField(max_length=45, choices=status_choices, default='En proceso')
    suggested_location = models.CharField(max_length=255, null=False, default="Patio Central PUCE")
    match_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Exchange between {self.sender_user.username} and {self.receiver_user.username}"
    

#Tabla para manejo de Puntajes, se utilizará en un futuro.
    
# class Scores(models.Model):
#     exchange = models.OneToOneField(Exchange, on_delete=models.CASCADE, null=False, related_name='score')
#     rater_user = models.ForeignKey(Users, on_delete=models.CASCADE, null=False, related_name='ratings_given')
#     rated_user = models.ForeignKey(Users, on_delete=models.CASCADE, null=False, related_name='ratings_received')
#     score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
#     comment = models.TextField(max_length=250, null=True)
#     rating_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self) -> str:
#         return f"Rating by {self.rater_user.username} for {self.rated_user.username}"