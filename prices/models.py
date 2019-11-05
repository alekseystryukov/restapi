from django.db import models
from mongoengine import Document, EmbeddedDocument, fields


class Price(models.Model):
    name = models.CharField(max_length=200, default="")
    value = models.FloatField()


class MDPrice(Document):
    name = fields.StringField(default="")
    value = fields.FloatField()
