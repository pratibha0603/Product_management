from django.db import models

# Release model
class Release(models.Model):
    name = models.CharField(max_length=255, default="Release1")
    description = models.TextField(default="Sample release description")

    def __str__(self):
        return self.name

# Patch model
class Patch(models.Model):
    release = models.ForeignKey(Release, related_name='patches', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="Patch1")
    description = models.TextField(default="Sample patch description")

    def __str__(self):
        return self.name

# Product model
class Product(models.Model):
    patch = models.ForeignKey(Patch, related_name='products', on_delete=models.CASCADE, default=1)  # Default patch value
    name = models.CharField(max_length=255, default="Product1")
    status_choices = [
        ('deployed', 'Deployed'),
        ('under_testing', 'Under Testing'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='under_testing')

    def __str__(self):
        return self.name

# Image model
class Image(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField(default="https://example.com/image1.jpg")

    def __str__(self):
        return self.image_url
