def build_create_user_payload(user: dict) -> dict:

    return {
        "name": user["name"],
        "email": user["email"],
        "password": user["password"],
        "title": "Mr",
        "birth_date": "10",
        "birth_month": "5",
        "birth_year": "1995",
        "firstname": user["first_name"],
        "lastname": user["last_name"],
        "company": "Automation Company",
        "address1": user["address"],
        "address2": "",
        "country": user["country"],
        "zipcode": user["zipcode"],
        "state": user["state"],
        "city": user["city"],
        "mobile_number": user["mobile_number"],
    }