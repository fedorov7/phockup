import json
import shlex
import sys
from subprocess import CalledProcessError, check_output


class Exif(object):
    def __init__(self, file):
        self.file = file

    def data(self):
        try:
            exif_command = (
                "exiftool -time:all -make -model -filename -mimetype -j %s"
                % shlex.quote(self.file)
            )
            if sys.platform == "win32":
                exif_command = exif_command.replace("'", '"')
            data = check_output(exif_command, shell=True).decode("UTF-8")
            exif = json.loads(data)[0]
        except (CalledProcessError, UnicodeDecodeError):
            return None

        return exif
