from typing import List
import requests
from base_model import BaseModel, MoodleFunction


class User:
    """Moodle user"""
    def __init__(
        self,
        firstname: str,
        lastname: str,
        email: str,
        password: str,
        city: str,
        country: str,
        auth: str = "manual",
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.username = f"{firstname}.{lastname}".lower()
        self.email = email
        self.password = password
        self.city = city
        self.country = country
        self.auth = auth


class UserModel(BaseModel):
    """Class with all the moodle user requests"""
    def find_all(self) -> List[User]:
        """Return a all the users registered in moodle"""

        self.set_function(MoodleFunction.CORE_USER_GET_USERS)

        response = requests.get(self._url,
                                params={
                                    "criteria[0][key]": "",
                                    "criteria[0][value]": ""
                                })

        if response.status_code != 200:
            return {"ok": "false"}

        return response.json()["users"]

    def create(self, user: User) -> None:
        """Creates an user on moodle"""

        self.set_function(MoodleFunction.CORE_USER_CREATE_USERS)

        user_data = {
            "users[0][username]": user.username,
            "users[0][auth]": user.auth,
            "users[0][password]": user.password,
            "users[0][firstname]": user.firstname,
            "users[0][lastname]": user.lastname,
            "users[0][email]": user.email,
            "users[0][city]": user.city,
            "users[0][country]": user.country,
        }
        print(user_data)

        response = requests.get(self._url, params=user_data)
        print(response.json())

    def find_by_id(self, user_id: int) -> None:
        """Finds a user from moodle"""

        self.set_function(MoodleFunction.CORE_USER_GET_USERS)

        response = requests.post(self._url,
                                 params={
                                     "criteria[0][key]": "id",
                                     "criteria[0][value]": user_id
                                 })

        return response.json()["users"][0]


userModel = UserModel(
    "https://devtransformate.ciexpro.website/webservice/rest/server.php",
    "01d06e8754a3e3f1c13b627b9a6f66d3",
)
print(userModel.find_all())
gabriel = User("Test", "Api", "wotirah850@quossum.com", "Estelio01.",
               "Caracas", "VE")
