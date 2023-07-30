package baekjoon5;

import java.util.Scanner;

public class b2563 { 
	public static void main(String []args) {
		Scanner sc = new Scanner(System.in);
		
		int arr[][] = new int[100][100];
		int a = sc.nextInt();
		int cnt = 0;
		
		for(int i=0; i<a ; i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			for(int j=x; j<x+10 ; j++) {
				for(int k=y; k<y + 10; k++) {
					if(arr[j][k] == 1) 
						continue;
						arr[j][k] = 1;
						++cnt;
				}
			}
		}
		System.out.println(cnt);
	}
}