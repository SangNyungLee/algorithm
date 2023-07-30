package baekjoon5;

import java.util.Scanner;

public class b10798 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
	
		char arr[][] = new char[5][15];
		int max =0;
		for(int i=0; i<5 ; i++) {
			String s = sc.next();
			max = Math.max(max, s.length()); //가장 긴 문자열 체크 후 max에 저장
			for(int j=0; j<s.length(); j++) {
				arr[i][j] = s.charAt(j);
			}
		}
		for(int i=0; i<max ; i++) {
			for(int j=0; j<5 ; j++) {
				if(arr[j][i] == '\0') {
					continue;
				} else {
					System.out.print(arr[j][i]);
				}
			}
		}
	}
}
