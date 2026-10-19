def check_name(name):
    if not isinstance(name, str) or name.strip() == "":
        raise ValueError("Name must be a non-empty string")
    return name.strip()


def check_id(employee_id):
    if not isinstance(employee_id, int) or employee_id <= 0:
        raise ValueError("Employee ID must be a positive integer")
    return employee_id


def check_non_negative(value, field_name):
    if not isinstance(value, (int, float)) or value < 0:
        raise ValueError(f"{field_name} must be a non-negative number")
    return value