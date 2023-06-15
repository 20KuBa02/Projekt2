# Projekt2
WtyczkaNaZajeciahDialog
  Jest to wtyczka dla QGIS, która służy do wykonywania różnych zadań związanych z analizą danych przestrzennych. Wtyczka dostarcza interfejsu graficznego użytkownika (GUI), który umożliwia interakcję z funkcjonalnościami wtyczki.

# Instalacja
  Aby zainstalować wtyczkę, wykonaj następujące kroki:

Otwórz oprogramowanie QGIS.
  Przejdź do menu "Wtyczki" i wybierz "Zarządzaj i instaluj wtyczki".
  W oknie "Wtyczki" przejdź do zakładki "Ustawienia".
  Kliknij przycisk "Dodaj..." aby dodać nowe repozytorium.
  Wprowadź nazwę repozytorium (np. "WtyczkaNaZajeciah") oraz następujący adres URL: [repository_url].
  Kliknij "OK", aby zapisać repozytorium.
  Wróć do zakładki "Wtyczki" i wyszukaj "WtyczkaNaZajeciah" w pasku wyszukiwania.
  Kliknij nazwę wtyczki, aby ją wybrać, a następnie kliknij przycisk "Zainstaluj", aby zainstalować wtyczkę.
  Po zainstalowaniu, możesz uzyskać dostęp do wtyczki z menu "Wtyczki".
# Korzystanie
  Po zainstalowaniu wtyczki, możesz korzystać z jej funkcji za pośrednictwem interfejsu graficznego użytkownika (GUI) wtyczki. Interfejs graficzny udostępnia kilka przycisków, które wykonują różne zadania:

    "policz" - Ten przycisk liczy liczbę wybranych obiektów w bieżącej warstwie i wyświetla liczbę w etykiecie.
    "współrzędne punktów" - Ten przycisk wyświetla współrzędne wszystkich zaznaczonych plików. Punkty wyświetlane są układzie zdefini0wanym przez warstwę.
    "różnica wyskości" - Ten przycisk oblicza różnicę wysokości między dwoma wybranymi punktami w bieżącej warstwie i wyświetla wynik w oknie dialogowym. Funkcja działa jeśli punkt posiada atrybut 'H_PLEVRF20'. W repozytorium podany jest przykładowy plik do obliczenia. Różnica wyskości zwracana jest w metrach.
    "pole" - Ten przycisk oblicza powierzchnię wielokąta utworzonego przez wybór wielu punktów w bieżącej warstwie za pomocą metody Gaussa. Obliczona powierzchnia jest wyświetlana w oknie dialogowym. Jednostką wyświetlanej wartości jest metr kwadratowy.
  Upewnij się, że wybrano odpowiednią warstwę i obiekty przed użyciem funkcji wtyczki.
