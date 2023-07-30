package baekjoon7;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b2581 {
	public static void main(String [] args)throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int a = Integer.parseInt(br.readLine());
		int b = Integer.parseInt(br.readLine());

		int array = 0;
		int sum1 = 0;
		int sum2 =0;
		int arr[] = new int [b-a+1];
		for(int i = a; i<=b ; i++) {
			int cnt =0;
			for(int j=1 ; j<=i ; j++) {
				if(i%j == 0) {
					cnt+= 1;
				}
			}
			if(cnt == 2) {
				arr[array++] = i;
				sum2++;
			}
		}
		if(sum2 == 0) {
			System.out.println(-1);
	} else{
		for(int i =0; i<arr.length; i++) {
			if(arr[i] != 0) {
				sum1 += arr[i];
			}
		}
		System.out.println(sum1);
		System.out.println(arr[0]);
	}
	}
}
