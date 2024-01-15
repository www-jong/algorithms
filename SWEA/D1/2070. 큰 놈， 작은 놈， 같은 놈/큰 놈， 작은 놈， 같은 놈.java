import java.io.IOException;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        sc.nextLine();
        for(int i=1;i<=T;i++){
            int a=sc.nextInt();
            int b=sc.nextInt();
            sc.nextLine();
            String r = "=";
            if(a<b){
                r="<";
            }else if(a>b){
                r=">";
            }
            System.out.printf("#%d %s\n",i,r);
        }
        }
    }

