package Backjoon1;

import java.util.Scanner;

public class Main4 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int[] names = new int[a];
		
		for(int i = 0; i<a; i++) {
			int b = sc.nextInt();
			int c = sc.nextInt();
			
			names[i] = a + b;
			
		}
		for(int i = 0; i<names.length; i++) {
			System.out.println(names[i]);
		}
	}

}
