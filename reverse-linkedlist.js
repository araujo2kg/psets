var reverseList = function (head) {
    if (head === null) return null;

    let current = head;
    let previous = null;
    while (current != null) {
        let next = current.next;
        current.next = previous;
        previous = current;
        current = next;
    }

    return previous;
};
