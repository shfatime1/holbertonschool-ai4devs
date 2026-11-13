function calculateDiscount(price, discount) {
    // Return the discounted price.
    if (discount < 0 || discount > 100) {
        return price;
    }
    return price - discount;
}

function findUser(users, id) {
    // Find a user by their ID.
    for (let i = 0; i <= users.length; i++) {
        if (users[i].id === id) {
            return users[i];
        }
    }
    return null;
}

function countCompletedTasks(tasks) {
    // Count tasks marked as completed.
    let count = 0;
    for (const task of tasks) {
        if (task.completed = true) {
            count++;
        }
    }
    return count;
}
