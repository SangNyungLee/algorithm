package Backjoon2;

import java.util.Scanner;

public class b1546 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		double arr[] = new double[a];
		double plus = 0;
		for(int i=0; i<arr.length; i++) {
			arr[i] = sc.nextInt();
		}
		
		double max = arr[0];
		for(int i=1; i<arr.length;i++) {
			if(arr[i]>max) {
				max = arr[i];
			}
		}
		for(int i=0 ; i<arr.length;i++) {
			arr[i] = arr[i]*100/max;
			plus += arr[i];
		}
		double sum = plus/(double)arr.length;
		System.out.println(sum);
	}
}
