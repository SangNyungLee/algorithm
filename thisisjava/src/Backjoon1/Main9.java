package Backjoon1;

import java.util.Scanner;

public class Main9 {
	public static void main(String []args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = a-1;
		
		for(int i=1 ; i<=a ; i++) {
			for(int k = b ; k>0 ; k--) {
				System.out.print(" ");
			}
			for(int j=i ; j>0 ; j--) {
				System.out.print("*");
			}
			System.out.println();
			b--;
		}
	}
}