import java.io.*;
import java.util.*;

public class B03_SuperMarket_1 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int[] arr = new int[N];
		
		st = new StringTokenizer(br.readLine());
		for(int i = 0 ; i < N ; i++)
			arr[i] = Integer.parseInt(st.nextToken());
		for(int i = 0 ; i < N - 2 ; i++){
			for(int j = i + 1 ; j < N - 1 ; j++){
				for (int k = j + 1 ; k < N ; k++){
					if (arr[i] + arr[j] + arr[k] == 1000){
						bw.write("Yes");
						bw.flush();
						bw.close();
						return ;
					}
				}
			}
		}
		bw.write("No");
		bw.flush();
		bw.close();
	} 
}
