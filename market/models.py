# # models.py in the marketplace app

# from django.db import models
# from django.contrib.auth.models import User
# from ConsumerProfile.models import ConsumerApp

# class ModelProject(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     developer = models.ForeignKey(User, on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     subscribers = models.ManyToManyField(Consumer, blank=True)
#     usage_statistics = models.JSONField(default=dict)

#     def __str__(self):
#         return self.name
