package baekjoon3;

import java.util.Scanner;

public class b2675 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();	//테스트 케이스의 개수

		for(int i=0 ; i<a ; i++) {
			int k = sc.nextInt();	//테스트 케이스 반복횟수
			String s = sc.next();	// 문자열
			String arr[] = new String[s.length()];
			arr[0] = s;
			arr = s.split("");
			for(int j = 0 ; j <s.length(); j++) {
				for(int e=0; e<k; e++) {
					System.out.print(arr[j]);	
				}	
				}
			System.out.println("");
			}
		}
	}