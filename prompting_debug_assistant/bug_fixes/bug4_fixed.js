function printNumbers(numbers) {
    for (let i = 0; i < numbers.length; i++) {
        console.log(numbers[i]);
    }
}

function calculateTotal(numbers) {
    let total = 0;

    for (let i = 0; i < numbers.length; i++) {
        total += numbers[i];
    }

    return total;
}

const values = [10, 20, 30, 40];

printNumbers(values);

const result = calculateTotal(values);
console.log("Total:", result);

console.assert(result === 100);
console.assert(calculateTotal([5, 10, 15]) === 30);
console.assert(calculateTotal([]) === 0);
