package Backjoon1;

import java.util.Scanner;

public class Main8 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int[] p = new int[a];
		
		for(int i =0 ; i<a ; i++) {
			int b = sc.nextInt();
			int c = sc.nextInt();
			int sum = b+c;
			System.out.println("Case #"+ (i+1) + ": "+ b +" + " + c +" = "  + sum);
			
		}
	}
}
