

def show_shelters(shelter_list: list[dict] )-> None:
    for shelter in shelter_list:
            print(f"Nazwa: {shelter['name']}, Miejscowość: {shelter['location']}, Szerokość geograficzna: {shelter['latitude']}, Długość geograficzna: {shelter['longitude']}")

def show_customers(customer_list: list[dict] )-> None:
    for customer in customer_list:
        print(f"Nazwa: {customer['name']}, Nazwisko: {customer['surname']}, Miejscowość: {customer['location']} Szerokość geograficzna: {customer['latitude']}, Długość geograficzna: {customer['longitude']}")

def show_workers(worker_list: list[dict] )-> None:
    for worker in worker_list:
      print(f"Nazwa: {worker['name']}, Nazwisko: {worker['surname']},Miejscowość: {worker['location']}, Szerokość geograficzna: {worker['latitude']}, Długość geograficzna: {worker['longitude']}")


def remove_shelters(shelter_list) -> None:
    kogo_szukasz = input('Kogo szukasz: ')
    for shelter in shelter_list:
        if shelter['name'] == kogo_szukasz:
            shelter_list.remove(shelter)
            print(f"Schronisko {kogo_szukasz} zostało usunięte.")
            return
    print(f"Schronisko {kogo_szukasz} nie zostało znalezione.")

def remove_customers(customer_list) -> None:
    kogo_szukasz = input('Kogo szukasz: ')
    for customer in customer_list:
        if customer['name'] == kogo_szukasz :
            customer_list.remove(customer)
            print(f"Klient {kogo_szukasz} został usunięty.")
            return


def remove_workers(worker_list) -> None:
    kogo_szukasz = input('Kogo szukasz: ')
    for worker in worker_list:
        if worker['name'] == kogo_szukasz:
            worker_list.remove(worker)
            print(f"Pracownik {kogo_szukasz} został usunięty.")
            return


def update_shelters(shelters_list) -> None:
    kogo_szukasz = input('Podaj nazwę schroniska do aktualizacji: ')
    for shelter in shelters_list:
        if shelter['name'] == kogo_szukasz:
            new_name = new_shelter = input('Podaj nową nazwę schroniska: ')
            new_location = input('Podaj nową miejscowość: ')


            coordinates = get_coordinates(new_location)
            if coordinates:
                new_latitude, new_longitude = coordinates
            else:
                new_latitude = float(input('Podaj nową szerokość geograficzną: '))
                new_longitude = float(input('Podaj nową długość geograficzną: '))

            # Update shelter data
            shelter['name'] = new_name
            shelter['location'] = new_location
            shelter['latitude'] = new_latitude
            shelter['longitude'] = new_longitude
            shelter['shelter'] = new_shelter

            print(f"Schronisko {kogo_szukasz} zostało zaktualizowane.")
            return

    print(f"Schronisko {kogo_szukasz} nie zostało znalezione.")

def update_customers(customers_list, shelter_list) -> None:
    kogo_szukasz = input('Podaj imię klienta do aktualizacji: ')
    for customer in customers_list:
        if customer['name'] == kogo_szukasz:
            new_name = input('Podaj nowe imię klienta: ')
            new_surname = input('Podaj nowe nazwisko:')
            new_location = input('Podaj nową miejscowość:')
            new_my_shelter = input('Podaj schronisko z którego korzystasz')

            if new_my_shelter not in shelter_list:
                print("Klient nie należy do istniejącego schroniska, usuń go")

                remove_customers(customers_list)
                return

            coordinates = get_coordinates(new_location)
            if coordinates:
                new_latitude, new_longitude = coordinates
            else:
                new_latitude = float(input('Podaj nową szerokość geograficzną: '))
                new_longitude = float(input('Podaj nową długość geograficzną: '))

            customer['name'] = new_name
            customer['surname'] = new_surname
            customer['location'] = new_location
            customer['latitude'] = new_latitude
            customer['longitude'] = new_longitude
            customer['shelter'] = new_my_shelter

            print(f"Dane klienta {kogo_szukasz} zostały zaktualizowane.")
            return
    print(f"Klient {kogo_szukasz} nie został znalezione.")

def update_workers(worker_list) -> None:
    kogo_szukasz = input('Podaj imię pracownika do aktualizacji: ')
    for worker in worker_list:
        if worker['name'] == kogo_szukasz:
            new_name = input('Podaj nowe imię pracownika: ')
            new_surname = input('Podaj nowe nazwisko:')
            new_location = input('Podaj nową miejscowość:')
            new_workplace = input('Podaj nowe miejsce pracy:')

            if new_workplace not in worker_list:
                print("Pracownik nie należy do istniejącego schroniska, usuń go")

                remove_workers(worker_list)
                return

            coordinates = get_coordinates(new_location)
            if coordinates:
                new_latitude, new_longitude = coordinates
            else:
                new_latitude = float(input('Podaj nową szerokość geograficzną: '))
                new_longitude = float(input('Podaj nową długość geograficzną: '))


            # Aktualizacja danych klienta
            worker['name'] = new_name
            worker['surname'] = new_surname
            worker['location'] = new_location
            worker['latitude'] = new_latitude
            worker['longitude'] = new_longitude
            worker['workplace'] = new_workplace

            print(f"Dane pracownika {kogo_szukasz} zostały zaktualizowane.")
            return
    print(f"Pracownik {kogo_szukasz} nie został znalezione.")


def add_new_shelter(shelters_list):
    new_name = new_shelter = input("Nazwa nowego schroniska: ")
    new_location = input("Miejscowość nowego schroniska: ")

    coordinates = get_coordinates(new_location)

    if coordinates:
        new_latitude, new_longitude = coordinates
    else:
        new_latitude = float(input("Szerokość geograficzna schroniska: "))
        new_longitude = float(input("Długość geograficzna schroniska: "))

    new_shelter = {
        "name": new_name,
        "location": new_location,
        "latitude": new_latitude,
        "longitude": new_longitude,
        "shelter": new_shelter
    }

    shelters_list.append(new_shelter)
    print(f"Nowe schronisko {new_name} zostało dodane.")

def add_new_customer(customer_list, shelter_list):
    new_name = input("Imię nowego klienta: ")
    new_surname = input("Nazwisko nowego klienta")
    new_location = input("Miejsce zamieszkania nowego klienta: ")
    new_my_shelter = input("Podaj schronisko, z którego korzysta nowy klient:")

    if new_my_shelter not in shelter_list:
        print("Klient nie należy do istniejącego schroniska, usuń go")

        remove_customers(customer_list)
        return


    coordinates = get_coordinates(new_location)

    if coordinates:
        new_latitude, new_longitude = coordinates
    else:

        new_latitude = float(input("Szerokość geograficzna klienta: "))
        new_longitude = float(input("Długość geograficzna klienta: "))

    new_customer = {
        "name": new_name,
        "surname": new_surname,
        "location": new_location,
        "latitude": new_latitude,
        "longitude": new_longitude,
        "shelter": new_my_shelter
    }

    customer_list.append(new_customer)
    print(f"Nowy klient {new_name} zostało dodane.")


def add_new_worker(worker_list):
    new_name = input("Imię nowego pracownika: ")
    new_surname = input("Nazwisko nowego pracownika:")
    new_location = input("Miejsce zamieszkania nowego pracownika: ")
    new_workplace = input("Podaj nowe miejsce pracy:")

    if new_workplace not in worker_list:
        print("Pracownik nie należy do istniejącego schroniska, usuń go")

        remove_workers(worker_list)
        return

    coordinates = get_coordinates(new_location)

    if coordinates:
        new_latitude, new_longitude = coordinates
    else:
        # If coordinates cannot be fetched, prompt user to input manually
        new_latitude = float(input("Szerokość geograficzna pracownika: "))
        new_longitude = float(input("Długość geograficzna pracownika: "))

    new_worker = {
        "name": new_name,
        "surname": new_surname,
        "location": new_location,
        "latitude": new_latitude,
        "longitude": new_longitude,
        "workplace": new_workplace
    }

    worker_list.append(new_worker)
    print(f"Nowy pracownik {new_name} został dodany.")

import requests
from bs4 import BeautifulSoup


def get_coordinates (location):
    """
    Function to get coordinates of foundations, donors, employee
    :return: list of coordinates of foundations, donors, employee
    """
    url: str = f"https://pl.wikipedia.org/wiki/{location}"
    response = requests.get(url)
    response_html = BeautifulSoup(response.text, "html.parser")
    latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
    longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
    return [latitude, longitude]


def map_single_shelter(shelters_list):
    shelter_name = input("Podaj nazwę schroniska do wyświetlenia na mapie: ").strip()

    selected_shelter = None
    for shelter in shelters_list:
        if shelter['name'].lower() == shelter_name.lower():
            selected_shelter = shelter
            break

    if selected_shelter is None:
        print(f"Schronisko '{shelter_name}' nie zostało znalezione.")
        return

    location = selected_shelter['location']
    latitude = selected_shelter['latitude']
    longitude = selected_shelter['longitude']

    print(f"Szerokość: {longitude}, Długość: {latitude}")

    map = folium.Map(location=[longitude, latitude], zoom_start=11)
    folium.Marker(location=[longitude, latitude], popup=f'{shelter_name}', icon=folium.Icon(color='blue')).add_to(map)
    map_filename = f'map_{shelter_name}.html'
    map.save(map_filename)
    print(f"Mapa została zapisana jako {map_filename}")

def map_single_customer(customers_list):
    customer_name = input("Podaj imię klienta do wyświetlenia na mapie: ").strip()

    selected_customer = None
    for customer in customers_list:
        if customer['name'].lower() == customer_name.lower():
            selected_customer = customer
            break

    if selected_customer is None:
        print(f"Imię klienta '{customer_name}' nie zostało znalezione.")
        return

    location = selected_customer['location']
    latitude = selected_customer['latitude']
    longitude = selected_customer['longitude']


    print(f"Szerokość: {longitude}, Długość: {latitude}")

    map = folium.Map(location=[longitude, latitude], zoom_start=11)
    folium.Marker(location=[longitude, latitude], popup=f'{customer_name}', icon=folium.Icon(color='blue')).add_to(map)
    map_filename = f'map_{customer_name}.html'
    map.save(map_filename)
    print(f"Mapa została zapisana jako {map_filename}")

def map_single_worker(worker_list):
    worker_name = input("Podaj imię do wyświetlenia do wyświetlenia na mapie: ").strip()

    selected_worker = None
    for worker in worker_list:
        if worker['name'].lower() == worker_name.lower():
            selected_worker = worker
            break

    if selected_worker is None:
        print(f"Pracownik '{worker_name}' nie został znalezione.")
        return

    location = selected_worker['location']
    latitude = selected_worker['latitude']
    longitude = selected_worker['longitude']

    print(f"Szerokość: {longitude}, Długość: {latitude}")

    map = folium.Map(location=[longitude, latitude], zoom_start=11)
    folium.Marker(location=[longitude, latitude], popup=f'{worker_name}', icon=folium.Icon(color='blue')).add_to(map)
    map_filename = f'map_{worker_name}.html'
    map.save(map_filename)
    print(f"Mapa została zapisana jako {map_filename}")





import folium

def map_all_shelters(shelters):
    map = folium.Map(location=[52, 20], zoom_start=6)
    for shelter in shelters:
        url = (f"https://pl.wikipedia.org/wiki/{shelter['location']}")
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude],
                      popup=f"{shelter['name']}",
                      icon=folium.Icon(color='blue')).add_to(map)

    map.save(f'map.shelters.html')

def map_all_customers(customers):
    map = folium.Map(location=[52, 20], zoom_start=6)
    for customer in customers:
        url = (f"https://pl.wikipedia.org/wiki/{customer['location']}")
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude],
                      popup=f"{customers['name']}",
                      icon=folium.Icon(color='blue')).add_to(map)

    map.save(f'map.customers.html')


def map_all_workers(workers):
    map = folium.Map(location=[52, 20], zoom_start=6)
    for worker in workers:
        url = (f"https://pl.wikipedia.org/wiki/{worker['location']}")
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude],
                      popup=f"{worker['name']}",
                      icon=folium.Icon(color='blue')).add_to(map)

    map.save(f'map.workers.html')


def assign_workers_to_shelters(shelters_list, workers_list):
    shelter_workers = {shelter['name']: [] for shelter in shelters_list}

    for worker in workers_list:
        work_place = worker['work_place']
        if work_place in shelter_workers:
            shelter_workers[work_place].append(worker)

    for shelter in shelters_list:
        shelter_name = shelter['name']
        print(f"Pracownicy schroniska '{shelter_name}':")
        workers = shelter_workers.get(shelter_name, [])
        if workers:
            for worker in workers:
                print(f"- {worker['name']} {worker['surname']} (Pracuje w {worker['work_place']})")
        else:
            print("Brak pracowników w tym schronisku.")
        print()

def assign_customers_to_shelters(shelters_list, customers_list):
    shelter_customer = {shelter['name']: [] for shelter in shelters_list}

    for customer in customers_list:
        my_shelter = customer['my_shelter']
        if my_shelter in shelter_customer:
            shelter_customer[my_shelter].append(customer)

    for shelter in shelters_list:
        shelter_name = shelter['name']
        print(f"Klienci schroniska '{shelter_name}':")
        customers = shelter_customer.get(shelter_name, [])
        if customers:
            for customer in customers:
                print(f"- {customer['name']} {customer['surname']} (Pracuje w {customer['my_shelter']})")
        else:
            print("Brak klientów w tym schronisku.")
        print()