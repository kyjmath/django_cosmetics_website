from django import template

register = template.Library()

#template안에 있는 Library()라는 태그 생성 함수
@register.simple_tag(takes_context=True) 
def param_replace(context, **kwargs):
    #<QueryDict: {'type': ['마스크팩', '로션/에멀전', '세럼'], 'effect': ['진정', '미백'], 'price': ['0원 - 400000원'], 'page': [1]}>
    # d는 쿼리 딕트이다.
    #form을 통해 제출된 양식을 템플릿 태그 함수에서는 context로 받는것 같음..
    d = context['request'].GET.copy() 

    #kwargs = keyword argument로 가변인수 함수를 정의할 때 사용, 이를 함수의 정의에 넣어주면 변수의 갯수를 마음대로 넣어도 됨

    for k, v in kwargs.items(): 
        d[k] = v

    for k in [k for k, v in d.items() if not v]:
        del d[k]
        
    #urlencdoe()는 문자열을 url로 인코드 해줌
    #type=%EB%A7%88%EC%8A%A4%ED%81%AC%ED%8C%A9&type=%EB%A1%9C%EC%85%98%2F%EC%97%90%EB%A9%80%EC%A0%84&type=%EC%84%B8%EB%9F%BC&effect=%EC%A7%84%EC%A0%95&effect=%EB%AF%B8%EB%B0%B1&price=0%EC%9B%90+-+400000%EC%9B%90&page=9
    return d.urlencode()
    