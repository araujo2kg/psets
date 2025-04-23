var countStudents = function (students, sandwiches) {
    while (students.includes(sandwiches[0])) {
        if (students[0] === sandwiches[0]) {
            students.shift();
            sandwiches.shift();
            continue;
        }

        let student = students.shift();
        students.push(student);
    }
    return students.length;
};

var countStudents = function (students, sandwiches) {
    let studentCount = { 1: 0, 0: 0 };
    students.forEach((student) => studentCount[student]++);
    for (let i = 0; i < sandwiches.length; i++) {
        if (studentCount[sandwiches[i]] > 0) {
            studentCount[sandwiches[i]]--;
            continue;
        }
        break;
    }
    return studentCount["1"] + studentCount["0"];
};
