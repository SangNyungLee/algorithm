#include <bits/stdc++.h>
using namespace std;

int func2(int arr[], int N){
    int arr2[101] = {0};
    // for (int i = 0 ; i < N ; i++)
    //     arr2[arr[i]] = 1;
    // for (int i = 0 ; i < N ; i++)
    //     if (arr2[100 - arr[i]] == 1 && 100 - arr[i] != 50){
    //         cout << 100 - arr[i] << '\n';
    //         return 1;
    //     }
    // return 0;
    for (int i = 0 ; i < N ; i++){
        if(arr2[100 - arr[i]] == 1)
            return 1;
        arr2[arr[i]] = 1;
    }

}
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int a1[] = {1, 52, 48};
    int a2[] = {50, 42};
    int a3[] = {4, 13, 63, 87};
    cout << func2(a1, 3) << '\n';
    cout << func2(a2, 2) << '\n';
    cout << func2(a3, 4) << '\n';
}