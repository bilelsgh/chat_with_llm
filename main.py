from clients.base import AvailableClients
from clients.mistral import MistralClient
from config.config import client_type, key, model_name

if __name__ == "__main__":

    clients = {AvailableClients.MISTRAL: MistralClient}
    client = clients[client_type](model_name=model_name, key=key)

    print(client.ask("Hello"))
