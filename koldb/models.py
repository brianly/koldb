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
    DISEASE_AREAS = (
        (u'MM', u'MM'),
        (u'CLL', u'CLL'),
        (u'NHL', u'NHL'),
        (u'CLL/NHL', u'CLL/NHL'),
        (u'MDS', u'MDS'),
        (u'AML', u'AML'),
        (u'MDS/AML', u'MDS/AML'),
        (u'ST-Breast', u'ST-Breast'),
        (u'ST-Lung', u'ST-Lung'),
        (u'ST-Melanoma', u'ST-Melanoma'),
        (u'ST-Pancreatic', u'ST-Pancreatic'),
        (u'ST-Melanoma/Pancreatic', u'ST-Melanoma/Pancreatic'),
    )
    speciality1 = models.CharField(max_length=200, choices=DISEASE_AREAS)
    speciality2 = models.CharField(max_length=200, choices=DISEASE_AREAS)
    photo_url = models.CharField(max_length=500)
    international = models.CharField(max_length=10, blank=True, null=True)



    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
