from django.db import models


class MyOtherModel(models.Model):
    number = models.IntegerField


class MyNullableOtherModel(models.Model):
    number = models.IntegerField


class MyModel(models.Model):
    name = models.CharField(max_length=30)
    other_model = models.ForeignKey(MyOtherModel, on_delete=models.CASCADE)
    nullable_other = models.ForeignKey(MyNullableOtherModel, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(blank=True)
