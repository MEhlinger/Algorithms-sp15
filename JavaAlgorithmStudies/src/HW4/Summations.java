package HW4;

/**
 * For Design and Analysis of Algorithms, chapter 2.3 exercises
 *  as well as practice and enrichment and all that good stuff.
 * 
 * @author Marshall Ehlinger
 */
public class Summations {
    public static void main (String[] args) {
        //MAIN METHOD-- tests
        
        // sumPrimes test:
        //System.out.println(sumPrimes(0, 999));
        
        // Sum every other number test
        //System.out.println(everyOtherSum(1, 999));
        
        // Sum 2^i test
        //System.out.println(exponentialSum(2, 1024));

    }

    public static int sumPrimes(int min, int max) {
        int primeSum = 0;
        
        for (int i = min; i < max; i ++) {
            if (isPrime(i)) {
                primeSum += i;
            }
        } 
        return primeSum;
	}

    public static boolean isPrime (int val) {
        // Method determines if given value is a prime
        // Even values are never prime
        if (val % 2 == 0 && val != 2) {
                return false;
        }
        // Check all odd values up to square root of val
        for (int i = 3; i < Math.sqrt(val); i += 2) {
                if (val % i == 0) {
                        return false;
                }
        }

        // If no odd value less than the square root of val 
        return true;
    }
    
    public static int everyOtherSum(int min, int max) {
        int sum = 0; // Below loop does not work with 1, but true min is 1
        for (int i = min; i <= max; i += 2) {
            sum += i;
        }
        return sum;
    }
    
    public static int exponentialSum(int base, int maxVal) {
        int sum = 0;
        int i = 0;
        int value = 0;       
        
        while (value < maxVal) {
            i ++;
            value = (int) Math.pow(base, i); 
            sum += value;      
        }
        
        return sum;
    }
}
