from config.config import client_type, key
from helpers.utils import get_llm_client

if __name__ == "__main__":

    client = get_llm_client(client_type, key)

    # Première question
    response1 = client.ask("Quelle est la capitale de la France ?")
    print("Assistant:", response1)  # Attendu: "La capitale de la France est Paris."

    # Deuxième question, le modèle doit comprendre le contexte
    response2 = client.ask("Quel est la population de cette ville ?")
    print("Assistant:", response2)  # Attendu: Données sur la population de Paris
