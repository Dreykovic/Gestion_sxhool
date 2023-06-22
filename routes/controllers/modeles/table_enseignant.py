from table_personne import *
import datetime as dt


class TableEnseignant(TablePersonne):
    relation = "enseignant"
    schema = [
        primary_key("matricule"),
        not_null(string("nom")),
        not_null(string("prenom")),
        not_null(date("date_naissance")),
        not_null(string("contact")),
        not_null(string("genre")),
        not_null(string("adresse")),
        not_null(string("statut")),
    ]

    def __init__(
        self,
        nom=None,
        prenom=None,
        date_naissance=None,
        contact=None,
        genre=None,
        adresse=None,
        statut=None,
    ):
        TablePersonne.__init__(
            self, nom, prenom, date_naissance, contact, genre, adresse
        )
        self.statut = statut


def main():
    tut = TableEnseignant(
        "Dosseh", "OOO", datenaiss, "70546987", "M", "BP 25 Sok", "Soulard"
    )
    tut.create()


if __name__ == "__main__":
    main()
    print("5555")
    pass
