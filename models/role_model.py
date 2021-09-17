from typing import List
from base_model import BaseModel, MoodleFunction
import requests


class Role:
    def __init__(self, name: str):
        self.name = name


class RoleModel(BaseModel):
    """Class with all the moodle Role rquests"""
    def find_all(self) -> List[Role]:
        """Returns all the moodle roles"""
        self.set_function(MoodleFunction.LOCAL_WSGETROLES_GET_ROLES)

        response = requests.get(self._url)

        return response.json()


role_model = RoleModel(
    "https://devtransformate.ciexpro.website/webservice/rest/server.php",
    "01d06e8754a3e3f1c13b627b9a6f66d3",
)

print(role_model.find_all())
