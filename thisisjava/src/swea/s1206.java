package swea;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class s1206 {
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		int arr[] = new int[1000];
		int arr2[] = new int[1000];
		int i=0;

		
		while(i<10) {
			int num=0;
			int a = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<a ; j++) {
				arr[j] = Integer.parseInt(st.nextToken());
			}
			for(int k=2; k<a-2 ; k++) {
					int max = Math.max(arr[k - 2], Math.max(arr[k - 1], Math.max(arr[k + 1], arr[k + 2])));	
					if(arr[k]-max >0) {
					num += arr[k]-max;	
					}
			}
			bw.write("#"+ (i+1) +" " + num +"\n");
			arr = arr2;
			i++;
		}
		br.close();
		bw.flush();
	}
}
