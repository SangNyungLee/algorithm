package baekjoon6;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class b2903 {
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int a = Integer.parseInt(br.readLine());
		int b = 1;
		int d = 0;
		for(int i=0;i<a ; i++) {
			int c = b*2;
			b = c;
			d = (c+1)*(c+1);

		}
		System.out.println(d);
	}
}
