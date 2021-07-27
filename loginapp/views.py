from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
import json
from django.contrib.auth import authenticate
from django.contrib import auth
from loginapp.models import User
from django.contrib.auth import get_user_model




@csrf_exempt
def LoginFunc(request):
    lg_id = request.POST.get('id')
    lg_passwd = request.POST.get('password')
    idChecked = False
    psChecked = False
    
    try :     
        dataID = User.objects.get(username = lg_id)
        
        if dataID != None :
            idChecked = True
                              
    except Exception as e:
        print('err:',e)
        
    try :     
        dataPS = User.objects.filter(username = lg_id, password = lg_passwd).exists()
        
        if dataPS == True :
            psChecked = True
                              
    except Exception as e:
        print('err:',e)
    
    context = {'id' : idChecked, 'password' : psChecked}
    
    return HttpResponse(json.dumps(context), content_type = "application/json") 

@csrf_exempt
def Login(request):
    if request.method == 'POST':
        username = request.POST.get("id")
        password = request.POST.get("password")
        user = User.objects.filter(username = username)
        if user is not None:
            user = User.objects.get(username = username)
            auth.login(request, user)
            return redirect('/home')
        else:
            return HttpResponse('Login failed. Try again.')
    else:
        return render(request, 'error.html')
    

def Logout(request):
    auth.logout(request)
    return redirect('/home')












