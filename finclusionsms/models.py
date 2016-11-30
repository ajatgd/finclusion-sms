from django.db import models


class User(models.Model):
     CatChoices = (
    (General, "General"),
    (OBC, "OBC"),
    (SC, "SC"),
    (ST, "ST")
)
    notChoices = (
    (LPG, "LPG Schemes"),
    (Ration, "Ration Schemes"),
    (apy, "Atal Pension Yojana"),
    (new_yojanas, "New Yojanas")
)
    full_name = models.CharField(max_length=255)
    phone = models.IntegerField(max_length=12)
    salary = models.IntegerField(max_length=10)
    category = models.CharField(max_length=9, choices=CatChoices)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    age = models.IntegerField(max_length=2)
    aadhaaruid = models.IntegerField(max_length=2)
    notifications = models.CharField(max_length=20, choices=notChoices)
    
    def __str__(self):

        return ' '.join([
            self.first_name,
