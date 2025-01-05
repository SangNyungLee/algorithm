import java.io.*;
import java.util.*;

public class 인간_컴퓨터_상호작용 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;

		String str = br.readLine();
		int q = Integer.parseInt(br.readLine());
		int[][]arr = new int[26][str.length()];
		
		for(int i = 0 ; i < str.length() ; i++){
			char c = str.charAt(i);
			arr[c - 'a'][i] = 1;
		}
		for(int i = 0 ; i < arr.length ; i++){
			for(int j = 1 ; j < arr[0].length ; j++)
				arr[i][j] += arr[i][j-1];
		}
		for(int i = 0 ; i < q ; i++){
			st = new StringTokenizer(br.readLine());
			char s = st.nextToken().charAt(0);
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());

			int result = arr[s - 'a'][end];
			if (start > 0)
				result = result - arr[s - 'a'][start - 1];

			bw.write(result + "\n");
		}
		bw.flush();
		bw.close();
	}
}
