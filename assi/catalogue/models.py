from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractProduct

size = {
    'small':'small',
    'medium':'medium',
    'large':'large'
}



class Product(AbstractProduct):
    video_url = models.URLField()


from oscar.apps.catalogue.models import *