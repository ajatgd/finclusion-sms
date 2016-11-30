from __future__ import unicode_literals

from django.db import models

class UserData(models.Model):
     CatChoices = (
    ('GENERAL', "General"),
    ('OBC', "OBC"),
    ('SC', "SC"),
    ('ST', "ST")
)

     full_name = models.CharField(max_length=255)
     phone = models.CharField(max_length=10)

     employed = models.BooleanField(default=False)
     salary = models.IntegerField(max_length=10)
     category = models.CharField(max_length=9, choices=CatChoices)
     address = models.CharField(max_length=255)
     email = models.EmailField(max_length=50)
     age = models.IntegerField(max_length=2)
     aadhaar_uid = models.IntegerField(max_length=2)
     lpg_subsidy=models.BooleanField(default=False)
     ration=models.BooleanField(default=False)
     atal_pension_yojana=models.BooleanField(default=False)
     new_services=models.BooleanField(default=False)
    #  def __str__(self):
     #
    #      return ' '.join([
    #          self.full_name])
