from typer.testing import CliRunner
from util import app

runner = CliRunner()


def test_valid_timestamp_1():
    result = runner.invoke(
        app, ["tests/test_files/timestamps.log", "--timestamps", "11:11:11"]
    )
    assert result.exit_code == 0
    print(result.stdout)
    assert "11:11:11" in result.stdout


def test_valid_timestamp_2():
    result = runner.invoke(app, ["tests/test_files/timestamps.log", "--timestamps", "12:03:59"])
    assert result.exit_code == 0
    print(result.stdout)
    assert "12:03:59" in result.stdout


def test_valid_timestamp_3():
    result = runner.invoke(app, ["tests/test_files/timestamps.log", "--timestamps", "23:59:59"])
    assert result.exit_code == 0
    print(result.stdout)
    assert "23:59:59" in result.stdout


def test_invalid_timestamp_1():
    result = runner.invoke(app, ["tests/test_files/timestamps.log", "--timestamps", "1:1:1"])
    assert result.exit_code == 2
    print(result.stdout)
    assert "Error: Invalid value" in result.stdout
    assert "not zero padded" in result.stdout

def test_invalid_timestamp_2():
    result = runner.invoke(app, ["tests/test_files/timestamps.log", "--timestamps", "24:53:23"])
    assert result.exit_code == 2
    print(result.stdout)
    assert "Error: Invalid value" in result.stdout

def test_invalid_timestamp_3():
    result = runner.invoke(app, ["tests/test_files/timestamps.log", "--timestamps", "23:61:23"])
    assert result.exit_code == 2
    print(result.stdout)
    assert "Error: Invalid value" in result.stdout

def test_invalid_timestamp_4():
    result = runner.invoke(app, ["tests/test_files/timestamps.log", "--timestamps", "23:41:61"])
    assert result.exit_code == 2
    print(result.stdout)
    assert "Error: Invalid value" in result.stdout

def test_invalid_timestamp_5():
    result = runner.invoke(app, ["tests/test_files/timestamps.log", "--timestamps", "23:4:6"])
    assert result.exit_code == 2
    print(result.stdout)
    assert "Error: Invalid value" in result.stdout
    assert "not zero padded" in result.stdout

def test_invalid_timestamp_6():
    result = runner.invoke(app, ["tests/test_files/timestamps.log", "--timestamps", "23:40:6"])
    assert result.exit_code == 2
    print(result.stdout)
    assert "Error: Invalid value" in result.stdout
    assert "not zero padded" in result.stdout