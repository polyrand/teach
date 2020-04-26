from pathlib import Path

def carpeta_ssh():
  """Funcion que devuelve ruta de configuracion ssh."""
  return Path.home() / ".ssh"