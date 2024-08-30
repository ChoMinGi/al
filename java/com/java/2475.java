import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int res = 0;
        for (int i = 0; i < 5; i++) {
            int T = sc.nextInt();
            res = res + T*T;
        }
        res = res%10;

        System.out.println(res);
    }

}