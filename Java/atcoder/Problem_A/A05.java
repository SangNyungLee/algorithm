import java.io.*;
import java.util.*;

public class A05 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int count = 0;

		for(int i = 1 ; i <= N ; i++){
			for(int j = 1 ; j <= N ; j++){
				if (i + j + N >= K && i + j < K){
					count++;
				}
			}
		}
		bw.write(Integer.toString(count));
		bw.flush();
		bw.close();
	}	
}
