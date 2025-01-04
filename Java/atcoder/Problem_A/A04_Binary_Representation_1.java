import java.util.*;

public class A04_Binary_Representation_1 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		for(int x = 9 ; x >= 0 ; x--){
			int wari = (1 << x);
			System.out.print((N / wari) % 2);
		}
		System.out.println();
	}
}
