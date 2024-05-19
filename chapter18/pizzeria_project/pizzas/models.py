from django.db import models


class Pizza(models.Model):
    """A menu for Pizza"""
    name = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of a model"""
        return self.name


class Topping(models.Model):
    """List of topping to be added on a pizza"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        """Represent a simple string representing the topping."""
        return self.name
