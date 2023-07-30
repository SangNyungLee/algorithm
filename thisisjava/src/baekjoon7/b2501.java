package baekjoon7;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class b2501 {
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] arr2 = br.readLine().split(" ");
		int a = Integer.parseInt(arr2[0]);
		int b = Integer.parseInt(arr2[1]);

		int arr[] = new int[a+1];
		int count =0;
		for(int i=1; i<=a ; i++) {
			if(a%i == 0) {
				arr[i] = a/i;
				
			} else {
				count++;
			}
		}
		Arrays.sort(arr);
		if((a-count)>=b) {
			System.out.println((arr[b+count]));
		} else {
			System.out.println("0");
		}
		br.close();
	}
}
