from django.db import models

# Create your models here.
class AuditModelMixin(models.Model):

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Note(AuditModelMixin):
    title = models.CharField(max_length=129, blank=True)
    note = models.TextField(blank=True)
