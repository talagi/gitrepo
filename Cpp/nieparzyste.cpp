/*
 * nieparzyste.cpp
 * 
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    int n, i;
    cout << "Podaj liczbę: ";
    cin >> n;

    i = 1;
    
    while( i != n ) {
        cout << i << endl;
        i += 2;
    }
	
	return 0;
}

