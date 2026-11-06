// Bug 2: Logical Error

function calculate_discount(price, discount) {
    let finalPrice = price + (price * discount / 100);
    return finalPrice;
}

function displayPrice(price, discount) {
    const result = calculate_discount(price, discount);

    console.log("Original price:", price);
    console.log("Discount:", discount + "%");
    console.log("Final price:", result);

    return result;
}

displayPrice(100, 20);
displayPrice(200, 10);
