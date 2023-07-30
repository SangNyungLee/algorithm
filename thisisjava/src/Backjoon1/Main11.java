package Backjoon1;

import java.util.Scanner;

public class Main11 {
	public static void main(String []args) {
		Scanner sc = new Scanner(System.in);
		
		boolean ab = true;
		
		while(ab) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			if(a>0 && b>0) {
				System.out.println(a+b);
			} else if(a==0 && b==0) {
				ab = false;
			}
		}
	}
}
 