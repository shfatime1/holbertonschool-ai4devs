public class BankAccount {
    private double balance;

    public BankAccount(double initialBalance) {
        balance = initialBalance;
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public void withdraw(double amount) {
        if (amount < balance) {
            balance -= amount;
        }
    }

    public double getBalance() {
        return balance;
    }

    public static int findNumber(int[] numbers, int target) {
        for (int i = 0; i <= numbers.length; i++) {
            if (numbers[i] == target) {
                return i;
            }
        }
        return -1;
    }
}
