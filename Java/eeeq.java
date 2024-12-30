import java.util.*;

public class eeeq {
    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedList<>();
        Deque<Integer> deque = new LinkedList<>();
        Stack<Integer> stack = new Stack<>();

        stack.push(1);
        stack.push(2);
        stack.push(3);

        queue.add(1);
        queue.add(2);
        queue.add(3);

        deque.add(1);
        deque.add(2);
        deque.add(3);

        System.out.println("queue = " + queue.remove());

        System.out.println("deque = " + deque.remove());

        System.out.println("stack = " + stack.pop());
    }
}
