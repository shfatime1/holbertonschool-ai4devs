// Bug 5: Data Type Misuse

public class Bug5 {

    public static int calculateTotal(String[] prices) {
        int total = 0;

        for (String price : prices) {
            total += price;
        }

        return total;
    }

    public static void main(String[] args) {

        String[] prices = {"10", "20", "30"};

        int result = calculateTotal(prices);

        System.out.println("Total price: " + result);
    }
}
