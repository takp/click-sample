import click
from generator import YamlGenerator
import requests, zipfile, io, os


@click.command()
@click.option('--app_name', prompt="Your application name", help='Name of application')
def execute(app_name):
    """Simple program that generates sample YAML file."""
    download_framework(app_name)
    YamlGenerator().execute(app_name)
    click.echo('Created output.yml.')


def download_framework(app_name: str):
    branch = 'master'
    url = 'https://github.com/Innovatube/pipeline-framework/archive/' + branch + '.zip'
    request = requests.get(url, stream=True)
    zip = zipfile.ZipFile(io.BytesIO(request.content))
    zip.extractall()
    os.rename("pipeline-framework-" + branch, app_name)
    zip.close()


if __name__ == '__main__':
    execute()
