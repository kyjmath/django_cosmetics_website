from django.shortcuts import render, redirect
from cosmetics.models import Cosmetics, Basket, Client, Comment
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Sum
from django.db.models import Q
from loginapp.models import User
from datetime import datetime


# 홈 화면(/home)
def HomeFunc(request):
    number_of_products = len(Cosmetics.objects.all())
    number_of_clients = len(User.objects.all())
    number_of_baskets = len(Basket.objects.all())
    return render(request, 'home.html', {"products":number_of_products, \
                                         "clients":number_of_clients, \
                                         "baskets":number_of_baskets 
                                         })
    
    
# 상품 리스트 보여주기(/list)
def ListFunc(request):
    # GET 방식 요청
    if request.method == "GET":
        # 필터링한 값들 받아오기
        type = request.GET.getlist('type') 
        effect = request.GET.getlist('effect') 
        gen = request.GET.getlist('gen')
        age = request.GET.getlist('age')
        skin_type = request.GET.getlist('skin_type')
        grade = request.GET.getlist('grade')     
        price = request.GET.get('price')
                
        # 아무것도 안골랐을경우, 전체값 적용
        if type == []:
            type = ["스킨/토너", "크림", "마스크팩", "로션/에멀전", "세럼", "에센스"]
        if effect == []:
            effect = ["진정", "미백", "탄력", "수분", "주름개선", "보습"]
        if gen == []:
            gen = ["남", "여"]  
        if age == []:
            age = ["10", "20", "30", "40", "50"]  
        if "1" in skin_type or skin_type == []:
            skin_type = ["1", '건성', '복합성', '민감성', '지성']
        if grade != []:  # grade를 골랐을 경우, .5개 별도 추가 (예, 별3개를 선택했을경우, 별3.5개도 보여줌)
            for i in range(len(grade)):
                x = int(grade[i]) + 0.5
                grade.append(x)   
        if grade == []:
            grade = [2.5, 3, 3.5, 4, 4.5, 5]
            
         
        # 필터된 데이터 db에서 불러오기
        # 제품유형 필터
        Cosmetics_list = Cosmetics.objects.filter(type__in = type) 
        
        # 평점 필터 
        Cosmetics_list = Cosmetics_list.filter(grade__in = grade) 
        
        # 성별 필터
        Cosmetics_list = Cosmetics_list.filter(gender__in = gen) 
        
        # 가격 필터
        if price == None:
            price = "0원 - 400000원"
        price = price.split(' - ')
        min_price = int(price[0][:-1])
        max_price = int(price[1][:-1])
        Cosmetics_list = Cosmetics_list.filter(price__range = (min_price, max_price))  
        
        # 효과 필터
        if len(effect) == 1:
            Cosmetics_list = Cosmetics_list.filter(effect__contains = effect[0])
        elif len(effect) == 2:
            Cosmetics_list = Cosmetics_list.filter(Q(effect__contains = effect[0]) |
                                                   Q(effect__contains = effect[1]))
        elif len(effect) == 3:
            Cosmetics_list = Cosmetics_list.filter(Q(effect__contains = effect[0]) |
                                                   Q(effect__contains = effect[1]) |
                                                   Q(effect__contains = effect[2]))
        elif len(effect) == 4:
            Cosmetics_list = Cosmetics_list.filter(Q(effect__contains = effect[0]) |
                                                   Q(effect__contains = effect[1]) |
                                                   Q(effect__contains = effect[2]) |
                                                   Q(effect__contains = effect[3]))
        elif len(effect) == 5:
            Cosmetics_list = Cosmetics_list.filter(Q(effect__contains = effect[0]) |
                                                   Q(effect__contains = effect[1]) |
                                                   Q(effect__contains = effect[2]) |
                                                   Q(effect__contains = effect[3]) |
                                                   Q(effect__contains = effect[4]))
        elif len(effect) == 6:
            Cosmetics_list = Cosmetics_list.filter(Q(effect__contains = effect[0]) |
                                                   Q(effect__contains = effect[1]) |
                                                   Q(effect__contains = effect[2]) |
                                                   Q(effect__contains = effect[3]) |
                                                   Q(effect__contains = effect[4]) |
                                                   Q(effect__contains = effect[5]))

        # 연령대 필터
        if len(age) == 1:
            Cosmetics_list = Cosmetics_list.filter(age__contains = age[0])
        elif len(age) == 2:
            Cosmetics_list = Cosmetics_list.filter(Q(age__contains = age[0]) |
                                                   Q(age__contains = age[1]))
        elif len(age) == 3:
            Cosmetics_list = Cosmetics_list.filter(Q(age__contains = age[0]) |
                                                   Q(age__contains = age[1]) |
                                                   Q(age__contains = age[2]))
        elif len(age) == 4:
            Cosmetics_list = Cosmetics_list.filter(Q(age__contains = age[0]) |
                                                   Q(age__contains = age[1]) |
                                                   Q(age__contains = age[2]) |
                                                   Q(age__contains = age[3]))
        elif len(age) == 5:
            Cosmetics_list = Cosmetics_list.filter(Q(age__contains = age[0]) |
                                                   Q(age__contains = age[1]) |
                                                   Q(age__contains = age[2]) |
                                                   Q(age__contains = age[3]) |
                                                   Q(age__contains = age[4]))
        
        # 피부타입 필터
        if len(skin_type) == 1:
            Cosmetics_list = Cosmetics_list.filter(skin_type__contains = skin_type[0])
        elif len(skin_type) == 2:
            Cosmetics_list = Cosmetics_list.filter(Q(skin_type__contains = skin_type[0]) |
                                                   Q(skin_type__contains = skin_type[1]))
        elif len(skin_type) == 3:
            Cosmetics_list = Cosmetics_list.filter(Q(skin_type__contains = skin_type[0]) |
                                                   Q(skin_type__contains = skin_type[1]) |
                                                   Q(skin_type__contains = skin_type[2]))
        elif len(skin_type) == 4:
            Cosmetics_list = Cosmetics_list.filter(Q(skin_type__contains = skin_type[0]) |
                                                   Q(skin_type__contains = skin_type[1]) |
                                                   Q(skin_type__contains = skin_type[2]) |
                                                   Q(skin_type__contains = skin_type[3]))
        elif len(skin_type) == 5:
            Cosmetics_list = Cosmetics_list.filter(Q(skin_type__contains = skin_type[0]) |
                                                   Q(skin_type__contains = skin_type[1]) |
                                                   Q(skin_type__contains = skin_type[2]) |
                                                   Q(skin_type__contains = skin_type[3]) |
                                                   Q(skin_type__contains = skin_type[4]))
        elif len(skin_type) == 6:
            Cosmetics_list = Cosmetics_list.filter(Q(skin_type__contains = skin_type[0]) |
                                                   Q(skin_type__contains = skin_type[1]) |
                                                   Q(skin_type__contains = skin_type[2]) |
                                                   Q(skin_type__contains = skin_type[3]) |
                                                   Q(skin_type__contains = skin_type[4]) |
                                                   Q(skin_type__contains = skin_type[5]))        
        
        
        # 정렬
        sort_method = request.GET.get('sort')
        if sort_method != None:
            sort_method = int(sort_method)
        
        if sort_method == None or sort_method == 1:
            pass
        elif sort_method == 2:
            Cosmetics_list = Cosmetics_list.order_by("price")
        elif sort_method == 3:
            Cosmetics_list = Cosmetics_list.order_by("-price")
        elif sort_method == 4:
            Cosmetics_list = Cosmetics_list.order_by("-grade")
        
      
        # 페이징
        paginator = Paginator(Cosmetics_list, 6)
        page = request.GET.get('page')
        
        try:
            data = paginator.page(page)
        
        except PageNotAnInteger:
            data = paginator.page(1)
         
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
          
        return render(request, 'list.html', {'data':data, "sort_method":sort_method})
        
        
# 찜 목록 보여주기(/cart)
def CartFunc(request):
    client_id = request.GET.get('id')
    cos_no = Basket.objects.filter(client_id = client_id).values('cos_no')
    Basket_List = Cosmetics.objects.filter(no__in = cos_no)
    total_price = Cosmetics.objects.filter(no__in = cos_no).aggregate(Sum('price'))['price__sum']
    if total_price == None:
        total_price = 0
        
    # 페이징
    paginator = Paginator(Basket_List, 6)
    page = request.GET.get('page')
    
    try:
        datas = paginator.page(page)
    
    except PageNotAnInteger:
        datas = paginator.page(1)
     
    except EmptyPage:
        datas = paginator.page(paginator.num_pages)
            
    return render(request, 'cart.html', {'datas':datas, 'total_price':total_price})


# 찜하기 버튼 눌렀을때 basket 테이블에 추가
def SavecartFunc(request):
    cos_no = request.GET.get("no")
    cos_no = int(cos_no)
    client_id = request.GET.get('id')
    isRegistered = False
    
    
    if Basket.objects.all().count() == 0:
        Basket(
            no = 1,
            cos_no = Cosmetics.objects.get(no = cos_no),
            client_id = client_id
        ).save()
        isRegistered = True
    
    else:
        Basket(
            no = Basket.objects.latest('no').no + 1,
            cos_no = Cosmetics.objects.get(no = cos_no),
            client_id = client_id
        ).save()
        isRegistered = True
        
    context = {'check' : isRegistered}
    return HttpResponse(json.dumps(context), content_type = "application/json") 


# 찜 목록에서 상품 삭제하기
def DeletecartFunc(request):
    cos_no = request.GET.get('no')
    client_id = request.GET.get('id')
    data = Basket.objects.filter(cos_no = cos_no, client_id=client_id)
    data.delete()
    return HttpResponseRedirect("/cart?id="+client_id)  
    
    
# 상품 상세정보 보여주기(/product)
def ProductFunc(request):
    no = request.GET.get('no')
    product = Cosmetics.objects.get(no=no)
    return render(request, 'product.html', {'product':product})


def CommentFunc(request):
    product = request.GET.get('product') 
        
    if product == None:
        comment = Comment.objects.all().order_by('-date')
    else:
        cos_num = Cosmetics.objects.filter(product__contains = product).values_list('no')
        comment = Comment.objects.filter(cos_num__in = cos_num).order_by('-date')
        
    # 페이징
    paginator = Paginator(comment, 5)
    page = request.GET.get('page')
    
    try:
        datas = paginator.page(page)
    
    except PageNotAnInteger:
        datas = paginator.page(1)
     
    except EmptyPage:
        datas = paginator.page(paginator.num_pages)
    
    return render(request, 'comment.html', {'comment':datas})


# 코멘트 저장
def SavecommentFunc(request):
    cos_name = request.GET.get('product')
    product = Cosmetics.objects.get(product = cos_name)
    cos_num = product.no
    client_user = request.GET.get('id')
    content = request.GET.get('contentarea')  
    date = datetime.now()
    
    if Comment.objects.all().count() == 0:
        Comment(
            no = 1,
            cos_num = Cosmetics.objects.get(no = cos_num),
            client_user = Client.objects.get(id = client_user),
            content = content,
            date = date
        ).save()
    
    else:
        Comment(
            no = Comment.objects.latest('no').no + 1,
            cos_num = Cosmetics.objects.get(no = cos_num),
            client_user = Client.objects.get(id = client_user),
            content = content,
            date = date
        ).save()

    return HttpResponseRedirect("/comment") 


# 코멘트 삭제
def DeletecommentFunc(request):
    no = request.GET.get('no')
    data = Comment.objects.get(no = no)
    data.delete()
    return HttpResponseRedirect("/comment")


# 회원가입 아이디 중복 확인
@csrf_exempt
def Id_CheckFunc(request):
    id = request.POST.get('id')
    isRegister = False
    try:
        data = Client.objects.get(id = id)
        if data != None:
            isRegister = True
    
    except Exception as e:
        print('err:',e)
    context = {'id' : isRegister}
    return HttpResponse(json.dumps(context), content_type = "application/json")  


@csrf_exempt
def IdDbFunc(request):
    id = request.POST.get('id')
    isRegistered = False
    try:
        data = User.objects.get(username = id)
        if data != None :
            isRegistered = True
    
    except Exception as e:
        print('err:',e)
    context = {'id' : isRegistered}
    return HttpResponse(json.dumps(context), content_type = "application/json")  


# 회원가입 완료
@csrf_exempt
def SignUpFunc(request):
    
    if request.method == "GET":
        return render(request,"home.html" )
    
    elif request.method == "POST":
        Client(
            id = request.POST.get('user_id'),
            passwd = request.POST.get('user_password'),
            name = request.POST.get('user_name')
        ).save()
        
        User(
            name = request.POST.get('user_name'),
            username = request.POST.get('user_id'),
            password = request.POST.get('user_password')
        ).save()
    
        return redirect('/home')
       
    else :
        return render(request,'error.html')


# 관리자를 위한 데이터 관리 
def Admin_addFunc(request):
    return render(request, 'admin_add.html')


# 관리자를 위한 데이터 추가
def Admin_manageFunc(request):
    datas = Cosmetics.objects.all()
    datas = datas.order_by('-no')
    
    # 페이징
    paginator = Paginator(datas, 15)
    page = request.GET.get('page')
    
    try:
        datas = paginator.page(page)
    
    except PageNotAnInteger:
        datas = paginator.page(1)
     
    except EmptyPage:
        datas = paginator.page(paginator.num_pages)
    
    return render(request, 'admin_manage.html', {'datas':datas})


# 데이터 삭제하기
def Data_deleteFunc(request):
    no = request.GET.get('no')
    data = Cosmetics.objects.filter(no = no)
    data.delete()
    return HttpResponseRedirect('/admin_manage')


# 데이터 추가하기
def Data_addFunc(request):
    try:
        brand = request.GET.get('brand')
        product = request.GET.get('product')
        type = request.GET.get('type')
        effect = request.GET.get('effect')
        ingredient = request.GET.get('ingredient')
        price = int(request.GET.get('price'))
        grade = float(request.GET.get('grade'))
        gender = request.GET.get('gender')
        age = request.GET.get('age')
        skin_type = request.GET.get('skin_type')
        pro_image = request.GET.get('pro_image')
    
    except: 
        return HttpResponseRedirect('/admin_manage')
        
    Cosmetics(
        no = Cosmetics.objects.latest('no').no + 1,
        brand = brand,
        product = product,
        type = type,
        effect = effect,
        ingredient = ingredient,
        price = price,
        grade = grade,
        gender = gender,
        age = age,
        skin_type = skin_type,
        pro_image = pro_image
    ).save()
    
    return HttpResponseRedirect('/admin_manage')


# 데이터 수정창
def Data_modifyFunc(request):
    no = request.GET.get('no')
    data = Cosmetics.objects.get(no = no)
    return render(request, 'admin_modify.html', {'data':data})


# 데이터 수정확인 
def Data_modify_saveFunc(request):
    no = request.GET.get('no')
    
    try:
        brand = request.GET.get('brand')
        product = request.GET.get('product')
        type = request.GET.get('type')
        effect = request.GET.get('effect')
        ingredient = request.GET.get('ingredient')
        price = int(request.GET.get('price'))
        grade = float(request.GET.get('grade'))
        gender = request.GET.get('gender')
        age = request.GET.get('age')
        skin_type = request.GET.get('skin_type')
        pro_image = request.GET.get('pro_image')
    
    except: 
        return HttpResponseRedirect('/data_modify?no='+no)
    
    data = Cosmetics.objects.filter(no = no)
    data.update(
        brand = brand,
        product = product,
        type = type,
        effect = effect,
        ingredient = ingredient,
        price = price,
        grade = grade,
        gender = gender,
        age = age,
        skin_type = skin_type,
        pro_image = pro_image
    )
     
    return HttpResponseRedirect('/admin_manage')
    



