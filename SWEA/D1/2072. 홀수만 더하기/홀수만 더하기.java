import java.io.IOException;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        sc.nextLine();
        for (int i = 1; i <= T; i++) {
            int res = 0 ;
            for (int j =0; j<10;j++){
                int n = sc.nextInt();
                if(n%2!=0){
                    res+=n;
                }
            }
            System.out.printf("#%d %d\n", i, res);
            }
        }
    }
