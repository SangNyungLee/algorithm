package baekjoon4;

import java.util.Scanner;

public class b3003 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		int arr[] = new int[6];
		int arr2[] = {1, 1, 2, 2, 2, 8};
		int sum =0;
		for(int i=0; i<6 ; i++) {
			arr[i] = sc.nextInt();
			
			arr2[i] = arr2[i]-arr[i];
			
			System.out.print(arr2[i] +" ");
		}
	}
}
