<?php

$sayi="12231231131";

$odd = !strlen($sayi)%2;

$toplam = 0;

for($i=0;$i<strlen($sayi);++$i) {

$n=0+$sayi[$i];

$odd=!$odd;

if($odd) {

$toplam+=$n;

} else {

$x=2*$n;

$toplam+=$x>9?$x-9:$x;

}

}

if (($toplam%10)==0){  echo $sayi." için luhn algoritmasi geçerli";}

else {echo $sayi." için luhn algoritmasi geçerli değil";}

?>
