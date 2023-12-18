from typing import Union

from pyrogram.types import Animation, Audio, Document, Photo, Sticker, Video

from Hellbot.core import Symbols


async def get_metedata(
    media: Union[
        Animation,
        Audio,
        Document,
        Photo,
        Sticker,
        Video
    ]
):
    output = "📄 MetaData:\n\n"
    if isinstance(media, Animation):
        output += f"<b>{Symbols.diamond_2} File ID:</b> <code>{media.file_id}</code>\n"
        output += f"<b>{Symbols.diamond_2} Width:</b> <code>{media.width}</code>\n"
        output += f"<b>{Symbols.diamond_2} Height:</b> <code>{media.height}</code>\n"
        output += f"<b>{Symbols.diamond_2} Duration:</b> <code>{media.duration}</code>\n"
        output += f"<b>{Symbols.diamond_2} File Name:</b> <code>{media.file_name}</code>\n"
        output += f"<b>{Symbols.diamond_2} Mime Type:</b> <code>{media.mime_type}</code>\n"
        output += f"<b>{Symbols.diamond_2} File Size:</b> <code>{media.file_size}</code>\n"
        output += f"<b>{Symbols.diamond_2} Date:</b> <code>{media.date}</code>\n"
        output += f"<b>{Symbols.diamond_2} File Type:</b> <code>Animation</code>\n"
    elif isinstance(media, Audio):
        output += f"<b>{Symbols.diamond_2} File ID:</b> <code>{media.file_id}</code>\n"
        output += f"<b>{Symbols.diamond_2} Duration:</b> <code>{media.duration}</code>\n"
        output += f"<b>{Symbols.diamond_2} Performer:</b> <code>{media.performer}</code>\n"
        output += f"<b>{Symbols.diamond_2} Title:</b> <code>{media.title}</code>\n"
        output += f"<b>{Symbols.diamond_2} File Name:</b> <code>{media.file_name}</code>\n"
        output += f"<b>{Symbols.diamond_2} Mime Type:</b> <code>{media.mime_type}</code>\n"
        output += f"<b>{Symbols.diamond_2} File Size:</b> <code>{media.file_size}</code>\n"
        output += f"<b>{Symbols.diamond_2} Date:</b> <code>{media.date}</code>\n"
        output += f"<b>{Symbols.diamond_2} File Type:</b> <code>Audio</code>\n"
    elif isinstance(media, Document):
        output += f"<b>{Symbols.diamond_2} File ID:</b> <code>{media.file_id}</code>\n"
        output += f"<b>{Symbols.diamond_2} File Name:</b> <code>{media.file_name}</code>\n"
        output += f"<b>{Symbols.diamond_2} Mime Type:</b> <code>{media.mime_type}</code>\n"
        output += f"<b>{Symbols.diamond_2} File Size:</b> <code>{media.file_size}</code>\n"
        output += f"<b>{Symbols.diamond_2} Date:</b> <code>{media.date}</code>\n"
        output += f"<b>{Symbols.diamond_2} File Type:</b> <code>Document</code>\n"
    elif isinstance(media, Photo):
        output += f"<b>{Symbols.diamond_2} File ID:</b> <code>{media.file_id}</code>\n"
        output += f"<b>{Symbols.diamond_2} Width:</b> <code>{media.width}</code>\n"
        output += f"<b>{Symbols.diamond_2} Height:</b> <code>{media.height}</code>\n"
        output += f"<b>{Symbols.diamond_2} File Name:</b> <code>photo.jpg</code>\n"
        output += f"<b>{Symbols.diamond_2} Mime Type:</b> <code>image/jpeg</code>\n"
        output += f"<b>{Symbols.diamond_2} File Size:</b> <code>{media.file_size}</code>\n"
        output += f"<b>{Symbols.diamond_2} Date:</b> <code>{media.date}</code>\n"
        output += f"<b>{Symbols.diamond_2} File Type:</b> <code>Photo</code>\n"
    elif isinstance(media, Sticker):
        output += f"<b>{Symbols.diamond_2} File ID:</b> <code>{media.file_id}</code>\n"
        output += f"<b>{Symbols.diamond_2} Width:</b> <code>{media.width}</code>\n"
        output += f"<b>{Symbols.diamond_2} Height:</b> <code>{media.height}</code>\n"
        output += f"<b>{Symbols.diamond_2} File Name:</b> <code>{media.file_name}</code>\n"
        output += f"<b>{Symbols.diamond_2} Mime Type:</b> <code>{media.mime_type}</code>\n"
        output += f"<b>{Symbols.diamond_2} File Size:</b> <code>{media.file_size}</code>\n"
        output += f"<b>{Symbols.diamond_2} Date:</b> <code>{media.date}</code>\n"
        output += f"<b>{Symbols.diamond_2} Emoji:</b> <code>{media.emoji}</code>\n"
        output += f"<b>{Symbols.diamond_2} Set Name:</b> <code>{media.set_name}</code>\n"
        output += f"<b>{Symbols.diamond_2} File Type:</b> <code>Sticker</code>\n"
    elif isinstance(media, Video):
        output += f"<b>{Symbols.diamond_2} File ID:</b> <code>{media.file_id}</code>\n"
        output += f"<b>{Symbols.diamond_2} Width:</b> <code>{media.width}</code>\n"
        output += f"<b>{Symbols.diamond_2} Height:</b> <code>{media.height}</code>\n"
        output += f"<b>{Symbols.diamond_2} Duration:</b> <code>{media.duration}</code>\n"
        output += f"<b>{Symbols.diamond_2} File Name:</b> <code>{media.file_name}</code>\n"
        output += f"<b>{Symbols.diamond_2} Mime Type:</b> <code>{media.mime_type}</code>\n"
        output += f"<b>{Symbols.diamond_2} File Size:</b> <code>{media.file_size}</code>\n"
        output += f"<b>{Symbols.diamond_2} Date:</b> <code>{media.date}</code>\n"
        output += f"<b>{Symbols.diamond_2} File Type:</b> <code>Video</code>\n"
    else:
        return None

    return output
