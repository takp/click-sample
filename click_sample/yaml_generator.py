from typing import Any

import yaml


class YamlGenerator(object):
    def __init__(self) -> None:
        pass

    def execute(self, project_name) -> Any:
        data = dict(
            version='1.0',
            project=project_name,
            services=dict(
                service_a='framework_a',
                service_b='framework_b',
                service_c='framework_c',
            ))
        with open('settings.yml', 'w') as outfile:
            yaml.dump(data, outfile, default_flow_style=False)
