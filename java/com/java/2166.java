import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        ArrayList<int[]> poly = new ArrayList<>();
        for (int i=0;i<N;i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            poly.add(new int[]{x,y});
        }
        
        poly.add(poly.get(0));

        double res = 0.0;
        for (int i = 0; i < N; i++) {
            res += (poly.get(i)[0] * poly.get(i + 1)[1]) - (poly.get(i + 1)[0] * poly.get(i)[1]);
        }

        System.out.println(String.format("%.1f", Math.abs(res * 0.5)));

    }

}