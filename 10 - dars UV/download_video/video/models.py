from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.


class Video(models.Model):
    name = models.CharField(max_length=50)
    video = models.FileField(upload_to='videos/', validators=[
        FileExtensionValidator(allowed_extensions=['MP4', 'ASF', 'FLV', 'MKV', 'MOV'])
    ])
    description = models.TextField(null=True, blank=True, help_text='Video haqida qisqacha')

    def __str__(self):
        return self.name
