package Backjoon2;

import java.util.Scanner;

public class b10811 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int arr[] = new int[a];
		
		for(int i=0; i<a ; i++) {
			arr[i] = i+1;
		}
		
		for(int e=0; e<a ; e++) {
			int i = sc.nextInt();
			int j = sc.nextInt();
			
			int num = 0;
			int num1 = 0;
			
			int[] arr1 = new int[j - i + 1];
			
			for(int k=0; k<j -i+1; k++) {
				arr1[k] = arr[j-1-num];
				num++;
			}
			
			for(int l = i-1 ; l< j ; l++) {
				arr[l] = arr1[num1];
				num1++;
			}
		}
		
		for(int x =0; x<a; x++) {
			System.out.println(arr[x] + " ");
		}
	}

}
