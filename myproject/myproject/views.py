from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from myapp.models import *


def base(req):
    return render(req,'base.html')

def home(req):
    return render(req,'home.html')



def loginpage(req):
    if req.method=='POST':
        username=req.POST.get('username')
        password=req.POST.get('password')

        user=authenticate(password=password,username=username)
        if user:
            login(req,user)
            return redirect('home')


    return render(req,'loginpage.html')


def register(req):

    if req.method=='POST':
        username=req.POST.get('username')
        user_type=req.POST.get('user_type')
        password=req.POST.get('password')
        confirm_password=req.POST.get('confirm_password')
        if password==confirm_password:
            user=Custom_user.objects.create_user(
                username=username,
                user_type=user_type,
                password=confirm_password,


            )
            return redirect('loginpage')
        else:
            return HttpResponse('password did not Matched')
        

    return render(req,'register.html')




def addresume(req):
 ALL_user=Custom_user.objects.all()
 if req.method=='POST':
    
        myid=req.POST.get('all_user_name')
        my_user=Custom_user.objects.get(id=myid)

        add=ResumeModel(
            user=my_user,
            skill=req.POST.get('skill'),
            education=req.POST.get('education'),
            language=req.POST.get('language'),
            img=req.FILES.get('img'),

        )
        add.save()
        return redirect ('resumelist')

 return render(req,"addresume.html",{'ALL_user':ALL_user})



def resumelist(req):
    data=ResumeModel.objects.all()
    text={
        'data':data
    }

    return render(req,'resumelist.html',text)




def deletepage(req,id):
    data=ResumeModel.objects.filter(id=id)

    data.delete()

    return redirect('resumelist')

def viewpage(req,id):

    user=get_object_or_404(Custom_user,id=id)
    RESUME=ResumeModel.objects.filter(user=user)
    EDUCATION=EDUCATION_MODEL.objects.filter(user=user)
    EXPERIENCE=EXPERIENCE_MODEL.objects.filter(user=user)
    INTEREST=INTEREST_MODEL.objects.filter(user=user)
    LANGUAGE=LANGUAGE_MODEL.objects.filter(user=user)
    SKILL=SKILL_MODEL.objects.filter(user=user)


    text={
        'RESUME':RESUME,
        'EDUCATION':EDUCATION,
        'EXPERIENCE':EXPERIENCE,
        'INTEREST':INTEREST,
        'LANGUAGE':LANGUAGE,
        'SKILL':SKILL,

    }

    return render(req,'viewpage.html',text)




def edit(req,id):
    data=ResumeModel.objects.filter(id=id)
    text={
        'data':data
    }

    return render(req,'edit.html',text)

def update(req):
 
 if req.method=='POST':
        id=req.POST.get('id')
        skill=req.POST.get('skill')
        education=req.POST.get('education')
        language=req.POST.get('language')
        img=req.FILES.get('img')
        old_img=req.FILES.get('old_img')



        add=ResumeModel(

            id=id,
            skill=skill,
            education=education,
            language=language,
            img=img,

        )
        if img:
            img=img
            add.save()
        else:
            img=old_img
            add.save()

        return redirect ('resumelist')




def addskill(req):
 ALL_user=Custom_user.objects.all()
 myid=req.POST.get('all_user_name')
 skill_name=INTERMEDIATE_MODEL.objects.all()

 if req.method=='POST':
        skill_id=req.POST.get('skill_id')
        
        skill_name=get_object_or_404(INTERMEDIATE_MODEL,id=skill_id),
    
        my_user=Custom_user.objects.get(id=myid)
        add=SKILL_MODEL(
            user=my_user,
            skill_name=skill_name,
            PROFHECEENCY=req.POST.get('PROFHECEENCY'),

        )
        add.save()
        return redirect ('skilllist')

 return render(req,"addskill.html",{'ALL_user':ALL_user,'skill_name':skill_name})





def skilllist(req):
    data=SKILL_MODEL.objects.all()
    text={
        'data':data
    }

    return render(req,'skilllist.html',text)



def addeducation(req):
 ALL_user=Custom_user.objects.all()
 myid=req.POST.get('all_user_name')

 if req.method=='POST':
    
        my_user=Custom_user.objects.get(id=myid)

        add=EDUCATION_MODEL(
            user=my_user,
            start_year=req.POST.get('start_year'),
            end_year=req.POST.get('end_year'),
            type=req.POST.get('type'),

        )
        add.save()
        return redirect ('educationlist')

 return render(req,"addeducation.html",{'ALL_user':ALL_user})





def educationlist(req):
    data=EDUCATION_MODEL.objects.all()
    text={
        'data':data
    }

    return render(req,'educationlist.html',text)




def addlanguage(req):
 ALL_user=Custom_user.objects.all()
 myid=req.POST.get('all_user_name')

 if req.method=='POST':
    
        my_user=Custom_user.objects.get(id=myid)

        add=LANGUAGE_MODEL(
            user=my_user,
            language=req.POST.get('language'),
            PROFHECEENCY=req.POST.get('PROFHECEENCY'),

        )
        add.save()
        return redirect ('languagelist')

 return render(req,"addlanguage.html",{'ALL_user':ALL_user})





def languagelist(req):
    data=LANGUAGE_MODEL.objects.all()
    text={
        'data':data
    }

    return render(req,'languagelist.html',text)



def addinterest(req):
 ALL_user=Custom_user.objects.all()
 myid=req.POST.get('all_user_name')

 if req.method=='POST':
    
        my_user=Custom_user.objects.get(id=myid)

        add=INTEREST_MODEL(
            user=my_user,
            interest=req.POST.get('interest'),

        )
        add.save()
        return redirect ('interestlist')

 return render(req,"addinterest.html",{'ALL_user':ALL_user})





def interestlist(req):
    data=INTEREST_MODEL.objects.all()
    text={
        'data':data
    }

    return render(req,'interestlist.html',text)



def addexperience(req):
 ALL_user=Custom_user.objects.all()
 myid=req.POST.get('all_user_name')

 if req.method=='POST':
    
        my_user=Custom_user.objects.get(id=myid)

        add=EXPERIENCE_MODEL(
            user=my_user,
            tittle=req.POST.get('tittle'),
            company=req.POST.get('company'),
            start_date=req.POST.get('start_date'),
            end_date=req.POST.get('tittle'),

        )
        add.save()
        return redirect ('experiencelist')

 return render(req,"addexperience.html",{'ALL_user':ALL_user})





def experiencelist(req):
    data=EXPERIENCE_MODEL.objects.all()
    text={
        'data':data
    }

    return render(req,'experiencelist.html',text)