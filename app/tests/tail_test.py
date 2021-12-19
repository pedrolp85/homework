from typer.testing import CliRunner
from util import app

runner = CliRunner()


def test_tail_1():
    result = runner.invoke(app, ["tests/test_files/intersection.log", "--last", 5])
    assert result.exit_code == 0
    assert "L22" in result.stdout
    assert "L18" in result.stdout
    assert "L17" not in result.stdout
    print(result.stdout)


def test_tail_2():
    result = runner.invoke(app, ["tests/test_files/intersection.log", "--last", 0])
    assert result.exit_code == 0
    print(result.stdout)


def test_tail_3():
    result = runner.invoke(app, ["tests/test_files/intersection.log", "--last", -5])
    assert result.exit_code == 0
    assert "L1" in result.stdout
    assert "L5" in result.stdout
    assert "L6" not in result.stdout
    print(result.stdout)


def test_tail_4():
    result = runner.invoke(app, ["tests/test_files/intersection.log", "--last", 24])
    assert result.exit_code == 0
    assert "L1" in result.stdout
    assert "L2" in result.stdout
    print(result.stdout)


def test_tail_5():
    result = runner.invoke(app, ["tests/test_files/intersection.log", "--last", -24])
    assert result.exit_code == 0
    assert "L1" in result.stdout
    assert "L22" in result.stdout
    print(result.stdout)
