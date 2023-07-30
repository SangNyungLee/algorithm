package Backjoon2;

import java.util.Scanner;

public class b10818 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int arr1[] = new int[a];
		int max = -1000000;
		int min = 1000000;
		
		for(int i =0; i<a ; i++) {
			arr1[i] = sc.nextInt();
		}
		
		for(int j =0; j<a ; j++) {
			if(max < arr1[j]) {
				max = arr1[j];
			}
			if(min > arr1[j]) {
				min = arr1[j];
			}
		}
		System.out.println(min + " " + max);
	}
}
/* 최소, 최대값 다른 풀이 


public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int arr[] = new int[s.nextInt()];
		for(int i = 0; i < arr.length; i++) {
			arr[i] = s.nextInt();
		}
		int max = arr[0], min = arr[0];
		for(int i = 1; i < arr.length; i++) {
			if(arr[i] > max) {
			max = arr[i];
			}
			if(arr[i] < min) {
			min = arr[i];
			}
		}
		System.out.printf("%d %d", min, max);

	}
}
*/