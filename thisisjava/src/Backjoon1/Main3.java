package Backjoon1;

import java.util.Scanner;

public class Main3 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int sum = 0;
		
		for(int i=0 ; i<=a; i++ ) {
			sum +=i;
		}
		System.out.println(sum);
	}

}
