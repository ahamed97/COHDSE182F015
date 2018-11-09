<?php
if(isset($_REQUEST["txtUserName"])){
 $username = $_POST["txtUserName"];
 $password = md5($_POST["txtPassword"]);
$con = mysqli_connect("localhost","root");
 mysqli_select_db($con,"db_login");
 $sql = "select Password from tbl_logindetails where username = '$username' and password = '$password'";
 $result = mysqli_query($con,$sql);
$count = mysqli_num_rows($result);
 if($count == 1) {
	session_start();
    $_SESSION['login_user'] = $myusername;
	$_SESSION['nt'] = time();
    header("location: welcome.php");
	
 }else {
    $error = "User Name or Password is invalid";
	echo $error;
}
}
?>