import java.util.*;


public class 4779 {
    static String[] dp = new String[13];

    public static String cantour(int n ){
        if (dp[n]!=null){
            return dp[n];
        }
        String prev = cantour(n-1);
        dp[n] = prev+" ".repeat(prev.length())+prev;
        return dp[n];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println(sc);

        dp[0] = "-";

        while (sc.hasNextInt()) {
            int n = sc.nextInt();
            System.out.println(cantour(n));
        }
    }
}