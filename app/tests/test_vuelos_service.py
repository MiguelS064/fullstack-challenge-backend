from unittest.mock import patch, MagicMock
from app.services import vuelos_service


def make_mock_rows(data: list[dict]):
    """Convierte lista de dicts en filas mock con _mapping"""
    rows = []
    for d in data:
        row = MagicMock()
        row._mapping = d
        rows.append(row)
    return rows


def mock_engine_context(rows):
    """
    Crea el mock completo del context manager de engine.connect()
    que usa tu vuelos_service
    """
    mock_result = MagicMock()
    mock_result.__iter__ = lambda self: iter(rows)

    mock_conn = MagicMock()
    mock_conn.execute.return_value = mock_result

    mock_context = MagicMock()
    mock_context.__enter__ = MagicMock(return_value=mock_conn)
    mock_context.__exit__ = MagicMock(return_value=False)

    mock_engine = MagicMock()
    mock_engine.connect.return_value = mock_context

    return mock_engine


def test_top_aeropuerto():
    rows = make_mock_rows([{"nombre_aeropuerto": "Benito Juarez", "total": 5}])
    with patch.object(vuelos_service, "engine", mock_engine_context(rows)):
        result = vuelos_service.top_aeropuerto()
    assert result["data"][0]["nombre_aeropuerto"] == "Benito Juarez"


def test_top_aerolinea():
    rows = make_mock_rows([{"nombre_aerolinea": "Volaris", "total": 4}])
    with patch.object(vuelos_service, "engine", mock_engine_context(rows)):
        result = vuelos_service.top_aerolinea()
    assert result["data"][0]["nombre_aerolinea"] == "Volaris"


def test_top_dia():
    rows = make_mock_rows([{"dia": "2021-05-02", "total": 6}])
    with patch.object(vuelos_service, "engine", mock_engine_context(rows)):
        result = vuelos_service.top_dia()
    assert result["data"][0]["dia"] == "2021-05-02"


def test_aerolineas_mas_2_con_datos():
    rows = make_mock_rows([
        {"nombre_aerolinea": "Aeromar", "dia": "2021-05-02", "total": 3},
    ])
    with patch.object(vuelos_service, "engine", mock_engine_context(rows)):
        result = vuelos_service.aerolineas_mas_2()
    assert len(result["data"]) == 1
    assert result["data"][0]["nombre_aerolinea"] == "Aeromar"


def test_aerolineas_mas_2_sin_datos():
    rows = make_mock_rows([])  # query no retorna nada
    with patch.object(vuelos_service, "engine", mock_engine_context(rows)):
        result = vuelos_service.aerolineas_mas_2()
    assert result["data"] == []