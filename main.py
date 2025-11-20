"""Outils simples pour vérifier si une chaîne est un palindrome"""

import unicodedata


def ispalindrome(p):
    """Retourne True si la chaîne `p` est un palindrome.
    Args:
        p (str): chaîne d'entrée à tester.

    Returns:
        bool: True si `p` (après normalisation/filtrage) est un palindrome.
    """
    # on met tous les caractères en minuscules
    p = p.lower()

    p = unicodedata.normalize('NFD', p)

    p = ''.join(c for c in p if unicodedata.category(c) != 'Mn')

    pclean = ""
    for c in p:
        if c.isalnum():   # garde seulement lettres + chiffres
            pclean += c
    return pclean == pclean[::-1]


def main():
    """Point d'entrée simple exécutant quelques exemples.

    Affiche pour chaque exemple la chaîne et le résultat du test
    `ispalindrome`.
    """

    # vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
