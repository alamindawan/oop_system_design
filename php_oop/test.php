<?php 

function recursive($n){
	if($n == 0){
		exit;
	}		
	echo $n;
	recursive($n-1);

	
}

recursive(5);