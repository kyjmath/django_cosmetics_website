"""midproject_team1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cosmetics import views
from loginapp import views as auth_views # view 함수가 중복되는 것을 피한다
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.HomeFunc),  # 홈
    
    path('list', views.ListFunc),  # 화장품 리스트 
    
    # 찜관련
    path('cart', views.CartFunc),  
    path('savecart', views.SavecartFunc),  
    path('deletecart', views.DeletecartFunc),  
    
    path('product', views.ProductFunc),  # 상품 자세한 정보
    
    # 코멘트 관련
    path('comment', views.CommentFunc),  
    path('savecomment', views.SavecommentFunc), 
    path('deletecomment', views.DeletecommentFunc),   
    
    # 로그인 관련
    path('signup',views.SignUpFunc),
    path('calldb',views.IdDbFunc),
    path('login', auth_views.LoginFunc),
    path('login/auth',auth_views.Login),
    path('logout', auth_views.Logout),
    
    # DB관리 관련
    path('admin_add', views.Admin_addFunc), 
    path('admin_manage', views.Admin_manageFunc),
    path('data_delete', views.Data_deleteFunc), 
    path('data_add', views.Data_addFunc),  
    path('data_modify', views.Data_modifyFunc),  
    path('data_modify_save', views.Data_modify_saveFunc),  
]
