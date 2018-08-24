import click

from click_sample import Downloader, YamlGenerator


@click.command()
@click.option('--app_name', prompt="Your application name", help='Name of application')
@click.option('--dag_name', prompt="Your task name", help='Name of task')
def execute(app_name, dag_name):
    """Simple program that generates sample YAML file."""
    Downloader().download_framework(app_name)
    YamlGenerator().execute(app_name)
    click.echo('Created output.yml.')


if __name__ == '__main__':
    execute()
