import pytest

from ibge.localidades import Regioes


@pytest.fixture
def region_data():
    return [
        {"id": 1, "sigla": "N", "nome": "Norte"},
        {"id": 2, "sigla": "NE", "nome": "Nordeste"},
        {"id": 3, "sigla": "SE", "nome": "Sudeste"},
        {"id": 4, "sigla": "S", "nome": "Sul"},
        {"id": 5, "sigla": "CO", "nome": "Centro-Oeste"},
    ]


def test_deve_retornar_200(region_data):
    region = Regioes()
    expect = region_data
    result = region.json()

    assert expect == result
