package baekjoon7;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class b9506 {
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		while(true) {
			int a = Integer.parseInt(br.readLine());
			if(a == -1) {
				break;
			}
			int arr [] = new int [a];
			int num = 1;
			int count = 0;
			 for(int i=1 ; i<a ; i++) {
				if(a%i == 0) {
					arr[num++] = i;
					count += i;
				}
			}

			if(a== count) {
//				System.out.print(a +" = ");
				bw.write(a +" = ");
				for(int i=1 ; i<num ; i++) {
					if(i == num-1) {
//						System.out.println(arr[i]);
						bw.write(arr[i] +"\n");
					} else {
//						System.out.print(arr[i] + " + ");
						bw.write(arr[i]+" + ");
					}
				}
			} else {
//				System.out.println(a + " is Not perfect");
				bw.write(a +" is NOT perfect." + "\n");
			}
		}
		br.close();
		bw.flush();
	}
}
