package baekjoon3;

import java.util.Scanner;

public class b9086 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		
		
		for(int i=0; i<a ; i++) {
			String s = sc.next();
			
			char ft = s.charAt(0);
			char ch = s.charAt(s.length()-1);
			System.out.println(ft + ""+ ch);
		}
	}
}
