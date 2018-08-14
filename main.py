import click


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def execute(count, name):
    """Simple program that generates sample YAML file."""
    click.echo('name: %s' % name)
    click.echo('count: %s' % count)
    click.echo('Generated YAML file.')


if __name__ == '__main__':
    execute()
