from django.db import models

# Here we created our models for the My SQL database. 

class Notes(models.Model):
#The First field name is pname = productname
    notes = models.CharField(max_length=2000, null=True)

#The second Field name is p_description = Product description
    audionotes = models.FileField(upload_to='documents', max_length=100, blank=True)
    
#The third field name is price = Price 
    videonotes = models.FileField(upload_to='documents', max_length=100)