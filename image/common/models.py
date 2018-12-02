from django.db import models


class BaseModelManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_deleted = models.BooleanField(default=False, db_index=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    objects = BaseModelManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True
        ordering = ['-create_time']

    def reload(self):
        self.refresh_from_db()

    def mark_delete(self):
        self.is_deleted = True
        self.save(update_fields=['is_deleted'])

    def restore(self):
        self.is_deleted = False
        self.save(update_fields=['is_deleted'])

    @property
    def id_str(self):
        return str(self.id)
