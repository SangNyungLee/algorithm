import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Solution2 {
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		for(int k=1; k<=t ; k++) {
			int n = sc.nextInt();	//지연장치 개수
			int d = sc.nextInt();	//왼쪽으로 발사되는 좌표
			int x =0;;	//0부터 가는놈
			int dx = d; //d 부터 마이너스
			int arr[] = new int[d];	//좌표
			int num = 0;
			for(int i=0; i<d ; i++) {
				arr[i] = 1;
			}
			
			for(int i=0; i<n ; i++) {
				int g = sc.nextInt(); // 지연장치 좌표
				int gt = sc.nextInt(); // 지연장치 시간
				arr[g] = gt;
				
			}
			
			for(int i=0; i<d ; i++) {
				if(arr[i] !=1) {
					if(Math.abs(i-x) > Math.abs(i-dx)) {
						dx -= arr[i];
						i= i + arr[i];
					}
					if(Math.abs(i-x) < Math.abs(i-dx)) {
						x += arr[i];
						i = i+ arr[i];
					}
				}
				x += arr[i];
				dx -= arr[i];
				if(x == dx) {
					num = i;
					break;
				}
			}
			System.out.println("#"+k+" " + num+2);
		}
	}
}
