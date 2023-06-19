from .table_personne import TablePersonne
import datetime as dt


class TableEnseignant(TablePersonne):
    relation = "enseignant"
    schema = [
        ("matricule", "k", "serial", "", ""),
        ("nom", "", "varchar", "", ""),
        ("prenoms", "", "varchar", "", ""),
        ("date_naissance", "", "date", "", ""),
        ("contact", "", "varchar", "", ""),
        ("genre", "", "varchar", "", ""),
        ("adresse", "", "varchar", "", ""),
        ("statut", "", "varchar", "", ""),
    ]
    primary_key = "matricule"

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

    @classmethod
    def update_statut(cls, matricule, statut):
        req = ''
        row = []
        try:
            req = f"UPDATE  {cls.relation} SET statut = '{statut}' WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
            row = cls.selectAttrWhereId(self.INFO_ATTR, matricule)
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la mise à jour du statut de  {row[0]} {row[1]}:\n{req}\n :"
            )
            print(err)
            return 0
        else:
            cls.lk.commit()
            print("UPDATE SUCCESSPULLY !!!")
            return 1


def main():
    datenaiss = dt.datetime(2003, 1, 2).date()
    tut = TableEnseignant(
        "Dosseh", "OOO", datenaiss, "70546987", "M", "BP 25 Sok", "Soulard"
    )
    tut.create()
    # tut.updateStatut(2, "Koba")


if __name__ == "__main__":
    main()
    print("5555")
    pass