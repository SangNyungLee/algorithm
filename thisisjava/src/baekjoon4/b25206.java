package baekjoon4;

import java.util.Scanner;

public class b25206 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		String arr[] = new String [61];
		
		double num = 0;
		double num1 = 0;
		
		for(int i=1; i<=60 ; i++) {
				arr[i] = sc.next();
		}
		for(int i=1; i<=60; i++) {
			switch(arr[i]) {
			case "A+":
				arr[i] = "4.5";
				break;
			case "A0":
				arr[i] = "4.0";
				break;
			case "B+":
				arr[i] = "3.5";
				break;
			case "B0":
				arr[i] = "3.0";
				break;
			case "C+":
				arr[i] = "2.5";
				break;
			case "C0":
				arr[i] = "2.0";
				break;
			case "D+":
				arr[i] = "1.5";
				break;
			case "D0":
				arr[i] = "1.0";
				break;
			case "F":
				arr[i] = "0.0";
				break;
			case "P":
				arr[i] = "0.0";
				arr[i-1] = "0.0";
				break;
			}
		}
		for(int i=1 ; i<=58 ; i++) {
				num += Double.parseDouble(arr[i+1])*Double.parseDouble(arr[i+2]);
				num1 += Double.parseDouble(arr[i+1]);
				i +=2;
		}
		double avg = num/num1;
		System.out.println(avg); 
	}
}