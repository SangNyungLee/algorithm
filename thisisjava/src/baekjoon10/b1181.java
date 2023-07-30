package baekjoon10;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class b1181 {
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int a = Integer.parseInt(br.readLine());
		int arr[] = new int [a]; // 단어수
		String arr2[] = new String[a]; // 단어
		for(int i=0; i<a ; i++) {
			String s = br.readLine();
			arr2[i] = s;
			arr[i] = s.length();
		}	
	}
}
