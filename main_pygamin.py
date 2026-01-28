#!/usr/bin/python3
Pyjama = __import__('exercice_pygamin').Pyjama


def main():
    # Création des pyjamas
    pyjama_jaune = Pyjama()
    pyjama_bleu = Pyjama("bleu", "soie", "XXL")
    pyjama_bordeau = Pyjama("bordeau", "velour", "XL")

    print("\n--- Julie ---")
    pyjama_jaune.acheter()

    print("\n--- Tom ---")
    pyjama_bleu.acheter()
    pyjama_bleu.vendre()

    print("\n--- Sophie ---")
    pyjama_bordeau.acheter()
    pyjama_bordeau.laver(pyjama_bordeau)


if __name__ == "__main__":
    main()
