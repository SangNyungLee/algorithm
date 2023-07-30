import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String [] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int t = Integer.parseInt(br.readLine());	//테스트케이스 수
		
		for(int k=1 ; k<=t ; k++) {
			
			int a = Integer.parseInt(br.readLine());	// 사람 수
			
			int arr[] = new int[a];
			int arr2[] = new int[a];
			int num = 0;
			int num2 = 0;

			for(int i=0; i<a ; i++) {
				arr[i] = i;
			}
			
			st = new StringTokenizer(br.readLine());
			for(int i=0; i<a ; i++) {	
				arr2[i] = Integer.parseInt(st.nextToken());
				if(arr2[i] + i <0) {
					arr2[i] = 0;
					num2 -=1;
				} else if(arr2[i] + i >= a) {
					arr2[i] = 0;
					num2 -=1;
				}
			}
			
			for(int i=0 ; i<a ; i++) {	
				
				int m = arr[i] + arr2[i];
				if(arr[m] == arr[i]+arr2[i] && arr[i] == arr[m] + arr2[m]) {
					num+=1;
				}
			}
			System.out.println("#"+k +" "+((num+num2)/2));
		}
	}
}
