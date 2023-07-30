package Backjoon1;

import java.util.*;

public class Main1 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
			
			int a = sc.nextInt();
			for(int n = 1 ; n<=9 ; n++) {
				System.out.println(a + " * " + n + " = " +(a*n));
			}
	}
}
