package baekjoon9;

import java.io.IOException;
import java.util.Scanner;

public class b2798 {
	public static void main(String [] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int sum =0;
		int tmp =0;
		
		int arr[] = new int[a];
		for(int i=0; i<a ; i++) {
			arr[i] = sc.nextInt();
		}

		for(int i=0; i<a; i++) {
			for(int j=i+1; j<a ; j++) {
				for(int k=j+1 ; k<a ; k++) {
					sum= arr[i]+arr[j]+arr[k];
					
					if(tmp < sum && sum <=b) {
						tmp = sum;
					}
				}
			}
		}
		System.out.println(tmp);
	}
}
