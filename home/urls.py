from django.urls import path , include
from home import views
urlpatterns = [
    path('',views.home,name='home'),
    path('contact/', views.contact1, name='contact'),
    path('about/', views.about, name='about'),
    path('search/',views.search,name='search'), 
    path('signup/',views.handlesignup,name='signup'), 
    path('login/',views.handlelogin,name='handlelogin'), 
    path('logout/',views.handlelogout,name='handlelogout'), 
    
]
