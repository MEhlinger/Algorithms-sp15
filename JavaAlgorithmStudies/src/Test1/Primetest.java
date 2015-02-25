package Test1;

/**
 *
 * @author Marshall Ehlinger
 */

// For take-home test 1
// Determine if integer n is prime, where n > ... in N^.5 time?!?
// Only use addition, subtraction, multiplication, mod, divison, and rounding

public class Primetest {
    public static void main (String[] args) {
        for (int i = 3; i < 105; i++) {
            if (isPrime(i)) {
                System.out.println(i + " is prime");
            } 
        }
    }
    
    public static boolean isPrime(int n) {
        if (n % 2 == 0) {
            return false;
        }
        if (n == 3) {
            return true;
        } 
        for (int j = 3; j < n; j++) {
            if (j * j == n) {
                return false;
            } else if (n % j == 0) {
                return false;
            }  
        }
        return true;
    }
}