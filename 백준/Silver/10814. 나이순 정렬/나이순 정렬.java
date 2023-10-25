import java.io.*;
import java.util.*;
import java.lang.Math;
class Main {
	static public void main(String []args) throws IOException{
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        Object[][] li = new Object[N][3];
        for(int i=0;i<N;i++){
            st=new StringTokenizer(br.readLine());
            int age = Integer.parseInt(st.nextToken());
            String name = st.nextToken();
            li[i][0]=age;
            li[i][1]=name;
            li[i][2]=i;
        }
        Arrays.sort(li,(a,b)->
            a[0]==b[0]?(int)a[2]-(int)b[2]:(int)a[0]-(int)b[0]);
        for(int i=0;i<N;i++){
            bw.write(Integer.toString((int)li[i][0])+" "+li[i][1]+"\n");
        }
        bw.flush();
        bw.close();
    }
}