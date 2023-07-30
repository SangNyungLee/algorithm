package Backjoon1;

import java.util.Scanner;

public class Main13 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		
		for(int i=1 ; i<=a ; i++) {
			for(int k=0 ; k<i ; k++) {
				System.out.print("*");
			}
			System.out.println(" ");
		}
	}

}
