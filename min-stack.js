var MinStack = function () {
    this.stack = [];
    this.minStack = [];
};

/**
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function (val) {
    if (
        this.minStack.length === 0 ||
        this.minStack[this.minStack.length - 1] > val ||
        this.minStack[this.minStack.length - 1] == val
    )
        this.minStack.push(val);
    this.stack.push(val);
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function () {
    if (
        this.stack[this.stack.length - 1] ==
        this.minStack[this.minStack.length - 1]
    )
        this.minStack.pop();
    this.stack.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function () {
    return this.stack[this.stack.length - 1];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function () {
    return this.minStack[this.minStack.length - 1];
};
