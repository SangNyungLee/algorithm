package Backjoon2;

import java.util.Scanner;

public class Main {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int[] arr1 = new int[a];
		int i = 0;
		for(i = 0 ; i<a ; i++) {
			arr1[i] = sc.nextInt();
		}
		int b = sc.nextInt();
		int c = 0;
		
		for(int j = 0 ; j<i ; j++) {
			if(arr1[j] == b) {
				c += 1;
			}
		}
		System.out.println(c);
	}

}
