import click

from click_sample import Downloader, YamlGenerator, DagGenerator


@click.command()
@click.option('--file', help='YAML file path', default='')
def execute(file: str):
    if file:
        execute_with_file(file)
    else:
        execute_with_prompt()


def execute_with_file(file: str) -> None:
    """
    Fetch arguments from YAML file.

    :param file: YAML file path
    """
    print(file)


@click.command()
@click.option('--app_name', prompt="Your application name", help='Name of application')
@click.option('--dag_name', prompt="Your task name", help='Name of task')
def execute_with_prompt(app_name: str, dag_name: str) -> None:
    """
    Execute with prompt.

    :param app_name: Application name
    :param dag_name: DAG name
    :return:
    """
    YamlGenerator().execute(app_name, dag_name)
    Downloader().download_framework(app_name)
    DagGenerator().execute(app_name, dag_name)
    click.echo('Created output.yml.')


if __name__ == '__main__':
    execute()
