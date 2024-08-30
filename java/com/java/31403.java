import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        System.out.println(a+b-c);

        String a_plus_b = String.join("",Arrays.asList(String.valueOf(a), String.valueOf(b)));
        System.out.println(Integer.parseInt(a_plus_b)-c);

    }

}