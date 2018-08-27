import yaml


class YamlGenerator(object):
    def __init__(self) -> None:
        pass

    def execute(self, app_name: str, dag_name: str) -> None:
        data = dict(version='1.0', app_name=app_name, dag_name=dag_name)
        with open('settings.yml', 'w') as outfile:
            yaml.dump(data, outfile, default_flow_style=False)
