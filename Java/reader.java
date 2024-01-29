import java.io.*;
import java.util.StringTokenizer;

public class reader {
    public static void main(String[] args) throws IOException {
        int N;
        int M;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
        String s = br.readLine();
        System.out.println("N");
        StringTokenizer st = new StringTokenizer(s);

        System.out.println(st);
    }


}
