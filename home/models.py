from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.

class Picture(models.Model):

    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images',max_length=255)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    

    class Meta:
        ordering=['title']
        verbose_name ="picture"
        verbose_name_plural = "pictures"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("picture_detail", kwargs={"pk": self.pk})
