package baekjoon4;

import java.util.Scanner;

public class b2444 {
	public static void main(String [] args) {
        Scanner scanner = new Scanner(System.in);
        int num=scanner.nextInt();
        
        for(int i=0;i<num-1;i++){
            for(int j=i;j<num-1;j++){
                System.out.print(" ");
            }
            
            for(int j=0;j<i*2+1;j++){
                System.out.print("*");
            }
            System.out.println();
        }
        
        
        for(int i=0;i<num;i++){
            for(int j=0;j<i;j++){
                System.out.print(" ");
            }
            
            for(int j=i*2;j<num*2-1;j++){
                System.out.print("*");
            }
            System.out.println();                                                                                      
        }
    }
}