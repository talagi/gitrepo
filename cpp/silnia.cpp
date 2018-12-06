/*
 * silnia.cpp
 * 
 */


#include <iostream>
using namespace std;

int silnia_it(int a){
    int wynik = 1;
    for (int i = 1; i <= a; i++){
        wynik = wynik * i;
    }
    return wynik;
}


int silnia_rek(int a){
    if (a < 2){
        return 1;
    }
    return a * silnia_rek(a - 1);
}

int main(int argc, char **argv)
{
	int a;
    cout << "Podaj liczbę: ";
    cin >> a;
    cout << "Silnia: " << silnia_it(a) << endl;
    cout << "Silnia: " << silnia_rek(a) << endl;
	return 0;
}

