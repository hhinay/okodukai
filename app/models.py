from django.db import models
from django.utils import timezone

# Create your models here.
class Money(models.Model):
    duedate = models.DateField("日付",default=timezone.now)
    content = models.TextField("メモ",null=True,blank=False)
    title = models.IntegerField("支出",default=0,null = True,blank=False)
    title2 = models.IntegerField("収入",default=0,null = True,blank=False)
    balance = models.IntegerField(default=0,null = True,blank=True)
    
    def swap_title_and_title2(self):
        temp = self.title
        self.title = self.title2
        self.title2 = temp
        self.save()

def __str__(self):
        return '<id:' + str(self.id) + ',' + self.name + ',' + self.department + '>'

class Want(models.Model):
    memo = models.TextField("メモ",max_length=255)
    yen = models.IntegerField("金額",null=True)

def __str__(self):
    return self.title
