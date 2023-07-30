package baekjoon6;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.text.ParseException;

public class b2292 {
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int a = Integer.parseInt(br.readLine());
		int b=1;
		for(int i=0; ; i++) {
			b += 6*i;
			if(a<=b) {
				b = i+1;
				break;
			} else if(a==1){
				break;
			}
		}
		System.out.println(b);
	}
}
