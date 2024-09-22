import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    static int m,n;
    static int[][] res;
    static int[][] mapList;
    
    static int[][] around = {{1, 0}, {-1, 0}, {0, -1}, {0, 1}};

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        
        res = new int[m][n];
        for (int[] row: res){
            Arrays.fill(row, -1);
        }

        mapList = new int[m][n];

        for (int i = 0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            for (int j=0;j<n;j++){
                mapList[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        System.out.println(dfs(0,0));

    }

    public static int dfs(int y, int x ){
        if (y==m-1 && x==n-1){
            return 1;
        }

        if (res[y][x] != -1){
            return res[y][x];
        }

        res[y][x] = 0;

        for (int[] td : around){
            int ny = y + td[0];
            int nx = x + td[1];

            if (0<=nx && nx<n && 0<=ny && ny<m) {
                if (mapList[y][x] > mapList[ny][nx]){
                    res[y][x] += dfs(ny, nx);
                }
            }

        }

        return res[y][x];
    }

}