var flag = false;

function checkuser(){
	//获取输入的用户名和密码
	var username = $("#username").val();
	var password = $("#password").val();
	//判断用户名是否符合输入规范
	check_username(username);
	//用户名已符合规范，判断密码是否符合
	if(flag)
		check_password(password);
	$.ajax({
		url:"/userlogin",
		data:{username:username},
		success:function(data){
			if(password == data.password)
				window.location.href="/table_basic?id=" + data.id;
			else{
				alert("密码不正确，请重新输入");
				$("#password")[0].value="";
			}
			
		},error:function(){
			alert("该用户不存在，请联系管理员！");
		}
	})
}

function check_username(username){
	if(username.length==0){
		alert("用户名不能为空！");
	}
	else flag = true;
}

function check_password(password){
	if(password.length==0){
		alert("密码不能为空！");
	}
}






