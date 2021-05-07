from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#講義名
class Subject(models.Model):
    subjects=models.CharField(verbose_name='講義名',max_length=10,unique=True)
    subinfo=models.TextField(verbose_name="講義内容の紹介",null=True,blank=True)
    
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
    worknum=models.IntegerField(
        verbose_name="作用分類の順序",
        default=1,
        blank=True,
        null=True,
        unique=False,
        validators=[MinValueValidator(1),MaxValueValidator(15)]
    )
    
    def __str__(self):
        return self.works
        
    class Meta:
        verbose_name_plural="作用の仕方"
    
    
#分野
class Fields(models.Model):
    #科目名選択
    subject=models.ForeignKey('Subject',verbose_name="科目選択",on_delete=models.CASCADE)
    #作用分野(自律神経　中枢神経
    fields=models.CharField(verbose_name='分野名(科目)　例：中枢神経(薬理Ⅰ)　',max_length=25,unique=True,)
    descriptione=models.TextField(verbose_name="分野の紹介",blank=True,null=True)
    reltarget=models.ManyToManyField('Target',verbose_name='関連薬の主な作用点',blank=True,null=True)
    fieldsnum=models.IntegerField(
        verbose_name="目次順番",
        default=1,
        blank=True,
        null=True,
        unique=False,
        validators=[MinValueValidator(1), MaxValueValidator(35)]
        )
    
            
    def __str__(self):
        return self.fields
        
    class Meta:
        verbose_name_plural="分野名登録"
        
        constraints=[
            models.UniqueConstraint(
                fields=['subject','fields'],
                name="subjects_fields_unique"
                )
            ]
        
# Create your models here.

class Target(models.Model):
    targets=models.CharField(verbose_name="作用点",max_length=35,unique=True)
    phsiologic=models.TextField(verbose_name="受容体の生理機能",blank=True,null=True)
    targetsnum=models.IntegerField(
        verbose_name="作用点表示順",
        default=1,
        blank=True,
        null=True,
        unique=False,
        validators=[MinValueValidator(1), MaxValueValidator(35)]
        )
    
    
    
    
    def __str__(self):
        return self.targets
    
    class Meta:
        verbose_name_plural="作用標的部位"

#詳細な情報
class Detail(models.Model):
    field=models.ForeignKey('Fields',verbose_name="分野(科目)選択",on_delete=models.CASCADE)
    name=models.CharField(verbose_name="薬物名",max_length=25)
    target=models.ManyToManyField('Target',verbose_name="標的受容体・標的タンパク")
    detail=models.TextField(verbose_name="特徴・説明",blank=True,null=True)
    work=models.ForeignKey('Work',verbose_name="作用の仕方",on_delete=models.CASCADE)
    grade=models.ForeignKey('Grade',verbose_name="学年",on_delete=models.CASCADE)
    season=models.ForeignKey('Season',verbose_name="学期",on_delete=models.CASCADE)
    
    #構造式の投稿(imageファイルへのアップロード)
    structure=models.ImageField(upload_to='image',blank=True,null=True)
    
    #任意ソート用に数値登録
    studynum=models.IntegerField('表示順序',
            default=1,
            blank=True,
            null=True,
            unique=False,
            validators=[MinValueValidator(1), MaxValueValidator(35)]
            )
    
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural="医薬品の名前・作用・学習時期・構造式の登録"
        
        constraints=[
            models.UniqueConstraint(
                fields=['field','name'],#分野と医薬品名の重複予防
                name="field_name"
                ),
            ]
    
#医薬品の学習順序カラム(ManyToMany)の影響を受けずに医薬品の並べ替えを実装


    
    
    
    
    
    
    
