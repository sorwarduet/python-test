def categorize_by_age(age):
    """
    Categorize a person based on their age.

    Parameters:
    age (int): The age of the person to categorize.

    Returns:
    str: The age category the person belongs to.
    """
    # Define age range constants
    CHILD_MAX = 9
    ADOLESCENT_MAX = 18
    ADULT_MAX = 65
    GOLDEN_AGE_MAX = 150

    if 0 <= age <= CHILD_MAX:
        return "Child"
    elif CHILD_MAX < age <= ADOLESCENT_MAX:
        return "Adolescent"
    elif ADOLESCENT_MAX < age <= ADULT_MAX:
        return "Adult"
    elif ADULT_MAX < age <= GOLDEN_AGE_MAX:
        return "Golden age"
    else:
        return f"Invalid age: {age}"