package Backjoon2;

import java.util.Scanner;

public class b3052 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		int arr[] = new int[10];
		boolean bl;
		int sum =0;
		for(int i=0 ; i<10 ; i++) {
			arr[i] = sc.nextInt()%42;
		}
		
		for(int i=0; i<arr.length; i++) {
			bl = false;
			for(int k=i+1; k<arr.length ; k++) {
				if(arr[i] == arr[k]) {
					bl = true;
					break;
				}
			}
			if(bl == false) {
				sum++;
			}
		}
		System.out.println(sum);
	}
}