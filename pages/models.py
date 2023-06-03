from django.db import models
from django.utils.translation import gettext as _


class Homepage(models.Model):
    """
    This model stores the readable text on the home page. I've made this into a model so a non-technical person can
    change what is written on the front page through Django admin.
    """
    text = models.TextField()
    text_et = models.TextField("Estonian text", default="")

    def __str__(self):
        return _("Homepage")
