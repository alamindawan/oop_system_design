<?php 
class CommonFunction{
	public static function contact(){
		echo ' 017620420000000';
	}

	public static function address(){
		echo self::contact(). ' Dhaka ';
	}

	public static function call(){
		echo "TABA";
	}
	
}