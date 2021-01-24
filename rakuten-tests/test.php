// you can write to stdout for debugging purposes, e.g.
// print "this is a debug message\n";

function solution($A) {
    sort($A);
    $A = array_unique(array($A));

    for ($i = 1; $i <= count($A); $i++) {
        if ($i != $A[$i]) {
            return $i;
        }
    }

    return $i;
}
