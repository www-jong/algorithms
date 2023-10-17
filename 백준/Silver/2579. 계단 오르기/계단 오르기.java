import java.util.Scanner;

class Main{

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		int[] arr=new int[t+1];
		int[][] dp=new int[t+1][3]; // 2579번
		for(int i=1;i<=t;i++) {
			arr[i]=sc.nextInt();
		}
		dp[0][0]=dp[0][1]=0;
		dp[1][1]=dp[1][2]=arr[1];
		
		for(int i=2;i<=t;i++) {
			dp[i][2]=dp[i-1][1]+arr[i]; // 전에 계단을 1개의 연속으로밟고 또 연속일때,
			dp[i][1]=Math.max(dp[i-2][1],dp[i-2][2])+arr[i];
			
		}
		System.out.printf("%d",Math.max(dp[t][1],dp[t][2]));
		
		
	}

}
