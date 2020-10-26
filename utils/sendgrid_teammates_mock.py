import json

def get_a_list_of_teammate():
  return json.dumps({
    "results": [
      {
        "username": "teammate1",
        "email": "teammate1@example.com",
        "first_name": "Jane",
        "last_name": "Doe",
        "user_type": "owner",
        "is_admin": "true",
        "phone": "123-345-3453",
        "website": "www.example.com",
        "company": "ACME Inc.",
        "address": "123 Acme St",
        "address2": "",
        "city": "City",
        "state": "CA",
        "country": "USA",
        "zip": "12345"
      },
      {
        "username": "teammate2",
        "email": "teammate2@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "user_type": "teammate",
        "is_admin": "false",
        "phone": "123-345-3453",
        "website": "www.example.com",
        "company": "ACME Inc.",
        "address": "123 Acme St",
        "address2": "",
        "city": "City",
        "state": "CA",
        "country": "USA",
        "zip": "12345"
      },
      {
        "username": "teammate3",
        "email": "example@example.com",
        "first_name": "Steve",
        "last_name": "Doe",
        "user_type": "admin",
        "is_admin": "true",
        "phone": "123-345-3453",
        "website": "www.example.com",
        "company": "ACME Inc.",
        "address": "123 Acme St",
        "address2": "",
        "city": "City",
        "state": "CA",
        "country": "USA",
        "zip": "12345"
      }
    ]
  })


print(json.loads(get_a_list_of_teammate())["results"][0])
