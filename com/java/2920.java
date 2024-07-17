import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int first = sc.nextInt();
        String cmd = "";
        if (first == 1){
            for (int i = 2; i < 8; i++) {
                int T = sc.nextInt();
                if (i != T) {
                    cmd = "mixed";
                    break;
                }
            }
            if (cmd != "mixed"){
                System.out.println("ascending");
            }else {
                System.out.println("mixed");
            }
        } else if (first == 8) {
            for (int i = 7; i > 0; i--) {
                int T = sc.nextInt();
                if (i != T) {
                    cmd = "mixed";
                    break;
                }
            }
            if (cmd != "mixed"){
                System.out.println("descending");
            }else {
                System.out.println("mixed");
            }
        } else {
            System.out.println("mixed");
        }

    }

}