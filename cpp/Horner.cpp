/*
 * Horner.cpp
 * 
 * w(x) = 2x^3 + 3x^2 +5x + 4 => 6
 * w(x) = x (2x^2 + 3x + 5) + 4
 * w(x) = x (x (2x + 3) + 5) + 4 => 3
 * 
 */

#include <iostream>
using namespace std;

void drukujw(int st, float tb[]) {
    int i = 0;
    for (int i = 0; i < st; i++) {
        cout << tb[i] << "x^" << st-i << " + ";
    }
    cout << tb[i] << endl;
    
}

float horner_it(float x, int stopien, float tbwsp[]){
    float wynik = tbwsp[0];
    for (int i = 0; i < stopien + 1; i++){
        wynik = wynik * x + tbwsp[i];
    }
    return wynik;
}


int main(int argc, char **argv)
{
	int stopien = 0;
    float *tbwsp;  // wskaźnik
    float x = 0;  // argument
    cout << "Stopień wielomianu: ";
    cin >> stopien;
    
    tbwsp = new float [stopien + 1];
    cout << tbwsp;
    
    for(int i = 0; i <= stopien; i++) {
        cout << "Podaj współczynnik przy potędze" << stopien - i << ": ";
        cin >> tbwsp[i];
    }
    
    cout << "Argument: ";
    cin >> x;
    
    cout << "Wartość wielomianu o postaci: ";
    drukujw(stopien, tbwsp);
    cout << "Wynosi: " << horner_it(x, stopien, tbwsp);
    
	return 0;
}

