import uuid
from django.db import models
from django.utils import timezone

class User(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    created_at = models.DateTimeField(editable=True)
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.created_at = timezone.now()
        return super(User, self).save(force_insert=False, force_update=False, using=None,
                                      update_fields=None)
    class Meta:
        managed = True
        db_table = 'users'