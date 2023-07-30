package baekjoon5;

import java.util.Scanner;

public class b2566 {
	public static void main(String []args) {
		Scanner sc = new Scanner(System.in);
		
		int arr[][] = new int [9][9];
		int max = -1;
		int num = 0;
		int num2 = 0;
		for(int i=0; i<9 ; i++) {
			for(int j=0 ;j<9 ; j++) {
				arr[i][j] = sc.nextInt();
			}
		}
		for(int i=0; i<9 ; i++) {
			for(int j=0 ;j<9 ; j++) {
				if(arr[i][j] > max) {
					max = arr[i][j];
					num = i+1;
					num2 = j+1;
				}
			}
		}
		System.out.println(max);
		System.out.println(num + " "+ num2);
	}
}
