import config
from pathlib import Path


def test_carpeta_ssh(monkeypatch):

  def mock_return(*args, **kwargs):
    return Path("/abc")

  monkeypatch.setattr(Path, "home", mock_return)

  x = config.carpeta_ssh()

  assert x == Path("/abc/.ssh")