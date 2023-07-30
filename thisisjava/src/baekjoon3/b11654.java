package baekjoon3;

import java.util.Scanner;

public class b11654 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		String s = sc.next();
		int sum = 0;
		String[] arr = new String[a];
		arr = s.split("");
		
		for(int i =0 ; i<arr.length ; i++) {
			sum += Integer.parseInt(arr[i]);
		}
		System.out.println(sum);
	}
}
