from django.db import models

class BaseModel(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @classmethod
    def new(cls, *args, **kwargs) -> models.Model:
        "Create and save a new model instance"
        ins = cls.objects.create(*args, **kwargs)
        return ins

    def update(self, **kwargs) -> None:
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)
        self.save()