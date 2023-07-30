 package baekjoon5;

import java.util.Scanner;

public class b2738 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		int num2 = sc.nextInt();
		int[][] array = new int[num][num2];
		int[][] array2 = new int[num][num2];
		for(int i=0; i<num; i++) {
			for(int j=0; j<num2 ; j++) {
				array[i][j] = sc.nextInt();
			}
		}
		for(int i=0; i<num; i++) {
			for(int j=0; j<num2 ; j++) {
				array2[i][j] = sc.nextInt();
			}
		}
		for(int i=0; i<num ; i++) {
			for(int j=0; j<num2 ; j++) {
				array[i][j] = array[i][j] + array2[i][j];
			}
		}
		for(int i=0; i<num; i++) {
			for(int j=0; j<num2 ; j++) {
				System.out.print(array[i][j] +" ");
			}
		}
	}

}
