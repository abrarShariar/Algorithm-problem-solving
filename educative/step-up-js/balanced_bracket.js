function isBalanced (inputStr) {
    const strStack = []
    const setOfStartingBracket = new Set(["(", "{", "["])
    const setOfEndingBracket = new Set([')', '}', ']'])
    
    for (let ch of inputStr) {
        if (setOfStartingBracket.has(ch)) {
            strStack.push(ch)
        } else if (setOfEndingBracket.has(ch)) {
            poppedItem = strStack.pop()
            if ((ch == ')' && poppedItem == '(') || (ch == '}' && poppedItem == '{') || (ch == ']' && poppedItem == '[')) {
                continue
            } 
            return false
        }
    }
    return strStack.length == 0
}

const inputStrs = [
    "(x+y) - (4)",
    "(50)(",
    "[{]}",
    "}}}",
    "({{",
    ")",
    "(",
    "()"
]

inputStrs.forEach(item => {
    console.log(isBalanced(item))
})