package Test;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Solution2 {
	public static void main(String [] args) throws IOException {
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//		StringTokenizer st;
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int M = sc.nextInt();
		int K = sc.nextInt();
		int arr[] = new int[N];
		int arr2[] = new int[N];
		int num =0;
		for(int i=1; i<N ; i++) {
			arr[i] = sc.nextInt();		//배열에 n값 저장
		}
		// M : 수의 변경이 일어나는 횟수
		for(int k=0 ; k<K ; k++) {
			// K : 구간합을 구하는 횟수
			for(int i=0; i<M ; i++) {
				int a = sc.nextInt();
				int b = sc.nextInt();
				int c = sc.nextInt();
				
				// 1일 때
				// b번째 수를 c로 바꿈
				// 2일 때
				// b번째 수부터 c번쨰 수 까지 더함
				// 3~5까지 구해라 -> 5번째 - 2번째
			
				if(a == 1) {
					arr[b-1] = c;
					for(int j= 1; j<N ; j++) {
						arr2[i] += arr[i] + arr[i-1];
					}
					
				} else if(a == 2) {
					num = arr[c-1] - arr[b-2]; 
				}
			}
			System.out.println(num);
		}



	}
}