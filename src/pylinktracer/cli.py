# outil ligne de commande pour pylinktracer
import argparse


def main():
    parser = argparse.ArgumentParser(description="Pylinktracer command line interface")

    # argument positionnel obligatoire pour l'URL à analyser
    parser.add_argument("url", help="URL to investigate")
    args = parser.parse_args()
    print("Pylinktracer CLI executed with arguments:", args)


# Permet d'exécuter ce fichier directement
if __name__ == "__main__":
    main()
