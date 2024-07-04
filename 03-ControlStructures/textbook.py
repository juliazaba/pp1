'''
Ćwiczenie 1. Przepisz ponownie swój program obliczający wynagrodzenie, tak aby dać pracownikowi 1,5 raza większą stawkę godzinową za czas przepracowany powyżej 40 godzin
liczba = int(input('Podaj liczbe godzin: '))
stawka = int(input('Podaj stawke godzinowa: '))

if liczba > 40:
    nadgodziny = liczba - 40
    wynagrodzenie = (stawka * 40) + (nadgodziny * stawka * 1.5)
    
    
else:
    wynagrodzenie = stawka * liczba 
    
print(f'Wynagrodzenie: {wynagrodzenie}')
'''
'''
liczba = input('Podaj liczbe godzin: ')
stawka = input('Podaj stawke godzinowa: ')
try:
    kwota = int(liczba)
    wyplata = int(stawka)
    if kwota > 40:
        nadgodziny = kwota - 40
        wynagrodzenie = (wyplata * 40) + (nadgodziny * wyplata * 1.5)
        
        
    else:
        wynagrodzenie = wyplata * kwota 
        
    print(f'Wynagrodzenie: {wynagrodzenie}')
    
except:
    print('Bląd, podaj wartość numeryczną')
    '''
    
'''
wartosc = input('Podaj wartość: ')
try:
    liczba = float(wartosc)
    if 0.0 < liczba < 0.5:
        print('2.0')
        
    elif 0.5 <= liczba < 0.6:
        print('3.0')
        
    elif 0.6 <= liczba < 0.7:
        print('3.5')
        
    elif 0.7 <= liczba < 0.8:
        print('4.0')
        
    elif 0.8 <= liczba < 0.9:
        print('4.5')
        
    elif 0.9 <= liczba <= 1.0:
        print('5.0')
        
    else:
        print('Niepoprawna wartosc')
except:
    print('Niepoprawna wartosc')
'''