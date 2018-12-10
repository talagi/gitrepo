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
// horner_rek(2, 3, tbwsp);
// horner_rek(2, 2, tbwsp) * 2 + 4;
// horner_rek(2, 1, tbwsp) * 2 + 5;
// horner_rek(2, 0, tbwsp) * 2 + 3;
// 2 * 2 + 3 = 7
// 7 * 2 + 5 = 19
// 19 * 2 + 4 = 42
// 42

float horner_rek(float x, int st, float tbwsp[]){
    if (st == 0) 
        return tbwsp[0];
    return x * horner_rek(x, st - 1, tbwsp) + tbwsp[st];
    
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

