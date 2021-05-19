import abc

import requests
from bot.file import prepare_file


class Message(abc.ABC):
    @abc.abstractmethod
    def send(self, chat_id: str, base_url: str) -> None:
        pass


class TextMessage(Message):
    def __init__(self, text):
        self.text = text
        self.path = '/sendMessage'

    def send(self, chat_id: str, base_url: str) -> None:
        target_uri = f'{base_url}{self.path}?chat_id={chat_id}&text={self.text}&parse_mode=HTML'
        requests.get(target_uri)


class ImageMessage(Message):
    def __init__(self, image_path, text):
        self.image_path = image_path
        self.text = text
        self.path = '/sendPhoto'

    def send(self, chat_id: str, base_url: str) -> None:
        target_uri = f'{base_url}{self.path}'
        multipart_data = prepare_file(self.image_path, self.text, chat_id, 'photo')

        requests.post(
            target_uri,
            data=multipart_data,
            headers={'Content-Type': multipart_data.content_type}
        )


class VideoMessage(Message):
    def __init__(self, video_path, text):
        self.video_path = video_path
        self.text = text
        self.path = '/sendVideo'

    def send(self, chat_id: str, base_url: str) -> None:
        target_uri = f'{base_url}{self.path}'
        multipart_data = prepare_file(self.video_path, self.text, chat_id, 'video')

        requests.post(
            target_uri,
            data=multipart_data,
            headers={'Content-Type': multipart_data.content_type}
        )


class AudioMessage(Message):
    def __init__(self, audio_path, text):
        self.audio_path = audio_path
        self.text = text
        self.path = '/sendAudio'

    def send(self, chat_id: str, base_url: str) -> None:
        target_uri = f'{base_url}{self.path}'
        multipart_data = prepare_file(self.audio_path, self.text, chat_id, 'audio')

        requests.post(
            target_uri,
            data=multipart_data,
            headers={'Content-Type': multipart_data.content_type}
        )


class DocumentMessage(Message):
    def __init__(self, document_path, text):
        self.document_path = document_path
        self.text = text
        self.path = '/sendDocument'

    def send(self, chat_id: str, base_url: str) -> None:
        target_uri = f'{base_url}{self.path}'
        multipart_data = prepare_file(self.document_path, self.text, chat_id, 'document')

        requests.post(
            target_uri,
            data=multipart_data,
            headers={'Content-Type': multipart_data.content_type}
        )


class LocationMessage(Message):
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.path = '/sendLocation'

    def send(self, chat_id: str, base_url: str) -> None:
        target_uri = f'{base_url}{self.path}?chat_id={chat_id}&latitude={self.latitude}&longitude={self.longitude}'
        requests.get(target_uri)
