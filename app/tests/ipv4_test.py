from typer.testing import CliRunner
from util import app

runner = CliRunner()

def test_valid_ipv4_1():
    result = runner.invoke(
        app, ["tests/test_files/ipv4.log", "--ipv4", "127.0.0.1"]
    )
    assert result.exit_code == 0
    print(result.stdout)
    assert "127.0.0.1" in result.stdout

def test_valid_ipv4_2():
    result = runner.invoke(app, ["tests/test_files/ipv4.log", "--ipv4", "192.168.1.1"])
    assert result.exit_code == 0
    print(result.stdout)
    assert "192.168.1.1" in result.stdout

def test_valid_ipv4_3():
    result = runner.invoke(app, ["tests/test_files/ipv4.log", "--ipv4", "192.168.1.255"])
    assert result.exit_code == 0
    print(result.stdout)
    assert "192.168.1.255" in result.stdout

def test_valid_ipv4_4():
    result = runner.invoke(app, ["tests/test_files/ipv4.log", "--ipv4", "0.0.0.0"])
    assert result.exit_code == 0
    print(result.stdout)
    assert "0.0.0.0" in result.stdout

def test_invalid_ipv4_1():
    result = runner.invoke(app, ["tests/test_files/ipv4.log", "--ipv4", "30.168.1.255.1"])
    assert result.exit_code == 2
    print(result.stdout)
    assert "Error: Invalid value" in result.stdout

def test_invalid_ipv4_2():
    result = runner.invoke(app, ["tests/test_files/ipv4.log", "--ipv4", "127.1"])
    assert result.exit_code == 2
    print(result.stdout)
    assert "Error: Invalid value" in result.stdout

def test_invalid_ipv4_3():
    result = runner.invoke(app, ["tests/test_files/ipv4.log", "--ipv4", "192.168.1.256"])
    assert result.exit_code == 2
    print(result.stdout)
    assert "Error: Invalid value" in result.stdout

def test_invalid_ipv4_4():
    result = runner.invoke(app, ["tests/test_files/ipv4.log", "--ipv4", "-1.2.3.4"])
    assert result.exit_code == 2
    print(result.stdout)
    assert "Error: Invalid value" in result.stdout

def test_invalid_ipv4_5():
    result = runner.invoke(app, ["tests/test_files/ipv4.log", "--ipv4", "-1.1.1.1."])
    assert result.exit_code == 2
    print(result.stdout)
    assert "Error: Invalid value" in result.stdout

def test_invalid_ipv4_6():
    result = runner.invoke(app, ["tests/test_files/ipv4.log", "--ipv4", "3...3"])
    assert result.exit_code == 2
    print(result.stdout)
    assert "Error: Invalid value" in result.stdout

def test_supersition_ipv4_1():
    result = runner.invoke(app, ["tests/test_files/ipv4.log", "--ipv4", "192.168.1.1"])
    assert result.exit_code == 0
    print(result.stdout)
    assert "L7" not in result.stdout

def test_supersition_ipv4_1():
    result = runner.invoke(app, ["tests/test_files/ipv4.log", "--ipv4", "92.168.1.1"])
    assert result.exit_code == 0
    print(result.stdout)
    assert "L2" not in result.stdout