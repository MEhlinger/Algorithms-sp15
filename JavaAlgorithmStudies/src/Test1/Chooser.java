package Test1;

/**
 *
 * @author Marshall Ehlinger
 */
public class Chooser {
    public static void main (String[] args) {
        // Gets rough efficiency in number of recursive calls of algorithm "choose"
        profile(25);
        profile(28);
        profile(35);
        
    }
    
    public static int choose (int n, int k, int[] count) {
        count[0] ++;
        if (k == 0) { return 1; }
        if (k == 1) { return n; }
        if (k == (n-1)) {return n; }
        if (k == n) {return n; }
        return choose(n-1, k-1, count) + choose(n-1, k, count);
    }
    
    public static void profile (int n) {
        // Tests efficiency of recursive algorithms
        int[] count = new int[1];
        count[0] = 0;
        for (int i = n; i > 0; i--) {
            choose(n, i, count);
            System.out.println("Count for n= " + n + ", k= " + i + " : " + count[0]);
            count[0] = 0;
        }
        System.out.print("\n\n");
    }
}
