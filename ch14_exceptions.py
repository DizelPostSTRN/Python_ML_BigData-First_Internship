class AgeNotInRange(Exception):
    pass


class PersonTooOld(AgeNotInRange):
    pass


class PersonNotAlive(AgeNotInRange):
    pass


def retrieve_age(person):
    try:
        age = int(person["age"])
        if 0 < age < 100:
            return age
        if 100 < age < 123:
            raise PersonTooOld(f"The age of person is {age}. Person too old")
        if age > 122:
            raise PersonNotAlive(f"The age of person is {age}. Today there are no people of this age")
    except (ValueError, KeyError, AgeNotInRange) as e:
        print(f"{e.__class__.__name__}: {e}")


print(retrieve_age({"age": 45}))
print(retrieve_age({"a": 45}))
print(retrieve_age({"age": "hdfsdjhfjskd"}))
print(retrieve_age({"age": 145}))
print(retrieve_age({"age": 110}))
