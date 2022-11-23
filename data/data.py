from dataclasses import dataclass


@dataclass
class Person:
    FULL_NAME: str = None
    FIRST_NAME: str = None
    LAST_NAME: str = None
    AGE: int = None
    SALARY: int = None
    DEPARTMENT: str = None
    EMAIL: str = None
    CURRENT_ADDRESS: str = None
    PERMANENT_ADDRESS: str = None
