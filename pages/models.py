from django.db import models
from precise_bbcode.fields import BBCodeTextField


class Homepage(models.Model):
    """
    This model stores the readable text on the home page. I've made this into a model so a non-technical person can
    change what is written on the front page through Django admin.
    """
    text = models.TextField()

    def __str__(self):
        return "Homepage"
