from django.db import models


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class New(AbstractBaseModel):
    title = models.CharField(max_length=125)
    body = models.TextField()
    img = models.ImageField(upload_to="news/")

    def __str__(self):
        return self.title

