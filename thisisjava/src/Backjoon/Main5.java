package Backjoon;

import java.util.Scanner;

public class Main5 {
	public static void main(String []args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = 45-b;
		int d = b-45;
		int e = 60+d;
	
		
		if(a>0 && b<45) {
			System.out.print(a-1);
			System.out.print(" " + e);
		}
		else if(a>0 && b>=45) {
			System.out.print(a);
			System.out.print(" " + d);
		}
		else if(a==0 && b>=45) {
			System.out.print(a);
			System.out.print(" " + d);
		}
		else if(a==0 && b<45) {
			System.out.print(a+23);
			System.out.print(" " + e);
		}
	}
}