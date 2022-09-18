<?php 
class Flower{
	public $petals;
	public function __construct(){
		$this->petals = 6;
		$leaf = 3;

	}
}


$obj = new Flower();
echo $obj->petals;
//echo 4444;
//flowers/flower.php