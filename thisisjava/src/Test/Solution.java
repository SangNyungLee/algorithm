package Test;

import java.util.Arrays;
import java.util.Scanner;

public class Solution {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		int numbers[] = {1,31,31,24,10,1,9};
		int num =0;
		int max = numbers[0];
		int max2 =0;
		int answer;
		for(int i=1 ; i<numbers.length ; i++) {
			if(numbers[i] >= max) {
				max = numbers[i];
			}
		}
		for(int i=0; i<numbers.length ; i++) {
			if(numbers[i] == max) {
				num++;
			}
		}
		if(num<2) {
			for(int i=0 ; i<numbers.length ; i++) {
				if(numbers[i] >0 && numbers[i] > max2 && numbers[i] <max) {
					max2 = numbers[i];
				}
			}
		} else {
			max2 = max;
		}
		
		answer = max*max2;
		System.out.println(max);
		System.out.println(max2);
		System.out.println(num);
		System.out.println(answer);
	}
}