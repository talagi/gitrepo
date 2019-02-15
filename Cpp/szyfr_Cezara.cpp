#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

#define MAKS 100

void deszyfruj(char tekst[], int klucz {
    klucz = klucz % 26;
    int kod = 0;
    int ilosc = strlen(tekst);
    
    while(tb[i] != '\0')
}

void szyfruj(char tekst[], int klucz){
    klucz = klucz % 26;
    int kod = 0;
    int ilosc = strlen(tekst);
    
    for(int i = 0; i < ilosc; i++){
        kod = (int)tekst[i] + klucz;
        if (tekst[i] == ' ') 
            kod -= klucz;
        else if (kod > 122) 
            kod -= 26;
        cout << tekst[i];
        tekst[i] = (char)kod;
    
    }

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
