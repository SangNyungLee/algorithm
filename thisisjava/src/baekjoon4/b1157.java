package baekjoon4;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class b1157 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = sc.next();
		char[] arr3 = s.toCharArray();
		int arr[] = new int[26]; // 대문자
		int arr2[] = new int[26]; // 소문자
		int arr4[] = new int[26]; // 대문자 합
		int arr5[] = new int[26]; // 소문자 합
		int arr6[] = new int[26]; // 둘다 합친거
		
		
		for(int i=0; i<arr.length ; i++) {		//소문자 집어넣기
			arr[i] = (char)('a'+i);
		}
		for(int i=0; i<arr2.length ; i++) {		//대문자 집어넣기
			arr2[i] = (char)('A'+i);
		}
		
		for(int i=0 ; i<26 ; i++) {
			for(int j=0; j<s.length(); j++) {
				if(arr[i] == arr3[j]) {
					arr4[i] += 1;
				} else {
					arr4[i] += 0;
				}
			}
		}
		for(int i=0 ; i<26 ; i++) {
			for(int j=0; j<s.length(); j++) {
				if(arr2[i] == arr3[j]) {
					arr5[i] += 1;
				} else {
					arr5[i] += 0;
				}
			}
		}
		int num =0;
		int num1 = 0;
		int numj= 0;
		for(int i=0; i<26 ; i++) {
			arr6[i] = arr4[i] + arr5[i];
		}
		
		loop:
		for(int i=s.length(); i>0; i--) {		//최대값 개수 확인
			for(int j=0; j<26; j++) {
				if(arr6[j] == i) {
					num =i;		//num = 최대값 개수
					numj = j;
					break loop;
				} else {
					continue;
				}
			}
		}
		for(int i=0; i<26; i++) {
			if(arr6[i] == num) {
				num1 += 1;
			} else {
				continue;
			}
		}
		if(num1 >=2) {
			System.out.println("?");
		} else {
			System.out.println((char)arr2[numj]);
		}
	}
}
