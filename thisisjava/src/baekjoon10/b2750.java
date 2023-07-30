package baekjoon10;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class b2750 {
	public static void main(String [] args)throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int a = Integer.parseInt(br.readLine());
		int arr[] = new int[a];
		for(int i=0 ; i<a ; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		
		Arrays.sort(arr);
		for(int i=0; i<a ; i++) {
			bw.write(arr[i]+"\n");
		}
		br.close();
		bw.flush();
	}
}
