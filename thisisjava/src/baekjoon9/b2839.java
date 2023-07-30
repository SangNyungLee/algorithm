package baekjoon9;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class b2839 {
	public static void main(String [] args) throws IOException{
//		Scanner sc = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
//		int a = sc.nextInt();
		int a = Integer.parseInt(br.readLine());
		int sum = 2000;
		for(int i=0; i<=a/5 ; i++) {
			for(int j=0; j<=a/3 ; j++) {
				if(i+j <= sum && (5*i) + (3*j) == a) {
					sum = i+j;
				} 
			}
		}
		if(sum ==2000) {
			System.out.println("-1");
		} else {
			System.out.println(sum);
		}
	}
}
