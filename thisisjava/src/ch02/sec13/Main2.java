package ch02.sec13;

import java.util.Scanner;

public class Main2 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = (b%10);
		int d = (b%100);
		int result1 = a * c;
		int result2 = a * ((d-c)/10);
		int result3 = a * (b/100);
		int result4 = a*b;
		
		System.out.println(result1);
		System.out.println(result2);
		System.out.println(result3);
		System.out.println(result4);
	}

}
