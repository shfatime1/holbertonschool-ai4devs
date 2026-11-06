public class Bug5 {
    public static int calculateTotal(String[] prices) {
        int total = 0;

        for (String price : prices) {
            total += Integer.parseInt(price);
        }

        return total;
    }

    public static void main(String[] args) {
        String[] prices = {"10", "20", "30"};

        int result = calculateTotal(prices);

        System.out.println("Total price: " + result);

        assert result == 60;
        assert calculateTotal(new String[]{"5", "15"}) == 20;
        assert calculateTotal(new String[]{}) == 0;
    }
}
