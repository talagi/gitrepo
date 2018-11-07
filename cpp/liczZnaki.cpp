/*
 * liczZnaki.cpp
 * 
 */


#include <iostream>

using namespace std;

void licz_znaki(char tb[], int roz)
{
    int cyfry, literyD, literyM, reszta;
    cyfry = literyD = literyM = reszta = 0;
    int i = 0;
    while (tb[i] != '\0') {
        znak_kod = (int)tb[i]; //kodASCII badanego znaku
        if (znak_kod > 64 && znak_kod < 91 )
            literyD++;
        else if
        }
        i++;
    }
    cout << "\n\nBiałych: " << biale << endl;
    cout << "Interpunkcyjne: " << inter << endl;
    cout << "Inne: " << reszta << endl;
}

int main(int argc, char **argv)
{
    const int rozmiar = 20;
    char znaki[rozmiar];
    cin.getline(znaki, rozmiar);
    licz_znaki(znaki, rozmiar);
    return 0;
}
