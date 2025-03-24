class Node {
    constructor(val, next = null, prev = null) {
        this.val = val;
        this.next = next;
        this.prev = prev;
    }
}
/**
 * @param {string} homepage
 */
var BrowserHistory = function (homepage) {
    this.homepage = new Node(homepage);
    this.current = this.homepage;
};

/**
 * @param {string} url
 * @return {void}
 */
BrowserHistory.prototype.visit = function (url) {
    let newPage = new Node(url, null, this.current);
    if (this.current.next !== null) this.current.next.prev = null;
    this.current.next = newPage;
    this.current = newPage;
};

/**
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.back = function (steps) {
    let newCurrent = this.current;
    while (newCurrent.prev !== null && steps > 0) {
        steps--;
        newCurrent = newCurrent.prev;
    }
    this.current = newCurrent;
    return this.current.val;
};

/**
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.forward = function (steps) {
    let newCurrent = this.current;
    while (newCurrent.next !== null && steps > 0) {
        steps--;
        newCurrent = newCurrent.next;
    }
    this.current = newCurrent;
    return this.current.val;
};
