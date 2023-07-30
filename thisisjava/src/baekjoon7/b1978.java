package baekjoon7;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class b1978 {
	public static void main(String []args)throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int a = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		int arr [] = new int [a];
		int sum = 0;
		

		for(int i =0 ; i<a ; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		for(int i =0; i<arr.length ; i++) {
			int cnt = 0;
			for(int j=1 ; j<=arr[i]; j++) {
				if(arr[i]%j == 0) {
					cnt ++;
				}
			}
			arr[i] = cnt;
		}
		for(int i=0; i<a ; i++) {
			if(arr[i] ==2) {
				sum++;
			}
		}
		System.out.println(sum);
		br.close();
	}
}
