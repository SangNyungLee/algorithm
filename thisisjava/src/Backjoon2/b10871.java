package Backjoon2;

import java.util.Scanner;

public class b10871 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int i;
		int arr1[] = new int[a];
		
		for(i = 0; i<a ; i++) {
			arr1[i] = sc.nextInt();
			
			if(arr1[i] < b) {
				System.out.print(arr1[i]+ " ");
		}
		}
	}

}
