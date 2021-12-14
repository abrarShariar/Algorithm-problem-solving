function enter_passcode (passcode) {
    console.log("Entering passcode");
    for (const ch of passcode) {
        tap_num(ch)
            .then((resolvedVal) => {
                console.log("This is resolved" + resolvedVal);
            }, (error) => {
                console.log("Error: " + error)
            });
    }
}

function tap_num (digit) {
    return new Promise((resolve, reject) => {
        if (digit !== 'x') {
            resolve(`This is a resolved promise! Digit: ${digit}`);
        }
        reject(`No digit Reject ${digit}`);
    });
}

enter_passcode("abxcd");
// enter_passcode("x");