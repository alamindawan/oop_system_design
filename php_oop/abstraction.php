<?php 

abstract class AbstractionClass{
	abstract protected function getValue();
	abstract protected function prefix();

	public function display(){
		echo $this->getValue().' '.$this->prefix();
	}
}

class Concrete extends AbstractionClass{
	public function getValue(){
		return 1000000;
	}

	public function prefix(){
		return '001 ';
	}
}

class Concrete2 extends AbstractionClass{
	public function getValue(){
		return 10000001;
	}

	public function prefix(){
		return '002 ';
	}
}

$obj = new Concrete2();
echo $obj->display();