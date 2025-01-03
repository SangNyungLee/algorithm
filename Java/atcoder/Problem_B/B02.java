import java.io.*;
import java.util.*;


// A이상 B이하의 정수 중에서 100의 약수인 정수가 존재합니까? 해답을 Yes/No로 대답하시오
public class B02 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int A = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		int [] arr = {1,2,4,5,10,20,25,50,100};
		for(int i = A ; i < B + 1 ; i++){
			for(int j : arr){
				if (j == i){
					bw.write("Yes");
					bw.flush();
					bw.close();
					return ;
				}
			}
		}
		bw.write("No");
		bw.flush();
		bw.close();
	}
}
