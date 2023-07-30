package baekjoon6;

import java.util.Scanner;

public class b11005 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();	//값
		int b = sc.nextInt();	//변환값
		if(b==2){
			System.out.println(Integer.toBinaryString(a).toUpperCase());	
		}
		else if(b==8){
			System.out.println(Integer.toOctalString(a).toUpperCase());
		}
		else if(b==16) {
			System.out.println(Integer.toHexString(a).toUpperCase());
		} else {
			System.out.println(Integer.toString(a, b).toUpperCase());
		}
	}
}
