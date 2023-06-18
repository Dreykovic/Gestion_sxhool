from table import Table
class TableClasse( Table):
    table = 'classe'
    schema = [("id_classe", "k", "serial", "", ""),
              ("nom", "", "varchar", "", ""),
              ("effectif", "", "integer", "", "")]
    primary_key = 'id_classe'
    def __init__(self, nom=None, effectif=None):
        self.id_classe = 0
        self.nom = nom
        self.effectif = effectif
        

    @classmethod
    def updateNom(cls, matricule, nom):

        try:
            req = f"UPDATE  {cls.table} SET nom = '{nom}' WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
            row = cls.selectAttrWhereId('nom, effectif', matricule)
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la mise à jour du libelle de  {row[0]} {row[1]}:\n{req}\n :")
            print(err)
            return 0
        else:
            cls.lk.commit()
            return 1
        
    @classmethod
    def updateEffectif(cls, matricule, effectif):

        try:
            req = f"UPDATE  {cls.table} SET effectif = '{effectif}' WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
            row = cls.selectAttrWhereId('nom, effectif', matricule)
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la mise à jour du libelle de  {row[0]} {row[1]}:\n{req}\n :")
            print(err)
            return 0
        else:
            cls.lk.commit()
            return 1


def main():

    tut = TableClasse("Dosseh")
    tut.create()


if __name__ == '__main__':
    main()
    print('5555')
    pass






