import click

from click_sample import Downloader, YamlGenerator, DagGenerator


@click.command()
@click.option('--app_name', prompt="Your application name", help='Name of application')
@click.option('--dag_name', prompt="Your task name", help='Name of task')
def execute(app_name, dag_name):
    """Simple program that generates sample YAML file."""
    YamlGenerator().execute(app_name)
    Downloader().download_framework(app_name)
    DagGenerator().execute(app_name, dag_name)
    click.echo('Created output.yml.')


if __name__ == '__main__':
    execute()
