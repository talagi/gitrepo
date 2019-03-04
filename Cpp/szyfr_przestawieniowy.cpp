#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

#define MAKS 100

void deszyfruj(char tekst[], int klucz) {
    ;
}

void szyfruj(char tb[], int klucz){
    int ile = strlen(tb);
    
}

int main(int argc, char **argv)
{
    char tekst[MAKS];
	int klucz = 0;
    
    cout << "Podaj tekst: " << endl;
    cin.getline(tekst, MAKS);
    
    cout << "Podaj klucz: " << endl;
    cin >> klucz;
    
    szyfruj(tekst, klucz);
	return 0;
}
