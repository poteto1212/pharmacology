from django.db import models

#講義名
class Subjects(models.Model):
    subjects=models.Charfield(verbose_name='講義名',max_length=10)
    
    def __str__(self):
        return self.subjects
        

class　Fields(models.Model):
    subject=models.ForiginKey('Subjects',on_delete=models.CASCADE)
    
    
# Create your models here.
