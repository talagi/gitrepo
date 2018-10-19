/*
 * figury.cpp
 * 
 */


#include <iostream>

using namespace std;

void prostokat2(int x, int y, char znak) {
    for (int i = 0; i < x; i++) {
        for (int j = 0; j < y; j++) {
            if (i == 0 || j == y - 1 || i == 0 || i == x - 1) {
                cout << znak; 
                ile++;
            }
        }
        cout << endl;
    }
}


int main(int argc, char **argv)
{
	int a, b; // deklaracja
    a = b = 0; // inicjacja
    // int a = 0; // definicja
    cout << "Podaj bok pierwszy: ";
    cin >> a;
    cout << "Podaj bok drugi: ";
    cin >> b;
    
    char znak;
    cout << "Podaj znak: ";
    cin >> znak;
    
    prostokat2(a, b, znak);
	return 0;
}

