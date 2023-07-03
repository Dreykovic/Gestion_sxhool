from .validators import *
from datetime import datetime
import sys
from .validators import *
from datetime import datetime
import sys
from .modeles.table import Table

class Controller:
    """
    Classe de contrôleur pour la gestion des opérations de données.

    Attributes:
        model (Table): Le modèle de données utilisé pour les opérations.
        MSG_INVALID_TEXT (str): Message d'erreur pour une saisie de texte invalide.
        MSG_INVALID_NUMBER (str): Message d'erreur pour un nombre invalide.
        MSG_INVALID_DATE (str): Message d'erreur pour une date invalide.
        MSG_INVALID_OPTION (str): Message d'erreur pour une option invalide.
    """

    model = Table
    MSG_INVALID_TEXT = "Saisie invalide. Veuillez saisir un texte valide."
    MSG_INVALID_NUMBER = "Saisie invalide. Veuillez saisir un nombre valide."
    MSG_INVALID_DATE = "Saisie invalide. Veuillez saisir une date valide."
    MSG_INVALID_OPTION = "Choix invalide. Veuillez sélectionner une option valide."

    def create(self):
        """
        Méthode pour créer une nouvelle entrée de données.
        """
        raise NotImplementedError("Le contrôleur doit implémenter la méthode create")

    @classmethod
    def destroy(cls):
        """
        Méthode pour supprimer des données existantes.
        """
        # ...
        message = f"Etes vous sur de vouloir supprimer les donnée de {cls.model.relation}  :"  # type: ignore
        data = cls.show(cls.model)
        matricule = cls.write_number("matricule")
        choix = cls.action_confirm(message, matricule, data)
        while True:
            if choix == "1":
                cls.model.delete(matricule)  # type: ignore
                break
            elif choix == "2":
                sys.exit(0)
                return 0
            else:
                print(cls.MSG_INVALID_OPTION)
                print("1. Oui")
                print("2. Non")
                choix = input("Choisissez une option (1-2) :       ")

    @classmethod
    def action_confirm(cls, message, matricule, data):
        """
        Méthode pour demander une confirmation d'action.

        Args:
            message (str): Le message de confirmation.
            matricule (int): Le matricule associé à l'action.
            data (list): Liste des données existantes.

        Returns:
            str: Le choix de l'utilisateur (1 pour oui, 2 pour non).
        """
        # ...
        print("")
        print("")
        print(message)
        while not cls.show_where_id(cls.model, matricule, data):
            matricule = cls.write_number("matricule")
            print("")
            print("")
            print(message)

        print("?")
        print("")
        print("")
        print("1. Oui")
        print("2. Non")
        choix = input("Choisissez une option (1-2) :       ")
        return choix

    @classmethod
    def write_text(cls, name):
        """
        Méthode pour saisir un texte valide.

        Args:
            name (str): Le nom associé à la saisie.

        Returns:
            str: Le texte saisi.
        """
        # ...
        text = input(f"Ecrire {name} de {cls.model.relation} :       ")  # type: ignore
        while not validate_text(text):
            print(cls.MSG_INVALID_TEXT)
            text = input(f"Ecrire {name} de {cls.model.relation} :       ")  # type: ignore
        return text

    @classmethod
    def write_number(cls, name):
        """
        Méthode pour saisir un nombre valide.

        Args:
            name (str): Le nom associé à la saisie.

        Returns:
            int: Le nombre saisi.
        """
        # ...
        number = input(f"Ecrire {name} de {cls.model.relation} :       ")  # type: ignore
        while not validate_number(number):
            print(cls.MSG_INVALID_NUMBER)
            number = input(f"Ecrire {name} de {cls.model.relation} :       ")  # type: ignore
        return int(number)

    @classmethod
    def write_date(cls, name):
        """
        Méthode pour saisir une date valide.

        Args:
            name (str): Le nom associé à la saisie.

        Returns:
            datetime.date: La date saisie.
        """
        # ...
        date = input(f"Ecrire {name} de {cls.model.relation} :  aaaa-mm-dd     ")  # type: ignore
        while not validate_date(date):
            print(cls.MSG_INVALID_DATE)
            date = input(f"Ecrire {name} de {cls.model.relation} :       ")  # type: ignore
        data = date.split("-")
        annee = int(data[0])
        mois = int(data[1])
        jour = int(data[2])
        return datetime(annee, mois, jour).date()  # type: ignore

    @classmethod
    def write_phone_number(cls, name):
        """
        Méthode pour saisir un numéro de téléphone valide.

        Args:
            name (str): Le nom associé à la saisie.

        Returns:
            int: Le numéro de téléphone saisi.
        """
        # ...
        phone_number = input(f"Ecrire {name} de {cls.model.relation} :       ")  # type: ignore
        while not validate_phone_number(phone_number):
            print(cls.MSG_INVALID_NUMBER)
            phone_number = input(f"Ecrire {name} de {cls.model.relation} :       ")  # type: ignore
        return int(phone_number)

    @staticmethod
    def show(model):
        """
        Méthode pour afficher les données.

        Args:
            model (object): Le modèle de données.

        Returns:
            list: Les données affichées.
        """
        # ...
        data = model.select_all()
        table_name = model.relation.capitalize()

        if len(data) == 0:
            print(f"Rien de '{table_name}' enregistré")
            return

        columns = model.get_columns()
        column_widths = [14] * len(columns)

        Controller.print_head(columns, column_widths, table_name)

        datetime_string_format = "%b %d %Y"
        uneListe = []
        for elt in data:
            tuplet = tuple()
            for value in elt:
                if type(value) == type(datetime(2000, 1, 1).date()):  # type: ignore
                    value = datetime.strftime(value, datetime_string_format)  # type: ignore
                tuplet += (value,)
            elt = tuplet
            uneListe.append(elt)
            row_format = " | ".join(
                ["{{:<{}}}".format(width) for width in column_widths]
            )
            print(row_format.format(*elt))
        data = uneListe
        return data

    @staticmethod
    def show_where_id(model, matricule, alldata):
        """
        Méthode pour afficher les données correspondant à un ID spécifique.

        Args:
            model (object): Le modèle de données.
            matricule (int): L'identifiant à rechercher.
            alldata (list): Liste des données existantes.

        Returns:
            int: 1 si l'ID correspond, 0 sinon.
        """
        # ...
        ids = [t[0] for t in alldata]
        while matricule not in ids:
            print(f"l'id  ne correspond a aucun {model.relation}, Veuillez réessayer")
            return 0
        data = tuple(filter(lambda x: x[0] == matricule, [t for t in alldata]))[0]
        table_name = model.relation.capitalize()

        columns = model.get_columns()
        column_widths = [14] * len(columns)

        Controller.print_head(columns, column_widths, table_name)

        row_format = " | ".join(["{{:<{}}}".format(width) for width in column_widths])
        print(row_format.format(*data))
        return 1

    @staticmethod
    def print_head(columns, column_widths, table_name):
        """
        Méthode pour afficher l'en-tête du tableau de données.

        Args:
            columns (list): Liste des noms de colonnes.
            column_widths (list): Liste des largeurs des colonnes.
            table_name (str): Nom de la table de données.
        """
        # ...
        print("=" * (sum(column_widths) + 3 * len(columns) + 1))  # type: ignore
        print(f"{table_name:^{sum(column_widths) + 3 * len(columns) + 1}}")  # type: ignore
        print("=" * (sum(column_widths) + 3 * len(columns) + 1))  # type: ignore

        header_format = " | ".join(
            ["{{:<{}}}".format(width) for width in column_widths]
        )
        print(header_format.format(*columns))  # type: ignore

        separator = "-" * (sum(column_widths) + 3 * len(columns) + 1)  # type: ignore
        print(separator)

    @classmethod
    def update(cls, attribut, result):
        """
        Méthode pour mettre à jour des données existantes.

        Args:
            attribut (str): L'attribut à mettre à jour.
            result (any): La nouvelle valeur de l'attribut.

        Returns:
            int: 0 si l'opération est annulée.
        """
        # ...
        data = cls.show(cls.model)
        matricule = cls.write_number(cls.model.primary_key)  # type: ignore
        message = f"Etes vous sur de vouloir mettre à jour les donnée de {cls.model.relation}  :"  # type: ignore

        choix = cls.action_confirm(message, matricule, data)
        while True:
            if choix == "1":
                cls.model.update(attribut, matricule, result)  # type: ignore
                break
            elif choix == "2":
                return 0
            else:
                print(cls.MSG_INVALID_OPTION)
                print("1. Oui")
                print("2. Non")
                choix = input("Choisissez une option (1-2) :       ")

    @classmethod
    def read(cls, attribut, phone_attribut=False, values=None):
        """
        Méthode pour lire une valeur spécifique.

        Args:
            attribut (str): L'attribut à lire.
            phone_attribut (bool): Indique si l'attribut est un numéro de téléphone.
            values (list): Liste des valeurs possibles (facultatif).

        Returns:
            any: La valeur lue.
        """
        # ...
        result = str()
        position = int()
        invalid_message_type = cls.MSG_INVALID_OPTION
        if values is None:
            if not phone_attribut:
                column_type = cls.model.get_colunm_type(attribut)  # type: ignore
                if column_type == "integer":
                    result = cls.write_number(attribut)
                    invalid_message_type = cls.MSG_INVALID_NUMBER
                elif column_type == "varchar":
                    result = cls.write_text(attribut)
                    invalid_message_type = cls.MSG_INVALID_TEXT
                elif column_type == "date":
                    result = cls.write_date(attribut)
                    invalid_message_type = cls.MSG_INVALID_DATE
            else:
                result = cls.write_phone_number(attribut)
                invalid_message_type = cls.MSG_INVALID_NUMBER
        else:
            for position, value in enumerate(values, start=1):
                print(f"{position}. {value}")
            choix = input(f"Choisissez une option (1-{position-1}) :        ")
            is_done = 0
            while not is_done:
                for i in range(1, len(values) + 1):
                    if choix == str(i):
                        result = values[i - 1]
                        is_done = 1
                        break
                if is_done:
                    continue
                else:
                    print(invalid_message_type)
                    position = 1
                    for value in values:
                        print(f"{ position}. {value}")
                        position = position + 1
                    choix = input(f"Choisissez une option (1-{position-1}) :        ")

        return result

    @classmethod
    def assign(cls, reference):
        """
        Méthode pour assigner une référence à une entrée existante.

        Args:
            reference (object): La référence à assigner.

        Returns:
            tuple: L'identifiant assigné et les données correspondantes.
        """
        # ...
        data = cls.show(reference)
        ids = [t[0] for t in data]
        identifiant = cls.write_number(f"id {reference.relation} ")
        while identifiant not in ids:
            print(f"l'id {identifiant} ne correspond a aucune {reference.relation}")
            identifiant = cls.write_number(f"id {reference.relation} ")
        return identifiant, data


if __name__ == "__main__":
    print(dir())