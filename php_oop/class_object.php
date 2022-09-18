<?php 
include 'static.php';
class Dog{
	private $age =10;
	public $age2 =20;
	function __construct($name){
		echo "It's first class ".$name." age = ".$this->age;
	}

	function __call($name,$arg){
		echo $name." oh ai function ki ache tumi je try koro!";

	}

	public function display(){
		CommonFunction::address();
	}
}

// class Cat{

// }

$obj = new Dog("Alamin");
echo $obj->age2;
echo $obj->display();

$stk = new CommonFunction();
$stk->call();