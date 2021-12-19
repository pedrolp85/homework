from typer.testing import CliRunner
from util import app

runner = CliRunner()

def test_inputfile_not_exists():
    result = runner.invoke(
        app, ["tests/test_files/noexists.log", "--first", 11, "--last", 11]
    )
    assert result.exit_code == 2
    assert "The File provided does not exist" in result.stdout
    print(result.stdout)

def test_inputfile_not_exists_absolute():
    result = runner.invoke(
        app, ["/tests/test_files/noexists.log", "--first", 11, "--last", 11]
    )
    assert result.exit_code == 2
    assert "The File provided does not exist" in result.stdout
    print(result.stdout)

def test_inputfile_absolute():
    result = runner.invoke(
        app, ["/etc/ssh/ssh_config", "--first", 1]
    )
    assert result.exit_code == 0
    print(result.stdout)

def test_inputfile_no_permission():
    result = runner.invoke(
        app, ["/etc/shadow", "--first", 1]
    )
    print(result.stdout)
    assert result.exit_code == 2
    assert "Permission denied to operate the file" in result.stdout