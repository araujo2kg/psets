var removeDuplicates = function (nums) {
    let countIndex = 0;
    for (i = 0; i < nums.length; i++) {
        if (nums[i] != nums[i - 1]) {
            nums[countIndex] = nums[i];
            countIndex++;
        }
    }
    return countIndex;
};
