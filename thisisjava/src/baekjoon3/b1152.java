package baekjoon3;

import java.util.Scanner;

public class b1152 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = sc.nextLine().trim();
//		s= s.trim();
		String arr[] = s.split("");
		int sum = 0;
		
		for(int i=0; i<arr.length; i++) {
			if(arr[i].equals("")) {
				break;
			}else {
				System.out.println(i+1 +": " + arr[i] +" ");
				sum +=1;
			}

		}
		System.out.println(sum);  
	}
}
