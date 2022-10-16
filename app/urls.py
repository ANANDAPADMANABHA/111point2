from django.urls import path
from . import views

urlpatterns = [
    path('',views.userLogin,name="userLogin"),
    path('userProfile',views.userProfile,name="userProfile"),
    path('userSignup',views.userSignup,name="userSignup"),
    path('uploadPost',views.uploadPost,name="uploadPost"),
    path('profileEdit/<int:id>/',views.profileEdit,name="profileEdit"),
    path('shorts',views.shorts,name="shorts"),
    path('userLogout',views.userLogout,name="userLogout"),

    


    

    
]