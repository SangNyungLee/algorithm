package baekjoon4;

import java.util.Arrays;
import java.util.Scanner;

public class b4344 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();

		double arr2[] = new double[a];
		
		for(int i=0; i<a ; i++) {
			int b = sc.nextInt();
			int arr[] = new int[b]; 
			double avg =0;
			double sum2 =0 ;
			int sum =0;
			
			for(int j=0 ; j<b ; j++) {
				arr[j] = sc.nextInt();
				sum += arr[j];
			}
			avg = sum/b;
			
			for(int j =0 ; j<b ; j++) {
				if(avg<arr[j]) {
					sum2+=1;
				}
			}
			arr2[i] = (sum2*100/b);

		}
			for(int i=0; i<a ; i++) {
				System.out.println(String.format("%.3f%%", arr2[i]));
			}
	}
}

