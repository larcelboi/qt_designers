import pytest
from personne import Personne

def test_personne():
    person = Personne("lARCEL",12,"Student")
    assert person.name == "lARCEL"
    assert person.age == 12
    assert person.role == "Student"