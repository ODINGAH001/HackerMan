<?php
$_fp = fopen("php://stdin", "r");
/* Enter your code here. Read input from STDIN. Print output to STDOUT */
$line = fgets($_fp);
    while (($line = fgets($_fp)) !== false) {
    	$record=preg_split('/[\s]+/',$line, -1,PREG_SPLIT_NO_EMPTY);
    	//print_r($record);
        if(preg_match_all('/^(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$/',trim($record[1])))	//start
        echo 'VALID'.PHP_EOL;
        else
	        echo 'INVALID'.PHP_EOL;
    }
fclose($_fp);
?>