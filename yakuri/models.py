from django.db import models

#講義名
class Subject(models.Model):
    subjects=models.CharField(verbose_name='講義名',max_length=10)
    
    def __str__(self):
        return self.subjects
    
    class Meta:
        verbose_name_plural="科目名を登録(例:薬理学序論　薬理学1 ・・・)"

#学習学年(２年・3年)
class Grade(models.Model):
    grades=models.CharField(verbose_name="学年",max_length=10)
    
    def __str__(self):
        return self.grades
    
    class Meta:
        verbose_name_plural="学習学年"
        
 #学習学期(前期・後期)
 class Season(models.Model):
    seasons=models.CharField(verbose_name="前期or後期",max_length=5)
    
    def __str__(self):
        return self.seasons
        
    class Meta:
        verbose_name_plural="前期or後期"
        
class Work(models.Model):
    works=models.CharField(verbose_name="刺激・遮断・酵素阻害等",max_length=25)
    
    def __str__(self):
        return self.works
        
    class Meta:
        verbose_name_plural="作用の仕方"
    
    
#分野
class Fields(models.Model):
    #科目名選択
    subject=models.ForeignKey('Subjects',on_delete=models.CASCADE)
    #作用分野(自律神経　中枢神経
    fields=models.CharField(verbose_name='分野名',max_length=25)
    
    def __str__(self):
        return self.fields
        
    class Meta:
        verbose_name_plural="分野名を登録"
        
        constraints=[
            ]
# Create your models here.

#詳細な情報
class Detail(models.Model):
    name=models.CharField('')

    
    
    
    
    
    
    
    
    
    
