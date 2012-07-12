from django.db import models

# Create your models here.
# class Poll(models.Model):
#     question = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

# class Choice(models.Model):
#     poll = models.ForeignKey(Poll)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField()

class Kol(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    organisation = models.CharField(max_length=200)
    mobile_phone = models.CharField(max_length=50)
    office_phone = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    communication_preference = models.CharField(max_length=50)
    speciality1 = models.CharField(max_length=200)
    speciality2 = models.CharField(max_length=200)
    photo_url = models.CharField(max_length=500)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
