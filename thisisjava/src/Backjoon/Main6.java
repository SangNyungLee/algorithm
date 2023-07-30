package Backjoon;

import java.util.Scanner;

public class Main6 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int d = b+c;
		int e = (d/60) + a;
		if(e >= 24) {
			System.out.print(e-24);
			System.out.print(" " +d%60);
		}
		else if(e < 24) {
			System.out.print(a+(d/60));
			System.out.println(" "+ d%60);
		}	
	}
}
