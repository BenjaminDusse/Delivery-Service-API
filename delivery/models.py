from django.db import models


class Status(models.Model):
    STATUS_TYPE_CHOICES = (
        ('in order', 'in order'),
        ('Confirmed', 'Confirmed'),
        ('pending', 'pending'),
        ('On the way', 'On the way'),
        ('Completed', 'Completed')
    )
    status_type = models.CharField(max_length=200, choices=STATUS_TYPE_CHOICES)

    def __str__(self):
        return self.status_type

    class Meta:
        verbose_name = 'status'
        verbose_name_plural = 'statuses'


class Branch(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=9)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'branch'
        verbose_name_plural = 'branches'


class User(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=9)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=9)
    address = models.CharField(max_length=500)
    comment = models.TextField(max_length=500, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
