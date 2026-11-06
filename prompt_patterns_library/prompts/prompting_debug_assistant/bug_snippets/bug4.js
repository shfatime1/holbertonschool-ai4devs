// Bug 4: Off-by-One Error

function printNumbers(numbers) {
    for (let i = 0; i <= numbers.length; i++) {
        console.log(numbers[i]);
    }
}

function calculateTotal(numbers) {
    let total = 0;

    for (let i = 0; i <= numbers.length; i++) {
        total += numbers[i];
    }

    return total;
}

const values = [10, 20, 30, 40];

printNumbers(values);
console.log("Total:", calculateTotal(values));
