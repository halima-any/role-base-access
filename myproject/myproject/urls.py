
from django.contrib import admin
from django.urls import path
from myproject.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', base,name='base'),
    path('', loginpage,name='loginpage'),
    path('register/', register,name='register'),
    path('home/', home,name='home'),
    path('addresume/', addresume,name='addresume'),
    path('resumelist/', resumelist,name='resumelist'),
    path('deletepage/<int:id>', deletepage,name='deletepage'),
    path('viewpage/<int:id>',viewpage,name='viewpage'),
    path('edit/<int:id>',edit,name='edit'),
    path('update/',update,name='update'),
    path('addskill/',addskill,name='addskill'),
    path('skilllist/',skilllist,name='skilllist'),
    path('addeducation/',addeducation,name='addeducation'),
    path('educationlist/',educationlist,name='educationlist'),
    path('addlanguage/',addlanguage,name='addlanguage'),
    path('languagelist/',languagelist,name='languagelist'),
    path('addinterest/',addinterest,name='addinterest'),
    path('interestlist/',interestlist,name='interestlist'),
    path('addexperience/',addexperience,name='addexperience'),
    path('experiencelist/',experiencelist,name='experiencelist'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
