from django.db import models


class Categoriya(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    frist_name = models.ForeignKey(Categoriya, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product_info(models.Model):
    last_name = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    number = models.IntegerField()
    price = models.IntegerField()
    datatime = models.DateTimeField()

    def __str__(self):
        return self.name
