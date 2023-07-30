package baekjoon10;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class b25305 {
	public static void main(String [] args)throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int a = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());
		
		int arr[] = new int[a];
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<a ; i++) {
			arr[i] = Integer.parseInt(st.nextToken())*-1;
			
		}
		Arrays.sort(arr);
		System.out.println(arr[b-1]*-1);
	}
}
