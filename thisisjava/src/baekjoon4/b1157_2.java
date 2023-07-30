package baekjoon4;

import java.util.Scanner;

public class b1157_2 {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		String word = sc.nextLine().toUpperCase();
		
		int[] count = new int[26];
		
		for(int i=0; i<word.length(); i++) {
			int num = word.charAt(i) -'A';
			count[num]++;
		} // 입력받은 문자를 숫자로 바꿔서 배열에 +1씩 집어넣음
		
		int wordCount =0;
		char answer = '?';
		
		for(int i =0; i<count.length; i++) { 
			
			if(wordCount < count[i]) {	//count 값이 0보다 클 때
				
				wordCount = count[i];	// wordCount 값에 count 값을 넣는다.
				answer = (char)(i+'A');	// answer 저장
				
			} else if(wordCount == count[i]) { //wordCount값이랑 count 값이 같으면 answer에 ? 저장
				answer ='?';					
			}
		}
		System.out.println(answer);
	}

}