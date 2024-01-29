import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class dd {
    public static void main(String [] args){
        Queue<Integer> q = new LinkedList<>();
        Stack<Integer> s = new Stack<>();

        s.push(1);
        s.push(2);
        s.push(3);
        s.push(4);
        s.pop();
        q.offer(5);
        q.offer(2);
        q.offer(3);
        q.offer(7);
        q.poll();
        q.offer(1);
        q.offer(4);
        q.poll();
        System.out.println(s);
        System.out.println("STACT" + s.peek());
        System.out.println("PEEK CHECK : " + q.peek());
        while(!q.isEmpty()){
            System.out.print(q.poll() + " ");
        }
        System.out.println();
        while(!s.isEmpty()){
            System.out.print(s.peek() + " ");
            s.pop();
        }

    }
}
