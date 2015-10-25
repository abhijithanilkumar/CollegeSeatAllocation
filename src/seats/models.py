from django.db import models

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
	
    def __unicode__(self):
        return self.name

class Branch(models.Model):
    college = models.ForeignKey(College)
    name = models.CharField(max_length=100)
    seats = models.IntegerField(default=0)
	
    def __unicode__(self):
        return "%s %s" % (self.college.name, self.name)

