#include <iostream>
#include <cmath>
using namespace std;

int func1(int n){
    int sum = 0;
    for(int i = 0 ; i <= n ; i++){
        if ((i%3 == 0) || (i % 5 == 0)) sum += i;
    }
    return sum;
}

int func2(int arr[], int N){
    for (int i = 0 ; i < N ; i++)
        for (int j = i + 1 ; j < N ; j++)
            if (arr[i] + arr[j] == 100) return 1;
    return 0;
}

int func3(int N){
    for (int i = 1 ; i * i <= N ; i++)
        if (i * i == N) return 1;
    return 0;
}

int func4(int N){
    // int max = 0;
    // for(int i = 2 ; i <= N ; i*=2)
    //     if (i > max) max = i;
    // return max;
    int val = 1;
    while (val * 2 <= N) val *= 2;
    return val;
}
int main() {
    cout << func1(16) << "\n";
    cout << func1(34567) << "\n";
    cout << func1(27639) << "\n";

    int a1[] = {1, 52, 48};
    int a2[] = {50, 42};
    int a3[] = {4, 13, 63, 87};

    cout << "func2" << endl;
    cout << func2(a1, 3) << "\n";
    cout << func2(a2, 2) << "\n";
    cout << func2(a3, 4) << "\n";

    cout << "func3" << endl;
    cout << func3(9) << endl;
    cout << func3(693953651) << endl;
    cout << func3(756580036) << endl;

    cout << "func4" << endl;
    cout << func4(5) << endl;
    cout << func4(97615282) << endl;
    cout << func4(1024) << endl;
}