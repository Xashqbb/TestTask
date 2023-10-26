from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username
