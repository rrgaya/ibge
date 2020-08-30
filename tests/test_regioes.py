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


def test_deve_retornar_o_json_contendo_todas_as_regios_cadastradas_no_ibge(region_data):
    regiao = Regioes()
    esperado = region_data
    resultado = regiao.json()
    assert esperado == resultado