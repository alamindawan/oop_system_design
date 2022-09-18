<?php 
interface Fruits{
	public function color();
}


class Banana implements Fruits{
	public __construct(){
		echo 'I am constructor auto kaj kori';
	}

	public function color(){
		echo 'Banana like Yellow';
	}
}

class Jamrul implements Fruits{
	public function color(){
		echo 'Jamrul look like white';
	}
}



$obj = new Banana();
$obj->color();