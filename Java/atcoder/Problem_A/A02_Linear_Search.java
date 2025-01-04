import java.io.*;
import java.util.*;

public class A02_Linear_Search {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int X = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(br.readLine());
		for(int i = 0 ; i < N ; i++){
			if (X == Integer.parseInt(st.nextToken())){
				bw.write("Yes");
				bw.flush();
				bw.close();
				return ;
			}
		}
		bw.write("No");
		bw.flush();
		bw.close();
	}
}
