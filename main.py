# Funkcja logowania
#Logowanie do systemu
#wyświetlanie, dodanie, usuwanie, aktualizacja listy schronisk (musi mieć współrzędne) + mapa z obiektami
#wyświetlanie dodanie, usuwanie, aktualizacja listy klientów (musi mieć współrzędne) + mapa z obiektami
#wyświetlanie dodanie, usuwanie, aktualizacja listy pracowników (musi mieć współrzędne) + mapa z obiektami
#wyświetlanie listy klientów wybranej firmy
#wyświetlanie listy pracowników wybranej firmy


from crud import show_shelters, show_customers, show_workers, remove_shelters, remove_customers, remove_workers, update_shelters, update_customers, update_workers, add_new_shelter,add_new_customer, add_new_worker, map_single_shelter, map_single_customer, map_single_worker, map_all_shelters, map_all_workers, map_all_customers, assign_workers_to_shelters, assign_customers_to_shelters
from date import shelters, customers, workers

if __name__== '__main__':
    print('Zaloguj się:')
    #menu_option: str = input("Wpisz imię i nazwisko autora kodu")
    print('Wpisz imię i nazwisko autora kodu')
    Login = "Joanna"
    Haslo = "Buda"
    login: str = input("Podaj login (imię):")
    hasło: str = input("Podaj hasło (nazwisko):")
    if Login == login and Haslo == hasło:
        print("Zalogowano pomyślnie")
    else:
        print("Błędny login lub hasło")
        login: str = input("Podaj login:")
        hasło: str = input("Podaj hasło:")
    while True:
        print("0. Wyśietl schroniska")
        print("1. Wyśietl klientów")
        print("2. Wyśietl pracowników")
        print("3. Usuń schronisko")
        print("4. Usuń klienta")
        print("5. Usuń pracownika")
        print("6. Aktualizuj schroniska")
        print("7. Aktualizuj klienta")
        print("8. Aktualizuj pracownika")
        print("9. Dodaj nowe schroniske")
        print("10. Dodaj nowego klienta")
        print("11. Dodaj nowego pracownika")
        print("12. Wyświetl schronisko na mapie")
        print("13. Wyświetl klienta na mapie")
        print("14. Wyświetl pracownika na mapie")
        print("15. Wyświetl wszystkie schroniska")
        print("16. Wyświetl wszystkich klientów")
        print("17. Wyświetl wszystkich pracowników")
        print("18. Wyświetl pracowników pracujących w danym schronisku")
        print("19  Wyświetl klientów danego schroniska")
        print("000.Zakończ pracę programu")
        menu_option: str = input("Dokonaj wyboru:")
        if menu_option == '0':
            show_shelters(shelters)
        if menu_option == '1':
            show_customers(customers)
        if menu_option == '2':
            show_workers(workers)
        if menu_option == '3':
            remove_shelters(shelters)
        if menu_option == '4':
            remove_customers(customers)
        if menu_option == '5':
            remove_workers(workers)
        if menu_option == '6':
            update_shelters(shelters)
        if menu_option == '7':
            update_customers(customers)
        if menu_option == '8':
            update_workers(workers)
        if menu_option == '9':
            add_new_shelter(shelters)
        if menu_option == '10':
            add_new_customer(customers, shelters)
        if menu_option == '11':
            add_new_worker(workers)
        if menu_option == '12':
            map_single_shelter(shelters)
        if menu_option == '13':
            map_single_customer(customers)
        if menu_option == '14':
            map_single_worker(workers)
        if menu_option == '15':
            map_all_shelters(shelters)
        if menu_option == '16':
            map_all_customers(customers)
        if menu_option == '17':
            map_all_workers(workers)
        if menu_option == '18':
            assign_workers_to_shelters(shelters, workers)
        if menu_option == '19':
            assign_customers_to_shelters(shelters, customers)
        if menu_option == '000':
            break

