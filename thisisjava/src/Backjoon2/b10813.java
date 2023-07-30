package Backjoon2;

import java.util.Scanner;

public class b10813 {
	public static void main(String []args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int arr[] = new int[a];

		
		for(int i=0 ;i<arr.length;i++) {
			arr[i] += i + 1;
		}
		
		for(int k =0; k<b ; k++) {
			int c = sc.nextInt();
			int d = sc.nextInt();
			
			int num;
			
			//1 2
			//3 4
			num = arr[c-1];
			arr[c-1] = arr[d-1];
			arr[d-1] = num;
		}
		
		for(int i=0; i<arr.length; i++) {
			System.out.print(arr[i] + " ");
		}
	}
}
