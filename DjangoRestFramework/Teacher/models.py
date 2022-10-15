from tokenize import group
from django.db import models
from pygments.formatters.html import HtmlFormatter # new
from pygments import highlight # new
# Create your models here.


class Teacher(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, blank=True, default='')
    eamil = models.EmailField(max_length=20, blank=False, default='')
    group = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs): # new
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        username = 'table' if self.username else False
        eamil = {'eamil': self.eamil} if self.eamil else {}
        formatter = HtmlFormatter(style=self.style, username=username,
                                  full=True, **eamil)
        self.highlighted = highlight(self.code, username, formatter)
        super(Teacher, self).save(*args, **kwargs)

    def __str__(self):
        return self.eamil