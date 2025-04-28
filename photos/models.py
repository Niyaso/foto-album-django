from django.db import models
from django.contrib.auth.models import User

# Define your models here.

class Category(models.Model):
    """
    Model representing a category for grouping photos.
    
    Attributes:
        user (ForeignKey): References the User who created the category. Can be null or blank.
        name (CharField): The name of the category. Cannot be null or blank.
    """

    class Meta:
        verbose_name = 'Category'                # Human-readable singular name
        verbose_name_plural = 'Categories'       # Human-readable plural name

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        """
        String representation of the Category model, returns the name of the category.
        """
        return self.name


class Photo(models.Model):
    """
    Model representing a photo uploaded by a user.
    
    Attributes:
        category (ForeignKey): References a Category. Can be null or blank.
        image (ImageField): The image file itself. Required field.
        description (TextField): A text description of the photo.
    """

    class Meta:
        verbose_name = 'Photo'                  # Human-readable singular name
        verbose_name_plural = 'Photos'          # Human-readable plural name

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        """
        String representation of the Photo model, returns the description of the photo.
        """
        return self.description
