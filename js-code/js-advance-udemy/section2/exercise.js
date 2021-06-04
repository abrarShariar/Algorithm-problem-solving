const list = new Array(60000).join('1.1').split('.');
 
function removeItemsFromList(list) {
	while (list.pop()) {
		removeItemsFromList(list);
	}

	return;
};
 
removeItemsFromList(list);