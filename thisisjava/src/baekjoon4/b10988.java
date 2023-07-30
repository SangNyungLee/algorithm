package baekjoon4;

import java.util.Scanner;

public class b10988 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = sc.next();
		String r = new StringBuffer(s).reverse().toString();
		
		if(s.equals(r)) {
			System.out.println("1");
		} else {
			System.out.println("0");
		}	
	}
}
