from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='perfis/', default='perfis/default.jpg', blank=True)
    
    def __str__(self):
        return f"Perfil de {self.user.username}"
    
@receiver(post_save, sender=User)
def create_or_save_user_profile(sender, instance, created, **kwargs):
    if created:
        userProfile.objects.create(user=instance)
    elif hasattr(instance, 'userprofile'):
        instance.userprofile.save()
