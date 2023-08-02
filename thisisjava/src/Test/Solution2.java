package Test;

import java.util.Scanner;

public class Solution2 {
	public static void main(String [] args)  {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();	//수의 개수
		int M = sc.nextInt();	// 수의 변경이 일어나는 횟수
		int K = sc.nextInt();	// 구간 합을 구하는 횟
		int arr[] = new int[N+1];
		int arr2[] = new int[N+1];
		int num = 0;
		
		for(int i=1; i<=N ; i++) {
			arr[i] = sc.nextInt();		//배열에 n값 저장
			arr2[i] = arr[i];
		}
		
		arr[0] = 0;
		arr2[0] = 0;
		
		for(int i=1 ; i<=N ; i++) {
			arr2[i] = arr2[i]+arr2[i-1];
		}
		
		// 1일 때
		// b번째 수를 c로 바꿈
		// 2일 때
		// b번째 수부터 c번쨰 수 까지 더함
		// 3~5까지 구해라 -> 5번째 - 2번째
		// M : 수의 변경이 일어나는 횟수
		// K : 구간합을 구하는 횟수
		
		for(int i=0; i<M+K ; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			int c = sc.nextInt();
			
			if(a == 1) {
				arr[b] = c;
				// arr랑 arr2랑 같게 만들어준다.
				for(int j=1 ; j<=N ; j++) {
					arr2[j] = arr[j];
				}
			} else if(a == 2) {
				for(int j=1; j<=N ; j++) {
					arr2[j] = arr2[j] + arr2[j-1];
				}
				num = arr2[c] - arr2[b-1];
				System.out.println(num);
			}
		}
	}
}