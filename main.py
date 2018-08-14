import click
from generator import YamlGenerator


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--project_name', prompt='Your project name', help='The project\'s name.')
def execute(count, project_name):
    """Simple program that generates sample YAML file."""
    YamlGenerator().execute(project_name)
    click.echo('Created output.yml.')


if __name__ == '__main__':
    execute()
