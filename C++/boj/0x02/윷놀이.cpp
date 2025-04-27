#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    for (int i = 0 ; i < 3 ; i++){
        int a = 0;
        int arr[4];
        cin >> arr[0] >> arr[1] >> arr[2] >> arr[3];

        for (int i = 0 ; i < 4 ; i++)
            if (arr[i] == 0)
                a++;
        if (a == 4)
            cout << "D" << '\n';
        else if (a == 3)
            cout << "C" << '\n';
        else if (a == 2)
            cout << "B" << '\n';
        else if (a == 1)
            cout << "A" << '\n';
        else
            cout << "E" << '\n';
        }
}