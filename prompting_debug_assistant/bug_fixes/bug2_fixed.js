
function calculate_discount(price, discount) {
    let finalPrice = price - (price * discount / 100);
    return finalPrice;
}

function displayPrice(price, discount) {
    const result = calculate_discount(price, discount);

    console.log("Original price:", price);
    console.log("Discount:", discount + "%");
    console.log("Final price:", result);

    return result;
}

console.assert(calculate_discount(100, 20) === 80);
console.assert(calculate_discount(200, 10) === 180);

displayPrice(100, 20);
displayPrice(200, 10);
