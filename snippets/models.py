from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]  # get_all_lexers() returns a list of tuples
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])  # sort by language name
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())  # get_all_styles() returns a list of styles


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)  # auto_now_add=True sets the field to now when the object is first created
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)  # BooleanField is either True or False
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)  # choices=LANGUAGE_CHOICES limits the choices to the ones we defined above
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)  # choices=STYLE_CHOICES limits the choices to the ones we defined above

    class Meta:
        ordering = ['created']
