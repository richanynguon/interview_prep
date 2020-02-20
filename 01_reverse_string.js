function reverse(str) {
	return str
		.split("") // o(N)
		.reverse() // TC: O(N), SC:O(1)
		.join(""); // o(N)
}
// time complexity: o(N)
// space complexity: o(n) + o(n) + o(1)

let reverseArray = arr => {
	for (let i = 0; i < arr.length / 2; i++) {
		[arr[i], arr[arr.length - i - 1]] = [arr[arr.length - i - 1], arr[i]];
	}

	return arr;
};
console.log(reverseArray([1,2,3,4,5]))
// Time complexity: O(n).
// Space complexity: O(1).

function reverse2(str) {
	let reverse = "";
	for (let character of str) {
		reversed = character + reversed;
	}
	return reverse;
}
// Time complexity: O(n).
// Space complexity: O(n).