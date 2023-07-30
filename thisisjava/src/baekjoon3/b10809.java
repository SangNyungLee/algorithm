package baekjoon3;

import java.util.Scanner;

public class b10809 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = sc.nextLine();
		String a = "abcdefghijklmnopqrstuvwxyz";
		String arr[] = new String[s.length()];	//입력값 저장
		String arr2[] = new String[a.length()];	//알파벳 저장
		int arr3[] = new int[26];
		arr = s.split("");
		arr2 = a.split("");
		
		for(int i=0; i<26 ; i++) {
			arr3[i] = -1;
		}
	
		for(int i=0; i<26 ; i++) {					//알파벳 순서대로
			for(int j=0; j<s.length(); j++) {		//입력값
				 if(arr2[i].equals(arr[j])) {
					 arr3[i] = j; 
					 break;
				 } else{
					 continue;
					 }
				 }
			System.out.print(arr3[i]+" ");
			}
		}
	}