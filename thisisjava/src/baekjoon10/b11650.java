package baekjoon10;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class b11650 {
	public static void main(String [] args)throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		int a = Integer.parseInt(br.readLine());
		int arr[] = new int[a];
		int arr2[] = new int[a];
		

		for(int i=0 ;i<a ; i++) {
			st = new StringTokenizer(br.readLine()," ");
			arr[i] = Integer.parseInt(st.nextToken());
			arr2[i] = Integer.parseInt(st.nextToken());
		}
		br.close();
		Arrays.sort(arr);
		Arrays.sort(arr2);
		
		for(int i=0; i<a ; i++) {
			System.out.println(arr[i] + " "+ arr2[i]);
		}
	}
}
