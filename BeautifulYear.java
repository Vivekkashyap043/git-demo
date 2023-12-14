import java.util.Scanner;

public class BeautifulYear {

    public static boolean hasDistinctDigits(int year) {
        // Check if the year has distinct digits
        int[] digitCount = new int[10];

        while (year > 0) {
            int digit = year % 10;
            if (digitCount[digit] > 0) {
                return false;
            }
            digitCount[digit]++;
            year /= 10;
        }

        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int y = scanner.nextInt();

        while (true) {
            y++;
            if (hasDistinctDigits(y)) {
                System.out.println(y);
                break;
            }
        }

        scanner.close();
    }
}
