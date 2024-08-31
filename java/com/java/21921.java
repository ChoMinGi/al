import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int X = sc.nextInt();

        int[] visit = new int[N];
        for (int i=0;i<N;i++){
            visit[i] = sc.nextInt();
        }
        
        int cnt = 0;
        int maxVisit = 0;
        int sumVisit = 0;

        // 초기 합계 계산 (첫 X개의 합)
        for (int i = 0; i < X; i++) {
            sumVisit += visit[i];
        }
        maxVisit = sumVisit;
        cnt = 1;

        for (int i = 1; i < N-X+1; i++) {
            sumVisit = sumVisit - visit[i-1] + visit[i+X-1];
            
            if(sumVisit==maxVisit){
                cnt++;
            } else if(sumVisit>maxVisit){
                maxVisit=sumVisit;
                cnt = 1;
            }
        }

        if (maxVisit == 0){
            System.out.println("SAD");
        } else {
            System.out.println(maxVisit);
            System.out.println(cnt);
        }

    }

}