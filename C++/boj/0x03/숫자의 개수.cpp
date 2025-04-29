#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int a, b, c;
    int arr[10] = {0};
    cin >> a >> b >> c;
    int res = a * b * c;
    
    while (res > 0){
        arr[res % 10]++;
        res /= 10;
    }
    for(int i : arr) cout << i << '\n';
}