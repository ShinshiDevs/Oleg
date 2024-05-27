import io
import typing
import zipfile


async def create_memory_zip(files: typing.Dict[str, bytes]) -> io.BytesIO:
    memory_file = io.BytesIO()
    with zipfile.ZipFile(memory_file, "w") as zip_file:
        for name, file in files.items():
            zip_file.writestr(name, file)
    memory_file.seek(0)
    return memory_file
