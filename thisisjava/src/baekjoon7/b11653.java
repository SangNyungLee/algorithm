package baekjoon7;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b11653 {
	public static void main(String []args)throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int a = Integer.parseInt(br.readLine());
		while(true) {
			if(a==1) break;
			for(int i=1 ; i<=a+i ; i++) {
				if(i>1 && a%i == 0) {
					a = a/i;
					System.out.println(i);
					break;
				}
			}
		}
	}
}
