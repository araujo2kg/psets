var isValid = function (s) {
    if (s.length % 2 != 0) return false;
    if (s[0] == ")" || s[0] == "}" || s[0] == "]") return false;
    if (
        s[s.length - 1] == "(" ||
        s[s.length - 1] == "{" ||
        s[s.length - 1] == "["
    )
        return false;

    let current = [];
    const relation = {
        "(": ")",
        "{": "}",
        "[": "]",
    };

    for (let i = 0; i < s.length; i++) {
        if (s[i] == "(" || s[i] == "{" || s[i] == "[") {
            current.push(s[i]);
        } else {
            if (relation[current[current.length - 1]] != s[i]) return false;
            current.pop();
        }
    }

    return current.length == 0;
};
