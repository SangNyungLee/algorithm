package Backjoon;

import java.util.Scanner;

public class Main3 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		double a = sc.nextDouble();
		
		if(((a%4 == 0) && (a%100 != 0)) || (a%400 == 0)) {
			System.out.println("1");
		}
		else { 
			System.out.println("2");
		}
	}
}
/*
 * 1. 400의 배수는 무조건 윤년임 -> 윤년 1 (A%400 = 0)
 * 2. 4의 배수이면서 100의 배수가 아니면 윤년임 -> 윤년 2 (A%4 = 0 && A%100 != 0)
 * 1,2 조건을 둘중 하나라도 만족시킨다 -> 윤년이고 나머지는 다 평년
 *
 * 
 */