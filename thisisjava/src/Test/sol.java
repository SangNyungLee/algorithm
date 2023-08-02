package Test;

import java.util.Scanner;

public class sol {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		for(int i=0; i<5 ; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			int c = sc.nextInt();
			
			if(a == 1) {
				System.out.println("1임");
			}else if(a==2) {
				System.out.println("2임");
			}else {
				System.out.println("나머지임");
			}
		}

	}

}
