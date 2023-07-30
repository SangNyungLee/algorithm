package Backjoon1;

import java.util.Scanner;

public class Main6 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		int a =sc.nextInt();
		
		for(int i =0; i<a ; i++) {
			if(i%4==0) {
			System.out.print("long ");
			}
		}
		System.out.print("int");
	}

}
