import java.io.*;
import java.util.*;

public class 나머지_합 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int[] arr = new int[N + 1];
		st = new StringTokenizer(br.readLine());
		for(int i = 1 ; i < N + 1 ; i++)
			arr[i] = arr[i - 1] + Integer.parseInt(st.nextToken());
		int answer = 0;
		for(int i = 1 ; i < arr.length ; i++){
			if(arr[i] % M == 0) answer++;
		}
		for (int step = 1; step < arr.length; step++) { // step은 연산 단계
			for (int i = 1; i < arr.length - step; i++) { // 범위를 좁혀가며 계산
				int result = arr[i + step] - arr[i];
				if (result % M == 0){
					answer++;
				}
			}
		}
		bw.write(Integer.toString(answer));
		bw.flush();
		bw.close();
	}
}
