from typing import List
import requests
from base_model import BaseModel, MoodleFunction


class Course:
    """Moodle course"""
    def __init__(self, fullname: str, shortname: str, category_id: int):
        self.fullname = fullname
        self.shortname = shortname
        self.category_id = category_id


class CourseModel(BaseModel):
    """All the moodle courses requests"""
    def find_all(self) -> List[Course]:
        """Get all the courses"""

        self.set_function(MoodleFunction.CORE_COURSE_GET_COURSES)

        response = requests.get(self._url)

        return response.json()

    def create(self, course: Course) -> List[Course]:
        """Create a new course"""

        self.set_function(MoodleFunction.CORE_COURSE_CREATE_COURSES)

        course_data = {
            "courses[0][fullname]": course.fullname,
            "courses[0][shortname]": course.shortname,
            "courses[0][categoryid]": course.category_id,
        }

        response = requests.post(self._url, params=course_data)

        print(response.json())

    def enrol(self, user_id: int, role_id: int, course_id: int) -> None:
        """Enrol a user in a course"""
        # The student role id is 5

        enrolment_data = {
            "enrolments[0][roleid]": role_id,
            "enrolments[0][userid]": user_id,
            "enrolments[0][courseid]": course_id,
        }

        self.set_function(MoodleFunction.ENROL_MANUAL_ENROL_USERS)
        response = requests.post(self._url, params=enrolment_data)

        print(response.json())


courseModel = CourseModel(
    "https://devtransformate.ciexpro.website/webservice/rest/server.php",
    "01d06e8754a3e3f1c13b627b9a6f66d3",
)

new_course = Course("Curso de prueba teletrabajo", "testcourseteletrabajo", 10)

#  courseModel.create(new_course)

#  print(courseModel.find_all())

courseModel.enrol(47, 5, 3)
