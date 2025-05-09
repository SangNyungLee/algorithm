#include <bits/stdc++.h>
using namespace std;

int main(void){
    stack<int> S;
    S.push(10); // 10
    S.push(20); // 10 20
    S.push(30); // 10 20 30
    cout << S.size() << '\n'; // 3
    if(S.empty()) cout << "S is empty\n";
    else cout << "S is not empty\n"; 
    S.pop(); // 10 20
    cout << S.top() << '\n'; // 20
    S.pop();
    cout << S.top() << '\n'; // 10
    S.pop();
    if(S.empty()) cout << "S is empty\n"; // S is empty
    cout << S.top() << '\n'; // runtime error 발생

    // 스택이 비어있을 때는 top이나 pop을 호출하지 않도록 해야됨!
}