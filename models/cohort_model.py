from typing import List
from base_model import BaseModel, MoodleFunction


class CohortModel(BaseModel):
    """Class with all the moodle cohorts requests"""
    def get_all(self):
        """Get all the cohorts"""
        self.set_function(MoodleFunction)
