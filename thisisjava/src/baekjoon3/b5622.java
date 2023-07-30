package baekjoon3;

import java.util.Scanner;

public class b5622 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = "WA";
		String[] str = {"ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"};
		
		int cnt =0;
		for(int i=0; i<8 ; i++) {
			for(int j=0 ;j< s.length(); j++) {
				if(str[i].indexOf(s.charAt(j))!= -1) {
					
					cnt += i + 3;
					System.out.print(cnt + " ");
				}
			}
		}
		System.out.println(cnt);
	}
}
