from django.db import models

class Collec(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    data = models.DateField(auto_now_add=True)
    date = models.DateField(null=False)

    def __str__(self):
        return self.title