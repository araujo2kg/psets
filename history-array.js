/**
 * @param {string} homepage
 */
var BrowserHistory = function (homepage) {
    this.history = [homepage];
    this.current = 0;
    this.length = 1;
};

/**
 * @param {string} url
 * @return {void}
 */
BrowserHistory.prototype.visit = function (url) {
    this.current++;
    this.history[this.current] = url;
    this.length = this.current + 1;
};

/**
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.back = function (steps) {
    this.current = Math.max(0, this.current - steps);
    return this.history[this.current];
};

/**
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.forward = function (steps) {
    this.current = Math.min(this.length - 1, this.current + steps);
    return this.history[this.current];
};
