# Allegro-Staż
Repozytorium zawierające rozwiązane do zadania nr 3 z trzeciego etapu rekrutacji na stanowisko Software Engineer Intern w firmie Allegro.

## Struktura
`allegro_server.py` - aplikacja serwerowa będąca rozwiązaniem zadania,

`allegro_client.py` - pomocnicza aplikacja kliencka pozwalająca na przetestowanie działania aplikacji serwerowej.

## Instalacja
Do poprawnego działania aplikacji konieczne będzie zainstalowanie biblioteki *requests* poleceniem `pip install requests`.
Samo oprogramowanie nie wymaga instalacji, należy jedynie pobrać pliki `allegro_server.py` i `allegro_client.py` oraz umieścić je w łatwo dostępnym folderze.

## Uruchomienie
Uruchomienie oprogramowania należy rozpocząć od pliku `allegro_server.py`:
```
python3 allegro_server.py
```
Aplikacje można uruchomić również określając nazwę hosta oraz numer portu (domyślnie localhost:80):
```
python3 allegro_server.py host:port
```

Aplikacja serwerowa jest już gotowa do przyjmowania żądań GET z parametrem w postaci `user=nazwa_uzytkownika`.
W celu przetestowania działania aplikacji możemy wykorzystać pomocniczą aplikację `allegro_client.py`, którą uruchamiamy analogicznie do `allegro_server.py`:
```
python3 allegro_client.py
```
Tutaj również aplikację można uruchomić określając inną nazwę hosta oraz numer portu:
```
python3 allegro_client.py host:port
```

## Zastosowanie
Po uruchomieniu obu aplikacji od strony klienta otrzymamy prośbę o wprowadzenie nazwy użytkownika:
```
Input GitHub username or click enter to finish:
```
Po podaniu nazwy użytkownika aplikacja kliencka wyśle zapytanie do serwera, który następnie zwróci odpowiednie dane. W kolejnym kroku zostają one przez klienta odpowiednio zinterpretowane oraz wyświetlone w terminalu.

### Przykład użycia
Uruchamiamy aplikację serwerową z domyślnymi parametrami:
```
python3 allegro_server.py
Listening on http://localhost:80
```
Uruchamiamy aplikację kliencką z domyślnymi parametrami i podajemy nazwę interesującego nas użytkownika serwisu GitHub (w tym przypadku wykorzystam swoją własną):
```
python3 allegro_client.py
Input GitHub username or click enter to finish: worso11
```
Serwer otrzymuje żądanie oraz wyświetla je w konsoli wraz z kodem odpowiedzi:
```
127.0.0.1 - - [25/Apr/2021 19:33:58] "GET /?user=worso11 HTTP/1.1" 200 -
```
Klient otrzymuje informację zwrotną od serwera i wyświetla ją w czytelny sposób:
```
User: worso11

Repositories:
1.      Repository name: Allegro-Internship
        Number of stars: 0
2.      Repository name: Bomberman
        Number of stars: 1
3.      Repository name: DP_Project
        Number of stars: 0

Total number of stars: 1
```

## Możliwe rozszerzenia projektu
- pobieranie dodatkowych informacji (opisy repozytoriów, wykorzystywane języki programowania, data utworzenia, dodatkowe dane o użytkowniku),
- poszerzenie danych na temat gwiazdek (średnia ilość gwiazdek na projekt, projekt z największą ilością gwiazdek).
