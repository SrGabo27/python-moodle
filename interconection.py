# Actions in Moodle

functions = {
    1: "core_user_create_users",  # Create users
    2: "core_user_get_users",  # Search for users matching the parameters
    3: "core_user_delete_users",  # Delete users matching the parameters
    4: "core_course_create_courses",  # Create new courses
    5: "core_course_get_courses ",  # Return course details
    6: "core_user_update_users",  # Update users
    7: "core_course_delete_courses",  # Deletes all specifieds courses
    8: "enrol_manual_enrol_users",  # Manual enrol users
    9: "enrol_self_enrol_user",  # Self enrol the given user in the give course
    10: "core_user_update_users",
    # Get courses matching a specific field
    # (id/s, shortname, idnumber, category)
    11: "core_course_get_courses_by_field",
    12: "core_course_get_categories",  # Return category details
    13: "core_role_assign_roles",  # Manual role assignments
}

# One of below dictionaries is sent in the request params

create_users = {
    "users[0][username]": "antonio.rojas",
    "users[0][auth]": "manual",
    "users[0][password]": "*Antonio21*",
    "users[0][firstname]": "Antonio",
    "users[0][lastname]": "Rojas",
    "users[0][email]": "johandre23@hotmail.com",
    "users[0][city]": "Caracas",
    "users[0][country]": "VE",
}

get_users = {
    "criteria[0][key]": "email",
    "criteria[0][value]": "johandre23@estelio.com",
}

update_users = {
    "users[0][id]": 10204,
    "users[0][email]": "johandre23@estelio.com",
    "users[0][lastname]": "Salcedo",
}

delete_users = {"userids[0]": 10193}

create_courses = {
    "courses[0][fullname]": "Curso de prueba 2",
    "courses[0][shortname]": "Prueba",
    "courses[0][categoryid]": 1,
}

get_categories = {
    "criteria[0][key]": "name",
    "criteria[0][value]": "Desarrollo"
}

assign_roles = {"assignments[0][roleid]": 1, "assignments[0][userid]": 10204}

local_url = "https://devacademia.ciexpro.website/webservice/rest/server.php?"

local_token = "1659e88702efd3d648f635ab80d03806"

url = (local_url + "&wstoken=" + local_token + "&moodlewsrestformat=json"
       "&wsfunction=" + function)

response = requests.get(url, params=values)
r = json.loads(response.text)

print(r)
