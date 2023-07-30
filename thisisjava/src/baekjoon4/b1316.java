package baekjoon4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b1316 {
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int a = Integer.parseInt(br.readLine());

		
		int cnt = a;
		
		for(int roop =0 ; roop<a ; roop++) {
			String st = br.readLine();

			boolean test[] = new boolean[26];
			
			for(int i=0; i<st.length()-1; i++) {
				if(st.charAt(i)!=st.charAt(i+1)) {
					if(test[st.charAt(i+1)-97] == true) {
						cnt--;
						break;
					}
				}
				test[st.charAt(i)-97] = true;
			}
		}
		System.out.println(cnt);
		br.close();
	}
}
