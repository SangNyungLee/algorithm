import java.io.*;
import java.util.*;

// public class A07_EventAttendance{
// 	public static void main(String[] args) throws IOException{
// 		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
// 		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
// 		StringTokenizer st;
	
// 		int D = Integer.parseInt(br.readLine());
// 		int N = Integer.parseInt(br.readLine());
// 		int[] arr = new int[D + 1];
	
// 		for(int i = 0 ; i < N ; i++){
// 			st = new StringTokenizer(br.readLine());
// 			int start = Integer.parseInt(st.nextToken());
// 			int end = Integer.parseInt(st.nextToken());
// 			for(int j = start ; j < end + 1 ; j++){
// 				arr[j] += 1;
// 			}
// 		}
// 		for(int i = 1 ; i < D + 1 ; i++)
// 			bw.write(arr[i] + "\n");
// 		bw.flush();
// 		bw.close();
// 	}
// }
// public class A07_EventAttendance{
// 	public static void main(String[] args) {
// 		Scanner sc = new Scanner(System.in);
// 		int D = sc.nextInt();
// 		int N = sc.nextInt();
// 		int[] arr = new int[D + 1];

// 		for(int i = 0 ; i < N ; i++){
// 			int start = sc.nextInt();
// 			int end = sc.nextInt();
// 			for(int j = start ; j < end + 1 ; j++)
// 				arr[j] += 1;
// 		}
// 		for(int i = 1 ; i < D + 1 ; i++)
// 			System.out.println(arr[i]);
// 	}
// }
public class A07_EventAttendance{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
	
		int D = Integer.parseInt(br.readLine());
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[D + 2];
		
		for(int i = 0 ; i < N ; i++){
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			arr[start] += 1;
			arr[end + 1] -= 1;
		}
		for(int i = 1 ; i < D + 1 ; i++){
			arr[i] = arr[i - 1] + arr[i];
			bw.write(Integer.toString(arr[i]) + "\n");
		}
		bw.flush();
		bw.close();
	}
}