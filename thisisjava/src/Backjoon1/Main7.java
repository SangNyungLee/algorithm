package Backjoon1;

import java.io.*;
import java.util.*;
 
 
public class Main7 {
 
    public static void main(String[] args) throws IOException {
        
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
       
       int n = Integer.parseInt(br.readLine());
       for(int i=0; i<n; i++) {
           StringTokenizer st = new StringTokenizer(br.readLine());
           int num1 = Integer.parseInt(st.nextToken());
           int num2 = Integer.parseInt(st.nextToken());
           
           bw.write((num1+num2)+"\n");
          }
       bw.flush();
       
        } 
        
    }