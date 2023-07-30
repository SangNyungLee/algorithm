package Backjoon2;

import java.util.Scanner;

public class b5597 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		int arr[] = new int[28];
		int arr1[] = new int[30];
		for(int i =0 ; i<28 ; i++) {
			arr[i] = sc.nextInt();
		}
		for(int i = 0 ; i<30 ; i++) {
			for(int j =0; j<28 ; j++) {
				if(arr[j] == i+1) {
					arr1[i] = 1;
					break;
				}
				else {
					arr1[i] = 0;
				}
			}
		}
		for(int i = 0 ; i<30 ; i++) {
			if(arr1[i] == 0) {
				System.out.println(i+1);
			}
		}
	}
}
