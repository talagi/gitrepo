/*
 * sortowanie.cpp
 * 

 */


#include <iostream>
#include <cstdlib>
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

void zamien1(int &a, int &b) {
    cout << a << " " << b << endl;
    int tmp = a;
    a = b;
    b = tmp;
    cout << a << " " << b << endl;
    
}

void zamien2(int tab[], int i) {
    int tmp = tab[i];
    tab[i] = tab[i+1];
    tab[i+1] = tmp;
    
}

void sort_bubble(int tab[], int n){
    for(int j = n - 1; j > 0; j--) {
        for(int i = 0; i < j; i++) {
            if (tab[i] > tab[i + 1])
                //zamien1(tab[i], tab[i+1]);
                zamien2(tab, i);
        }
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

void sort_selection(int tab[], int n){
    int i, k, j;
    for (i = 0; i < n; i++){
        k = i;  // indeks najmniejszego elementu
        for(j = k + 1; j < n; j++){
            if (tab[j] < tab[k])
            k = j;
        }
        zamien1(tab[i], tab[k]);
    }
}


int main(int argc, char **argv)
{
	int n = 20;
    int tab[n];
    wypelnij(tab, n);
    drukuj(tab, n);
    //int a = 10;
    //int b = 20;
    //zamien1(a, b)
    //cout << a << " " << b;
    cout << endl;
    sort_bubble(tab, n);
    sort_insert(tab, n);
    sort_selection(tab, n);
    cout << endl;
    drukuj (tab, n); 
	return 0;
}

