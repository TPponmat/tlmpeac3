from django.db import models

class transformer(models.Model):

    pub_date = models.DateTimeField('date published',null=True, blank=True)
    pub_time = models.TimeField('time published',null=True, blank=True)
    deviceid = models.CharField(max_length=200,default='pv01',)
    tempindoor = models.FloatField(default=0,null=True, blank=True)
    tempoutdoor = models.FloatField(default=0,null=True, blank=True)
    powera = models.FloatField(default=0,null=True, blank=True)
    powerb = models.FloatField(default=0,null=True, blank=True)
    powerc = models.FloatField(default=0,null=True, blank=True)
    powertot = models.FloatField(default=0,null=True, blank=True)
    reactivepowera = models.FloatField(default=0,null=True, blank=True)
    reactivepowerb = models.FloatField(default=0,null=True, blank=True)
    reactivepowerc = models.FloatField(default=0,null=True, blank=True)
    reactivepowertot = models.FloatField(default=0,null=True, blank=True)
    currenta = models.FloatField(default=0,null=True, blank=True)
    currentb = models.FloatField(default=0,null=True, blank=True)
    currentc = models.FloatField(default=0,null=True, blank=True)
    currenttot = models.FloatField(default=0,null=True, blank=True)
    voltagea = models.FloatField(default=0,null=True, blank=True)
    voltageb = models.FloatField(default=0,null=True, blank=True)
    voltagec = models.FloatField(default=0,null=True, blank=True)
    voltagetot = models.FloatField(default=0,null=True, blank=True)
    kwha = models.FloatField(default=0,null=True, blank=True)
    kwhb = models.FloatField(default=0,null=True, blank=True)
    kwhc = models.FloatField(default=0,null=True, blank=True)
    kwhtot = models.FloatField(default=0,null=True, blank=True)

class transformer2(models.Model):

    pub_date = models.DateTimeField('date published',null=True, blank=True)
    pub_time = models.TimeField('time published',null=True, blank=True)
    deviceid = models.CharField(max_length=200,default='pv01',)
    grid = models.FloatField(default=0,null=True, blank=True)
    load = models.FloatField(default=0,null=True, blank=True)
    solar = models.FloatField(default=0,null=True, blank=True)
    
