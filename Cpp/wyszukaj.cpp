/*
 * wyszukaj.cpp
 */


#include <iostream>
using namespace std;

void wypelnij(int tab[], int roz) {
    srand (time(NULL)); // inicjacja generatora liczb pseudolosowych
    for(int i=0; i < roz; i++) {
        tab[i] = rand() % 101;
    }

}

void drukuj(int tab[], int roz) {
    cout << "Podaj " << roz << " liczb: " << endl;
    for(int i=0; i < roz; i++) {
        cout << tab[i] << " ";
    }

}

void sort_insert(int tab[], int n){
    cout << "\nSortowanie przez wstawianie\n";
    int i, j, tmp;
    int licznik = 0;
    for (i = 1; i < n; i++) {
        tmp = tab[i];
        j = i - 1;
        licznik++;
        while (j >= 0 && tab[j] > tmp){
            tab[j+1] = tab[j];
            j--;
        }
        tab[j+1] = tmp;
    }
    cout << "\nPowtórzeń: " << licznik << endl;
}

int szukaj_lin (int tab[], int n, int szuk){
    for (int i = 0; i < n; i++)
        if (tab[i] == szuk)
            return i;
    return -1;
}

// dziel i zwyciężaj 
int szukaj_bin_lin(int tab[], int n, int szuk){
    int p, k, s;
    p = 0; 
    k = n -1;
    while (p <= k) {
        s = (p + k) / 2;
        if (tab[s] == szuk){
            p = s;
            break;
        } else if (szuk < tab[s]) k = s - 1;
        else p = s + 1;
    }
    
    if (p >= 0) 
        cout << "Znaleziono: " << p << endl;
    else 
        cout << "Nie znaleziono: ";
    return p;
}

int main(int argc, char **argv)
{
	int n = 20;
    int tab[n];
    wypelnij(tab, n);
    drukuj(tab, n);
    int szuk = 0;
    cout << "Podaj liczbę: ";
    cin >> szuk;
    sort_insert(tab, n);
    int indeks = szukaj_bin_lin(tab, n, szuk);
    if (indeks >= 0) 
        cout << "Znaleziono: " << indeks << endl;
    else 
        cout << "Nie znaleziono: ";
    //~int indeks = szukaj_lin(tab, n, szuk);
	//~if (indeks != -1)
        //~cout << "Znaleziono!";
    //~else
        //~cout << "Nie znaleziono!";
    return 0;
}

