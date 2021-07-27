프로젝트에 관해 더 자세히 보고 싶으면 project.pptx를 확인하세요.

<장고 프로젝트를 적용하는 방법>
1. 테이블 생성.docx 안에있는 생성코드로 테이블 4개를 생성한다.

2. excel_to_db.py 코드를 이용해서 cosmetics_data.xlsx 안의 데이터를 cosmetics 테이블 안으로 넣는다.
   (파일경로랑 db이름은 본인에 맞게 수정)

3. $$$$$$ 중요 $$$$$$$
    혹시 migrate할때 오류가 뜬다면 
    1. settings.py 안에 INSTALLED_APPS 안에 'django.contrib.admin', 이 행을 주석처리하고
    2. urls.py 안에 urlpatterns 안에 path('admin/', admin.site.urls), 이행도 주석처리하고 migrate 하면 될것이다.
    3. migrate 후에는 다시 주석 풀기




app : 1. cosmetics (주요앱)
      2. loginapp (로그인 기능 담당)
html 총 8개
css 총 4개
js 총 5개
