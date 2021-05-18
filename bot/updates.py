import requests


class Updates:
    @staticmethod
    def get_update_messages(base_url: str):
        target_uri = f'{base_url}/getUpdates'
        return requests.get(target_uri).json()

    @staticmethod
    def clear_replied_messages(base_url, update_id):
        target_uri = f'{base_url}/getUpdates?offset={update_id}'
        requests.get(target_uri)
