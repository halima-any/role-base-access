from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom_user(AbstractUser):
    USER=[
        ('admin','Admin'),
        ('viewer','Viewer')
    ]
    user_type=models.CharField(choices=USER,max_length=100,null=True)

    def  __str__(self):
        return f"{self.username}-{self.first_name}-{self.last_name}"
    

    
class ResumeModel(models.Model):
       
    GENDER=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]

    gender_type=models.CharField(max_length=100,null=True,choices=GENDER)
     

    user=models.OneToOneField(Custom_user,null=True,on_delete=models.CASCADE)


    linkdin=models.URLField(max_length=100, null=True)
    github=models.CharField(max_length=100, null=True)
    codepen=models.CharField(max_length=100, null=True)
    yoursite=models.CharField(max_length=100, null=True)

    contact=models.CharField(max_length=100, null=True)
    experience=models.CharField(max_length=100, null=True)
    designation=models.CharField(max_length=100, null=True)
    summary=models.CharField(max_length=100, null=True)
    skill=models.CharField(max_length=100, null=True)
    education=models.CharField(max_length=100, null=True)
    award=models.CharField(max_length=100, null=True)
    language=models.CharField(max_length=100, null=True)
    intrest=models.CharField(max_length=100, null=True)
    img=models.ImageField(upload_to='Media/img',null=True)

    def __str__(self) -> str:
        return f"{self.user}"
    

class EDUCATION_MODEL(models.Model):
    user=models.OneToOneField(Custom_user,null=True,on_delete=models.CASCADE)
    start_year=models.DateField(max_length=100, null=True)
    end_year=models.DateField(max_length=100, null=True)
    type=models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return f"{self.user}"

class EXPERIENCE_MODEL(models.Model):
    user=models.OneToOneField(Custom_user,null=True,on_delete=models.CASCADE)

    tittle=models.CharField(max_length=100, null=True)
    company=models.CharField(max_length=100, null=True)
    start_date=models.DateField(max_length=100, null=True)
    end_date=models.DateField(max_length=100, null=True)
    description=models.TextField(max_length=100, null=True)


    def __str__(self) -> str:
        return f"{self.user}"

class INTEREST_MODEL(models.Model):
    user=models.OneToOneField(Custom_user,null=True,on_delete=models.CASCADE)
    interest=models.CharField(max_length=100, null=True)


    def __str__(self) -> str:
        return f"{self.user}"


class LANGUAGE_MODEL(models.Model):

        
    PROFHECEENCY=[
        ('high','HIGH'),
        ('low','LOW'),
        ('medium','MEDIUM'),
    ]

    PROFHECEENCY=models.CharField(max_length=100,null=True,choices=PROFHECEENCY)
    user=models.OneToOneField(Custom_user,null=True,on_delete=models.CASCADE)

    language=models.CharField(max_length=100, null=True)



    def __str__(self) -> str:
        return f"{self.user}"


class SKILL_MODEL(models.Model):

          
    PROFHECEENCY=[
        ('high','HIGH'),
        ('low','LOW'),
        ('medium','MEDIUM'),
    ]
    PROFHECEENCY=models.CharField(max_length=100,null=True,choices=PROFHECEENCY)
    user=models.OneToOneField(Custom_user,null=True,on_delete=models.CASCADE)
    skill_name=models.CharField(max_length=100, null=True)


    def __str__(self) -> str:
        return f"{self.user}"
    


class INTERMEDIATE_MODEL(models.Model):
    skill_name=models.CharField(max_length=100)


    
    def __str__(self) -> str:
        return f"{self.skill_name}"
     
















    


