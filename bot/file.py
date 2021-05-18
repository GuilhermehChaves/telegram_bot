import mimetypes

from requests_toolbelt.multipart.encoder import MultipartEncoder


def prepare_file(path: str, text: str, chat_id: str, file_type: str) -> MultipartEncoder:
    parts = path.split('.')

    last_index = len(parts) - 1
    file_extension = '.{}'.format(parts[last_index])

    mime = mimetypes.types_map(file_extension)

    return MultipartEncoder(
        fields={
            f'{file_type}': (path, open(path, 'rb'), mime),
            'chat_id': chat_id,
            'caption': text
        }
    )
