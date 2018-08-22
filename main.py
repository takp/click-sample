import click
from generator import YamlGenerator


@click.command()
@click.option('--app_name', prompt="Your application name", help='Name of application')
def execute(app_name):
    """Simple program that generates sample YAML file."""
    YamlGenerator().execute(app_name)
    click.echo('Created output.yml.')


if __name__ == '__main__':
    execute()
