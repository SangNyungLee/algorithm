public class RecursiveFunction {
    public int recursiveSum(int n){
        if(n==1) return 1;
        return recursiveSum(n-1) + n;
    }
    public void main(String [] args){
        int n = 10;
        RecursiveFunction rf = new RecursiveFunction();

        System.out.println("1부터 10까지의 합(재귀함수) : " + rf.recursiveSum(n));
    }
}
