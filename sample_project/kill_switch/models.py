from django.db import models
import uuid
from .constants import RULE_STATUS, ACTIVE


def new_uuid():
    key = uuid.uuid4()
    return str(key)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(max_length=255, unique=True, default=new_uuid)

    class Meta:
        abstract = True


class Rule(BaseModel):
    identifier = models.CharField(max_length=255)
    conditions = models.TextField()
    from_date = models.DateTimeField(null=True, blank=True)
    to_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(choices=RULE_STATUS, default=ACTIVE, max_length=100)

    class Meta:
        db_table = "Rule"
        verbose_name_plural = "Rules"

    def __str__(self):
        return self.identifier

