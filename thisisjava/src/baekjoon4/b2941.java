package baekjoon4;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class b2941 {
    public static void main(String[] args) throws Exception {

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String str = bufferedReader.readLine();

        String repalce = str.replace("c=", "!").replace("c-", "!")
                .replace("dz=", "!").replace("d-", "!")
                .replace("lj", "!").replace("nj", "!")
                .replace("nj", "!").replace("s=", "!")
                .replace("z=", "!");

        System.out.println(repalce.length());
    }
}
