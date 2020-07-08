import requests
import app

class MockDatos:

  @staticmethod
  def json():
    return {"mock_key": "respuestamockeada"}


def test_bajar_datos(monkeypatch):

  def mock_get(*args, **kwargs):
    return MockDatos()

  monkeypatch.setattr(requests, "get", mock_get)

  resultado = app.bajar_datos("http://pythonatope.com")

  assert resultado["mock_key"] == "respuestamockeada"
