class AgeNotInRange(Exception):
    def __init__(self, message):
        super().__init__(message)


class PersonTooOld(AgeNotInRange):
    def __init__(self, age):
        super().__init__(message=f"The age of person is {age}. Person too old")


class PersonNotAlive(AgeNotInRange):
    def __init__(self, age):
        super().__init__(message=f"The age of person is {age}. Today there are no people of this age")


def retrieve_age(person):
    try:
        age = int(person["age"])
    except ValueError:
        return ValueError("Value not int")
    except KeyError:
        return KeyError("Key of dict not age")
    if 0 < age < 100:
        return age
    elif 100 < age < 123:
        return PersonTooOld(age)
    elif age > 122:
        return PersonNotAlive(age)


print(retrieve_age({"age": 45}))
print(retrieve_age({"a": 45}))
print(retrieve_age({"age": "hdfsdjhfjskd"}))
print(retrieve_age({"age": 145}))
print(retrieve_age({"age": 110}))
