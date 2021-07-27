from django.db import models

# Create your models here.
class Basket(models.Model):
    no = models.IntegerField(primary_key=True)
    cos_no = models.ForeignKey('Cosmetics', models.DO_NOTHING, db_column='cos_no')
    client = models.ForeignKey('Client', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'basket'


class Client(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    passwd = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'client'


class Cosmetics(models.Model):
    no = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=20)
    product = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    effect = models.CharField(max_length=30)
    ingredient = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    grade = models.FloatField(blank=True, null=True)
    gender = models.CharField(max_length=5)
    age = models.CharField(max_length=20, blank=True, null=True)
    skin_type = models.TextField()
    pro_image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cosmetics'
        

class Comment(models.Model):
    no = models.IntegerField(primary_key=True)
    cos_num = models.ForeignKey('Cosmetics', models.DO_NOTHING, db_column='cos_num')
    client_user = models.ForeignKey(Client, models.DO_NOTHING, db_column='client_user')
    content = models.TextField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comment'