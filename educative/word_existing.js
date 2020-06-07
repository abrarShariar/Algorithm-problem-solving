let board = [ 
	['A','B','C','E'], 
	['S','F','C','S'], 
	['A','D','E','E'] 
];


function check (row, col, word, step) {
	if (step === word.length - 1) {
		return true;
	}
	// check right
	if ((col + 1 < board[0].length) && (board[row][col+1] === word[step+1])) {
		console.log(word[step]);
		step++;
		markPath(row, col+1);
		return check(row, col + 1, word, step);
	}

	// check left
	if ((col - 1) >= 0 && (board[row][col - 1] === word[step+1])) {
		console.log(word[step]);
		step++;
		markPath(row, col-1);
		return check(row, col - 1, word, step);
	}

	// check up
	if ((row - 1 >= 0) && (board[row - 1][col] === word[step+1])) {
		console.log(word[step]);
		step++;
		markPath(row-1, col);
		return check(row - 1, col, word, step);
	}

	// check down
	if ((row + 1 < board.length) && (board[row + 1][col] === word[step+1])) {
		console.log(word[step]);
		step++;
		markPath(row+1, col);
		return check(row + 1, col, word, step);
	}

	// all possible options exhausted
	return false;
}

function markPath (row, col) {
	board[row][col] = board[row][col].toLowerCase();
}

function isWordExists (word) {
	for (let i = 0;i < board.length; i++) {
		for (let j = 0;j < board[i].length; j++) {			
			if (board[i][j] === word[0]) {
				// first char matches, now check recursively
				markPath(i, j);
				let isFound = check(i, j, word, 0);
				if (isFound) {
					return true;
				} else {
					board = [ 
						['A','B','C','E'], 
						['S','F','C','S'], 
						['A','D','E','E'] 
					];
				}
			}
		}
	}
	return false;
}



console.log(isWordExists("ABCCED"));
console.log(isWordExists("SEE"));
console.log(isWordExists("ABCB"));