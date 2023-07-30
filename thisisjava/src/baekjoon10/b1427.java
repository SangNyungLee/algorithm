package baekjoon10;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class b1427 {
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int a = Integer.parseInt(br.readLine());
		int b = a;
		int i=0;
		
		while(a>0) {
			a = a/10;
			i++;
		}
		int arr[] = new int[i];
		for(int j=0 ; j<i ; j++) {
			arr[j] = (b%10)*-1;
			b = b/10;
		}
		Arrays.sort(arr);
		for(int j=0; j<arr.length ; j++) {
			System.out.print(arr[j]*-1);
		}
	}
}
