from django.db import models

# Create your models here.
class MCQ_Quiz(models.Model):
    mq_no=models.CharField(max_length = 5,default="")
    question = models.CharField(max_length = 500)
    option1 = models.CharField(max_length = 50)
    option2 = models.CharField(max_length = 50)
    option3 = models.CharField(max_length = 50,null="True",blank="True")
    option4 = models.CharField(max_length = 50,null="True",blank="True")

class True_False(models.Model):
    tq_no=models.CharField(max_length = 5,default="")
    tfquestion = models.CharField(max_length = 500)
    tfoption1 = models.CharField(max_length = 50,null="True",blank="True")
    tfoption2 = models.CharField(max_length = 50,null="True",blank="True")
   
class Txt_Question(models.Model):
    txtq_no=models.CharField(max_length = 5,default="")
    txtquestion = models.CharField(max_length = 500)
    txtoption1 = models.CharField(max_length = 50,null="True",blank="True")
   
class Results(models.Model):
    user=models.CharField(max_length = 50,null="false")
    contact=models.CharField(max_length = 15,default="")
    email=models.CharField(max_length = 50,default="")
    a1 = models.CharField(max_length = 50,null="True",blank="True")
    a2 = models.CharField(max_length = 50,null="True",blank="True")
    a3 = models.CharField(max_length = 50,null="True",blank="True")
    a4 = models.CharField(max_length = 50,null="True",blank="True")
    a5= models.CharField(max_length = 50,null="True",blank="True")
    a6=models.CharField(max_length = 50,null="True",blank="True")
    a7= models.CharField(max_length = 50,null="True",blank="True")
    a8= models.CharField(max_length = 50,null="True",blank="True")
    a9= models.CharField(max_length = 50,null="True",blank="True")
    a10= models.CharField(max_length = 50,null="True",blank="True")
    
 
    