import java.util.Scanner;

class Main {
	public static void main(String[] args) throws Exception {
			Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int a=1;
		int b=0;
		int aa=0;
		int bb=0;
		for(int i=0;i<n;i++) {
		aa=b;
		bb=b+a;
		a=aa;
		b=bb;
		}
		System.out.println(a+" "+b);
		
	}

}
