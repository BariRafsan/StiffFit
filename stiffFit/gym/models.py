from django.db import models

from django.contrib.auth.models import User
from django.utils.html import mark_safe
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Banners(models.Model):
    img = models.ImageField(upload_to="banners/")
    alt_text = models.CharField(max_length=150)

    def __str__(self):
        return self.alt_text

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))


class Notify(models.Model):
    notify_detail=models.TextField()
    read_by_user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    

    def __str__(self):
        return str(self.notify_detail)

class NotifUserStatus(models.Model):
	notif=models.ForeignKey(Notify, on_delete=models.CASCADE)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	status=models.BooleanField(default=False)

	class Meta:
		verbose_name_plural='Notification Status'