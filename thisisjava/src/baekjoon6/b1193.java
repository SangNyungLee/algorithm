package baekjoon6;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.nio.Buffer;

public class b1193 {
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int a = Integer.parseInt(br.readLine());
		int n = 0;
		for(int j=1 ; j<=a ; j++) {
			for(int i=1; i<=j ; i++) {
				n += 1;
				System.out.println("i :" + i + ", j :" + j + ", N : " +n);
			}
		}
	}

}
