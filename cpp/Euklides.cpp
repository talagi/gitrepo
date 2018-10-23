/*
 * euklides.cpp
 */


#include <iostream>
using namespace std;
int nwd_1(int a, int b) {
    while(a != b) {
        if (a > b){
            a = a - b;
        }
        else {
            b = b - a;
        }
    }
    return(a);
}


int main(int argc, char **argv)
{
    int b = 0;
    int a = 0;
    cout << "Podaj 2 liczby: ";
    cin >> a >> b;

    int nwd = nwd_1(a,b);
        cout << "NWD ("<< a <<","<< b <<") = " << nwd << endl;

    return 0;
}
