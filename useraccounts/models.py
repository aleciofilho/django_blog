from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pictures', default='avatar.jfif')

    def __str__(self):
        return f"{self.user.username} profile"

    def save(self):
        super().save()

        img = Image.open(self.profile_pic.path)
        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

        # if img.height > 300 and img.width <= 300:
        #     output_size = (300, img.width)
        # elif img.height <= 300 and img.width > 300:
        #     output_size = (img.height, 300)
        # elif img.height > 300 and img.width > 300:
        #     output_size = (300, 300)


        # output_size = (min(img.height, 300), min(img.width, 300))
        # img.thumbnail(output_size)
        # img.save(self.profile_pic.path)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()