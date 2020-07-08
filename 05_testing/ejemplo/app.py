import requests

def bajar_datos(url):
  """Hace un GET del endpoint y devuelve JSON."""

  res = requests.get(url)

  return res.json()