from typer.testing import CliRunner
from util import app

runner = CliRunner()


def test_first_option():
    result = runner.invoke(app, ["tests/test_files/secure.log", "--first", 10])
    print(result.stdout)
    assert result.exit_code == 0


def test_first_option_error():
    result = runner.invoke(app, ["tests/test_files/secure.log", "--first", "aaa"])
    assert result.exit_code == 2
    print(result.stdout)
    assert result.exception
    assert "Error: Invalid value" in result.stdout


def test_first_option_short():
    result = runner.invoke(app, ["tests/test_files/secure.log", "-f", 10])
    assert result.exit_code == 0
    print(result.stdout)


def test_first_option_short_error():
    result = runner.invoke(app, ["tests/test_files/secure.log", "-f", "bbb"])
    assert result.exit_code == 2
    print(result.stdout)
    assert "Error: Invalid value" in result.stdout


def test_last_option():
    result = runner.invoke(app, ["tests/test_files/secure.log", "--last", 10])
    assert result.exit_code == 0
    print(result.stdout)


def test_last_option_error():
    result = runner.invoke(app, ["tests/test_files/secure.log", "--last", "aaa"])
    assert result.exit_code == 2
    print(result.stdout)
    assert "Error: Invalid value" in result.stdout


def test_last_option_short():
    result = runner.invoke(app, ["tests/test_files/secure.log", "-l", 10])
    assert result.exit_code == 0
    print(result.stdout)


def test_last_option_short_error():
    result = runner.invoke(app, ["tests/test_files/secure.log", "-l", "bbbb"])
    assert result.exit_code == 2
    print(result.stdout)
    assert "Error: Invalid value" in result.stdout


def test_ipv4_option():
    result = runner.invoke(
        app, ["tests/test_files/secure.log", "--ipv4", "172.16.0.102"]
    )
    assert result.exit_code == 0
    print(result.stdout)


def test_ipv4_option_error():
    result = runner.invoke(
        app, ["tests/test_files/secure.log", "--ipv4", "172.16.0.256"]
    )
    assert result.exit_code == 2
    assert "Error: Invalid value" in result.stdout
    print(result.stdout)


def test_ipv4_option_short():
    result = runner.invoke(app, ["tests/test_files/secure.log", "-i", "172.16.0.102"])
    assert result.exit_code == 0
    print(result.stdout)


def test_ipv4_option_short_error():
    result = runner.invoke(
        app, ["tests/test_files/secure.log", "--ipv4", "172.16.0.256"]
    )
    assert result.exit_code == 2
    assert "Error: Invalid value" in result.stdout
    print(result.stdout)


def test_ipv6_option():
    result = runner.invoke(
        app, ["tests/test_files/secure.log", "--ipv6", "2001:DB8::1"]
    )
    assert result.exit_code == 0
    print(result.stdout)


def test_ipv6_option_error():
    result = runner.invoke(
        app, ["tests/test_files/secure.log", "--ipv6", "200H:DB8::1"]
    )
    assert result.exit_code == 2
    assert "Error: Invalid value" in result.stdout
    print(result.stdout)


def test_ipv6_option_short():
    result = runner.invoke(app, ["tests/test_files/secure.log", "-I", "2001:DB8::1"])
    assert result.exit_code == 0
    print(result.stdout)


def test_ipv6_option_short_error():
    result = runner.invoke(app, ["tests/test_files/secure.log", "-I", "200H:DB8::1"])
    assert result.exit_code == 2
    assert "Error: Invalid value" in result.stdout
    print(result.stdout)


def test_call_no_options():
    result = runner.invoke(app, ["tests/test_files/secure.log"])
    assert result.exit_code == 0
    print(result.stdout)
