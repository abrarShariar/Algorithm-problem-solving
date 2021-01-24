// you can write to stdout for debugging purposes, e.g.
// print "this is a debug message\n";

function solution($A, $K) {

    rsort($A);

    // separate even and odd numbers
    $evenArr = array();
    $oddArr = array();

    for ($i = 0;$i < count($A); $i++) {
        if ($A[$i] % 2 == 0) {
            array_push($evenArr, $A[$i]);
        } else {
            array_push($oddArr, $A[$i]);
        }
    }

    // sort even and odd desc
    rsort($evenArr);
    rsort($oddArr);

    // largest of k numbers
    $largest_k = array();

    for ($i = 0; $i < count($A); $i++) {
        array_push($A[$i]);
    }

    $sum = array_sum($A);

    // if even
    if ($sum % 2 == 0) {
        return $sum;
    }

    while ($sum % 2 != 0) {
        
    }






}
