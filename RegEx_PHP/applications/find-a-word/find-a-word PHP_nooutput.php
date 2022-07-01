<?php
$_fp = fopen("domains.txt", "r");
/* Enter your code here. Read input from STDIN. Print output to STDOUT */
$n=(int)fgets($_fp);
$paragraph='';
$list_words=array();
while($n>0)
    {
    	$paragraph.=' '.fgets($_fp);
   		$n--;
	}
	//print_r($list_words);
$list_words=preg_split('/[\s]+/', $paragraph, -1, PREG_SPLIT_NO_EMPTY);

$t=(int)fgets($_fp);
$i=0;
while($t>0)
{    
	$count=0;
	$word=trim(fgets($_fp));
	for($i=0;$i<count($list_words);$i++)
	{	
	// echo strpos($list_words[$i],trim($word));
	$regex='/^'.$word.'$/';
	if(preg_match_all($regex, $list_words[$i]))
	//if(strpos($list_words[$i],trim($line)) !== false && strpos($list_words[$i],'_') === false)
		$count++;
	}
	echo $count++.'</br>';
    $t--;
}
fclose($_fp);
?>