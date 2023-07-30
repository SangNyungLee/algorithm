package baekjoon6;

import java.util.Scanner;

public class b2720 {
	public static void main(String []args) {
		Scanner sc = new Scanner(System.in);
		
		int arr[] = new int[4];		
		int a = sc.nextInt();	
		
		for(int i=0; i<a ; i++) {
			int b = sc.nextInt();
			int q = b/25;
			int d = (b%25)/10;
			int n = ((b%25)%10)/5;
			int p = ((b%25)%10)%5;
			
			System.out.println(q + " " + d + " " + n + " " + p);
		}
	}
}
