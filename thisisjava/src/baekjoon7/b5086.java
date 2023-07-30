package baekjoon7;

import java.util.Scanner;

public class b5086 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
	
		boolean run = true;
		while(run) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			if(a<b) {
				int sum = b/a;
				if(a*sum == b){
					System.out.println("factor");
				} else {
					System.out.println("neither");
				}
			} else if(a>b) {
				int sum = a/b;
				if(a == b*sum) {
					System.out.println("multiple");
				} else {
					System.out.println("neither");
				}
			} else if(a == 0 && b==0){
				run = false;
			} else {
				System.out.println("neither");
			}
		}
	}
}
