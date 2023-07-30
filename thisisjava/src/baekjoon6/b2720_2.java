package baekjoon6;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class b2720_2 {
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int a = Integer.parseInt(br.readLine());
		//q,d,n,p
		for(int i=0; i<a ; i++) {
			int b = Integer.parseInt(br.readLine());
			
			int q = b/25;
			int d = (b%25)/10;
			int n = ((b%25)%10)/5;
			int p = ((b%25)%10)%5;
			
			bw.write(q + " " + d +" " + n + " " +p + "\n");
		}
		br.close();
		bw.flush();
	}
}
