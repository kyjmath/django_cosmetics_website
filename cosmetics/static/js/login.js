$(document).ready(function(){
	
	var ischecked = false

$("#id-check").click(function(){
	 let id = $("#user_id").val()
		$.ajax({
			async:'true', 
			url:"calldb", 
			type:"post",
			data: {"id" : id},
			dataType:'json',
			success:function(datas){
				console.log(datas.id);
	
			if( id == '' || id.length < 6){
				 alert('아이디를 6자 이상 입력해주세요')
				 $("#user_id").focus(); //입력창 커서 활성화 함수
				 ischecked = false
				 return false
			 }
			 if(datas.id == true){
				 $("#user_id").val('');
				 alert('이미 사용중인 아이디입니다')
				 $("#user_id").focus();
				 ischecked = false
				 return false		
			
			 }else
			  ischecked = true
			  alert('사용가능한 아이디입니다')		
			  $("#user_id").blur(); //입력창 비활성화 함수
			 
			 
		
		},
		error : function(data) {
            alert("알수없는 오류가 발생했습니다.\n관리자에게 문의해 주시기 바랍니다.");
            return false;
		}
	});  
});
// 아이디 중복확인 후 재수정시 중복확인 안하면 다시 중복확인 요청메소드 :  focus 작동시 비중복상태로 전환
$("#user_id").focus(function(){  
		ischecked = false

}); 

$("#signup").click(function(){
	signup();
});

function signup(){
	let name = document.getElementById('user_name').value
	let id = document.getElementById('user_id').value
	let password = document.getElementById('user_password').value
	let confirm_password = document.getElementById('confirm_password').value

	
	
	if(name == ''){
	alert("이름을 입력해주세요")
	return false
	}
	if(id == '' || id.length < 6){
	alert("아이디를 6자 이상 입력해주세요")
	return false
	}
	if(ischecked != true){
	alert("아이디 중복확인을 해주세요")
	return false
	}

	if(password == ''|| password.length < 6){
	alert("비밀번호를 6자 이상 입력해주세요")
	return false
	}
	if(confirm_password == ''){
	alert("비밀번호확인을 입력해주세요")
	return false
    }
	if(password != confirm_password){
	alert("비밀번호가 다릅니다. 다시 입력해주세요")
	return false
	}
	else 
	document.signup.submit()
	alert("가입이 완료되었습니다")
	}

$("#loginbutton").click(function(){
	 let id = $("#id").val()
	 let password = $("#password").val()
		$.ajax({
			async:'true', 
			url:"login", 
			type:"post",
			data: {"id" : id, "password": password},
			dataType:'json',
			success:function(data){
				console.log(data.id);
				console.log(data.password)
				
				if(id == ''){
					 alert('아이디를 입력해주세요')
					 return false
				 }
				if(password == ''){
					 alert('비밀번호를 입력해주세요')
					 return false
				 }
				 
				if(data.id == false){
					 alert('아이디가 잘못되거나 존재하지 않습니다')
					 return false
				 }
				if(data.password == false){
				 alert('비밀번호가 잘못되었습니다.')
				 return false
				
				}else 
				document.login.submit()
			
			}
		});
	});
});