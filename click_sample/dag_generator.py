import shutil, os


class DagGenerator(object):
    def __init__(self):
        pass

    def execute(self, app_name: str, dag_name: str) -> None:
        work_dir = os.getcwd()
        template_dir = work_dir + '/click_sample/templates'
        src_path = template_dir + '/dag.py'
        dest_path = work_dir + '/' + app_name + '/airflow/dags/' + dag_name + '.py'
        shutil.copy(src_path, dest_path)
