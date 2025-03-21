function Node(val, next = null, prev = null) {
    return { val, next, prev };
}

var MyLinkedList = function () {
    this.head = null;
    this.tail = null;
    this.length = 0;
};

/**
 * @param {number} index
 * @return {number}
 */
MyLinkedList.prototype.get = function (index) {
    if (index >= this.length || index < 0) return -1;
    let currentNode = this.head;
    for (let i = 0; i <= index; i++) {
        if (i === index) return currentNode.val;
        currentNode = currentNode.next;
    }
};

/**
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtHead = function (val) {
    let newNode = Node(val, this.head, null);

    if (this.head !== null) {
        this.head.prev = newNode;
    } else {
        // If the list is empty, this node became the tail too.
        this.tail = newNode;
    }
    this.head = newNode;
    this.length++;
};

/**
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtTail = function (val) {
    let newNode = Node(val, null, this.tail);
    if (this.tail !== null) {
        this.tail.next = newNode;
    } else {
        // If tail is null, list is empty, so this is the head too
        this.head = newNode;
    }
    this.tail = newNode;
    this.length++;
};

/**
 * @param {number} index
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtIndex = function (index, val) {
    if (index > this.length) return null;
    if (index === this.length) {
        this.addAtTail(val);
        return null;
    }

    let node = this.head;
    for (let i = 0; i <= index; i++) {
        if (i === index) {
            let previous = node.prev;
            let newNode = Node(val, node, previous);
            if (previous !== null) previous.next = newNode;
            node.prev = newNode;
            if (index === 0) this.head = newNode;
        }

        node = node.next;
    }

    this.length++;
};

/**
 * @param {number} index
 * @return {void}
 */
MyLinkedList.prototype.deleteAtIndex = function (index) {
    if (index < 0 || index >= this.length) return null;

    let target = this.head;
    for (let i = 0; i <= index; i++) {
        if (i === index) {
            let previous = target.prev;
            let next = target.next;
            if (previous !== null) previous.next = next;
            if (next !== null) next.prev = previous;

            if (index === 0) this.head = next;
            if (index === this.length - 1) this.tail = previous;
        }

        target = target.next;
    }

    this.length--;
};
