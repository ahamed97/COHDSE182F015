   <html>
<body>

<?php

 session_start();
 if(time() - $_SESSION['nt']<=10){
	$_SESSION["nt"] = time();
	echo"<h1>Hello....!</h1>"; 
 }else{
	 header("location: login.html");
	 
 }


?>

</body>
</html>