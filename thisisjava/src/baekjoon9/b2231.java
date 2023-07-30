package baekjoon9;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b2231 {
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int a = Integer.parseInt(br.readLine());
		int b = a;
		int sum = 0;
		while(a>0) {
			sum += a%10;
			a = a/10;
		}
		System.out.println(b+sum);
	}

}
