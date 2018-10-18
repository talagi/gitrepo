/*
 * figury.cpp
 * 
 */


#include <iostream>

using namespace std;

void prostokat2(int x, int y, char znak) {
    for (int i = 1; i <= x; i++) {
        for (int j = 1; j <= y; j++) {
            if (i != j) {
                cout << i << j << " ";
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

