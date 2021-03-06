from django.conf import settings
from django.db import models

class Site(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(default=None)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField(default=None)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    def __str__(self):
        return str(self.site)+'_'+str(self.created_at)

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.item)+'_'+str(self.post)