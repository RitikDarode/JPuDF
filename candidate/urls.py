from django.urls import path
from candidate import views
urlpatterns = [
     path('Services/',views.Services,name='Services'),
     path('Jobs/',views.Jobs,name='Jobs'),
     path('Companies/',views.Companies,name='Companies'),
     path('About/',views.About,name='About'),
     path('Contact/',views.Contact,name='Contact'),

     path('dash/',views.candidateHome,name='dash'),
     path('',views.Home,name='home'),
     path('applyjob/<int:id>/',views.applyJob,name='applyjob'),
     path('applylist/',views.myjoblist,name='mylist'),
]
