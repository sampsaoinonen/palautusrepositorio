from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):        
        content = request.urlopen(self._url).read().decode("utf-8")        
        data = toml.loads(content)

        data_helper = data.get('tool', {}).get('poetry', {})        
        name = data_helper.get('name', 'N/A')
        description = data_helper.get('description', 'N/A')
        dependecies = data_helper.get('dependencies', [])
        dev_dependencies = data_helper.get('group', {}).get('dev', {}).get('dependencies', [])        
        license = data_helper.get('license', 'N/A')
        authors = data_helper.get('authors', [])

        return Project(name, description, dependecies, dev_dependencies, license, authors)
