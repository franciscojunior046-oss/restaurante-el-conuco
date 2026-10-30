import pytest
from app.utils.validators import texto_obligatorio, numero_positivo

def test_texto_obligatorio():
    assert texto_obligatorio(" Junior ", "nombre") == "Junior"

def test_texto_vacio():
    with pytest.raises(ValueError):
        texto_obligatorio(" ", "nombre")

def test_numero_positivo():
    assert numero_positivo("4", "capacidad") == 4
