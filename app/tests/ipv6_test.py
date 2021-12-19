from typer.testing import CliRunner
from util import app

runner = CliRunner()


def test_valid_ipv6_1():
    result = runner.invoke(
        app, ["tests/test_files/ipv6.log", "--ipv6", "1:2:3:4:5:6:7:8"]
    )
    assert result.exit_code == 0
    print(result.stdout)
    assert "1:2:3:4:5:6:7:8" in result.stdout


def test_valid_ipv6_2():
    result = runner.invoke(app, ["tests/test_files/ipv6.log", "--ipv6", "1::8"])
    assert result.exit_code == 0
    print(result.stdout)
    assert "1::8" in result.stdout


def test_valid_ipv6_3():
    result = runner.invoke(app, ["tests/test_files/ipv6.log", "--ipv6", "1::7:8"])
    assert result.exit_code == 0
    print(result.stdout)
    assert "1::7:8" in result.stdout


def test_valid_ipv6_4():
    result = runner.invoke(app, ["tests/test_files/ipv6.log", "--ipv6", "1::6:7:8"])
    assert result.exit_code == 0
    print(result.stdout)
    assert "1::6:7:8" in result.stdout


def test_valid_ipv6_5():
    result = runner.invoke(app, ["tests/test_files/ipv6.log", "--ipv6", "1::5:6:7:8"])
    assert result.exit_code == 0
    print(result.stdout)
    assert "1::5:6:7:8" in result.stdout


def test_valid_ipv6_6():
    result = runner.invoke(app, ["tests/test_files/ipv6.log", "--ipv6", "1::4:5:6:7:8"])
    assert result.exit_code == 0
    print(result.stdout)
    assert "1::4:5:6:7:8" in result.stdout


def test_valid_ipv6_7():
    result = runner.invoke(app, ["tests/test_files/ipv6.log", "--ipv6", "1::"])
    assert result.exit_code == 0
    print(result.stdout)
    assert "1::" in result.stdout


def test_valid_ipv6_9():
    result = runner.invoke(app, ["tests/test_files/ipv6.log", "--ipv6", "1:2:3:4::8"])
    assert result.exit_code == 0
    print(result.stdout)
    assert "1:2:3:4::8" in result.stdout


def test_valid_ipv6_10():
    result = runner.invoke(app, ["tests/test_files/ipv6.log", "--ipv6", "1:2:3::8"])
    assert result.exit_code == 0
    print(result.stdout)
    assert "1:2:3::8" in result.stdout


def test_valid_ipv6_11():
    result = runner.invoke(app, ["tests/test_files/ipv6.log", "--ipv6", "1:2::8"])
    assert result.exit_code == 0
    print(result.stdout)
    assert "1:2::8" in result.stdout


def test_valid_ipv6_12():
    result = runner.invoke(app, ["tests/test_files/ipv6.log", "--ipv6", "::8"])
    assert result.exit_code == 0
    print(result.stdout)
    assert "::8" in result.stdout


def test_valid_ipv6_13():
    result = runner.invoke(app, ["tests/test_files/ipv6.log", "--ipv6", "::"])
    assert result.exit_code == 0
    print(result.stdout)
    assert "::" in result.stdout


def test_valid_ipv6_14():
    result = runner.invoke(
        app, ["tests/test_files/ipv6.log", "--ipv6", "1::3:4:5:6:7:8"]
    )
    assert result.exit_code == 0
    print(result.stdout)
    assert "1::3:4:5:6:7:8" in result.stdout


def test_valid_ipv6_15():
    result = runner.invoke(
        app, ["tests/test_files/ipv6.log", "--ipv6", "1:2:3:4:5:6:7::"]
    )
    assert result.exit_code == 0
    print(result.stdout)
    assert "1:2:3:4:5:6:7::" in result.stdout


def test_valid_ipv6_16():
    result = runner.invoke(app, ["tests/test_files/ipv6.log", "--ipv6", "1:2:3:4:5::8"])
    assert result.exit_code == 0
    print(result.stdout)
    assert "1:2:3:4:5::8" in result.stdout


def test_invalid_ipv6_1():
    result = runner.invoke(app, ["tests/test_files/ipv6.log", "--ipv6", "225.1.4.2"])
    assert result.exit_code == 2
    print(result.stdout)
    assert "Error: Invalid value" in result.stdout


def test_invalid_ipv6_2():
    result = runner.invoke(
        app, ["tests/test_files/ipv6.log", "--ipv6", "fe80:2030:31:24"]
    )
    assert result.exit_code == 2
    print(result.stdout)
    assert "Error: Invalid value" in result.stdout


def test_several_representations_ipv6_1():
    result = runner.invoke(
        app, ["tests/test_files/ipv6.log", "--ipv6", "2001:db8:0:0:0::1"]
    )
    assert result.exit_code == 0
    print(result.stdout)
    assert "2001:db8:0:0:0::1" in result.stdout
    assert "2001:db8:0:0::1" in result.stdout
    assert "2001:db8:0::1" in result.stdout
    assert "2001:db8::1" in result.stdout


def test_valid_ipv6_duplicated_in_line():
    result = runner.invoke(app, ["tests/test_files/ipv6.log", "--ipv6", "1:2:3:4:5::8"])
    assert result.exit_code == 0
    print(result.stdout)
    assert "1:2:3:4:5::8" in result.stdout
