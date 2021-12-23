from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save

import geocoder

# Create your models here.


# USUARIOS Y ACCESO
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.CharField(default='Hola, AroundMe', max_length=100)
	image = models.ImageField(default='default.jpg')

	def __str__(self):
		return f'Perfil de {self.user.username}'

	def following(self):
		user_ids = Relationship.objects.filter(from_user=self.user)\
									.values_list('to_user_id', flat=True)
		return User.objects.filter(id__in=user_ids)

	def followers(self):
		user_ids = Relationship.objects.filter(to_user=self.user)\
									.values_list('from_user_id', flat=True)
		return User.objects.filter(id__in=user_ids)


# POST Y COMENTARIOS
g = geocoder.ip('me')

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	timestamp = models.DateTimeField(default=timezone.now)
	content = models.TextField()
	latitud = models.FloatField(default=g.latlng[0])
	longitud = models.FloatField(default=g.latlng[1])

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return (self.content)


class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE) #(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=100)
    timestamp  = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment_text


#Relaciones entre Seguidores y Seguidos

class Relationship(models.Model):
	from_user = models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
	to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.from_user} to {self.to_user}'


# Crea perfil a un nuevo usuario
def createProfile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

post_save.connect(createProfile, sender=User)