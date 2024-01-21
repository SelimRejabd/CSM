#include<bits/stdc++.h>
using namespace std;
int main()
{
    string t="";
    vector<string>vc;
    vector<string> removedCharacters;
    for(int i=0;i<3;i++){
        string s;
        getline(cin, s);
        removedCharacters.push_back(s.substr(s.size()-5));
        s.erase(s.size()-5);
        vc.push_back(s);
    }
    for(auto x:vc)
        cout<<x<<endl;
    for(auto x:removedCharacters){
        cout<<x<<endl;
    }
}