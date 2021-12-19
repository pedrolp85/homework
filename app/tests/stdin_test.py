from typer.testing import CliRunner
from util import app

runner = CliRunner()


def test_stdin():

    result = runner.invoke(app, ["--ipv4", "172.16.0.14"], input="172.16.0.14\n")
    assert result.exit_code == 0
    print(result.stdout)
    assert "172.16.0.14" in result.stdout
