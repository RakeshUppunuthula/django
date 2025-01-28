from django.db import models

# Create your models here.


class review(models.Model):
    user_Name =models.CharField(max_length=100)
    review_Text=models.TextField()
    rating =models.IntegerField()

    def __str__(self):
        return self.user_Name