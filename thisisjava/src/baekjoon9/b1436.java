package baekjoon9;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b1436 {
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int a = Integer.parseInt(br.readLine());
		
		int number = 666;
		int cnt = 1;
		
		while(cnt != a) {
			number++;
			if(String.valueOf(number).contains("666")){
				cnt++;
			}
		}
		System.out.println(number);
	}

}
