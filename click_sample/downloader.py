import io
import os
import zipfile

import requests


class Downloader(object):
    def download_framework(self, app_name: str):
        branch = 'master'
        repo_name = "pipeline-framework"
        url = 'https://github.com/Innovatube/' + repo_name + '/archive/' + branch + '.zip'
        request = requests.get(url, stream=True)
        zip = zipfile.ZipFile(io.BytesIO(request.content))
        zip.extractall()
        os.rename(repo_name + "-" + branch, app_name)
        zip.close()
