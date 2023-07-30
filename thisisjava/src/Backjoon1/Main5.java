package Backjoon1;

import java.util.Scanner;

public class Main5 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int sum = 0;
		
		for(int i = 0; i<b ; i++) {
			int c = sc.nextInt();
			int d = sc.nextInt();
			sum += c*d;
		}
		if(a == sum) {
			System.out.println("Yes");
		}
		else {
			System.out.println("No");
		}
	}

}
