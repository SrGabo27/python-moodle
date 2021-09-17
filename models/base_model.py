"""This module contains the base configuration
to make requests against moodle webservice"""
from enum import Enum
from typing import Dict


class MoodleFunction(Enum):
    """Moodle webservice functions enum"""

    CORE_USER_GET_USERS = "core_user_get_users"
    CORE_USER_CREATE_USERS = "core_user_create_users"
    CORE_COURSE_CREATE_COURSES = "core_course_create_courses"
    CORE_COURSE_GET_COURSES = "core_course_get_courses"
    ENROL_MANUAL_ENROL_USERS = "enrol_manual_enrol_users"
    LOCAL_WSGETROLES_GET_ROLES = "local_wsgetroles_get_roles"


class BaseModel:
    """Base model with the url configuration,
    all the models interacting with moodle must inherit from this class"""

    _moodle_url: str
    _token: str
    _url: str = "undefined"

    def __init__(self, moodle_url: str, token: str):
        self._moodle_url = moodle_url
        self._token = token

    def set_function(self, function: MoodleFunction) -> None:
        """Defines the moodle function to call"""
        self._url = f"{self._moodle_url}?&wstoken={self._token}\
        &moodlewsrestformat=json&wsfunction={function.value}"

    def send_request(self, function: MoodleFunction, payload: Dict) -> None:
        """Defines the moodle function to call"""
        self._url = f"{self._moodle_url}?&wstoken={self._token}\
        &moodlewsrestformat=json&wsfunction={function.value}"
