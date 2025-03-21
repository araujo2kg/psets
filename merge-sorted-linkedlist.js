var mergeTwoLists = function (list1, list2) {
    if (list1 === null) return list2;
    if (list2 === null) return list1;

    let newHead = list1.val <= list2.val ? list1 : list2;
    let tail = newHead;
    while (list1 !== null && list2 !== null) {
        if (list1.val <= list2.val) {
            let temp = list1;
            list1 = list1.next;
            tail.next = temp;
            tail = temp;
        } else {
            let temp = list2;
            list2 = list2.next;
            tail.next = temp;
            tail = temp;
        }
    }

    if (list1 !== null) tail.next = list1;
    if (list2 !== null) tail.next = list2;

    return newHead;
};
