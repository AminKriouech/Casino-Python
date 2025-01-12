class Libro:
    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
        self.disponibile = True

    def __str__(self):
        return f"{self.titolo} di {self.autore} (ISBN: {self.isbn})"

    def cambia_disponibilita(self, stato):
        self.disponibile = stato


class Utente:
    def __init__(self, nome, cognome, id_utente):
        self.nome = nome
        self.cognome = cognome
        self.id_utente = id_utente
        self.libri_prestati = []

    def __str__(self):
        return f"{self.nome} {self.cognome} (ID: {self.id_utente})"

    def prendi_in_prestito(self, libro):
        if libro.disponibile:
            self.libri_prestati.append(libro)
            libro.cambia_disponibilita(False)
            print(f"{self.nome} ha preso in prestito il libro: {libro}")
        else:
            print(f"Il libro '{libro.titolo}' non è disponibile.")

    def restituisci(self, libro):
        if libro in self.libri_prestati:
            self.libri_prestati.remove(libro)
            libro.cambia_disponibilita(True)
            print(f"{self.nome} ha restituito il libro: {libro}")
        else:
            print(f"Il libro '{libro.titolo}' non è stato preso in prestito da {self.nome}.")


class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.libri = []
        self.utenti = []

    def aggiungi_libro(self, libro):
        self.libri.append(libro)
        print(f"Libro aggiunto: {libro}")

    def registra_utente(self, utente):
        self.utenti.append(utente)
        print(f"Utente registrato: {utente}")

    def mostra_libri_disponibili(self):
        print("Libri disponibili:")
        for libro in self.libri:
            if libro.disponibile:
                print(f" - {libro}")


# Esempio di Uso del codice
biblioteca = Biblioteca("Biblioteca di Cattolica.")

# Aggiunta di libri
libro1 = Libro("Geronimo Stilton", "Elisabetta Dami", "10-8838432651")
libro2 = Libro("Diabolik", "Angela e Luciana Giussani", "8865277947")
biblioteca.aggiungi_libro(libro1)
biblioteca.aggiungi_libro(libro2)

# Registrazione di utenti
utente1 = Utente("Leonardo", "Moretti", "U001")
utente2 = Utente("Fabio", "Bilancioni", "U002")
biblioteca.registra_utente(utente1)
biblioteca.registra_utente(utente2)

# Prestiti
utente1.prendi_in_prestito(libro1)
utente2.prendi_in_prestito(libro1)  # Libro non disponibile

# Mostra libri disponibili
biblioteca.mostra_libri_disponibili()

# Restituzione
utente1.restituisci(libro1)
utente2.prendi_in_prestito(libro1)

# Mostra libri disponibili
biblioteca.mostra_libri_disponibili()
