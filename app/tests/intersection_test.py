from typer.testing import CliRunner
from util import app

runner = CliRunner()


def test_intersection_1():
    result = runner.invoke(
        app, ["tests/test_files/intersection.log", "--first", 11, "--last", 11]
    )
    assert result.exit_code == 0
    assert "L" not in result.stdout
    print(result.stdout)


def test_intersection_2():
    result = runner.invoke(
        app, ["tests/test_files/intersection.log", "--first", 11, "--last", 12]
    )
    assert result.exit_code == 0
    assert "L11" in result.stdout
    print(result.stdout)


def test_intersection_3():
    result = runner.invoke(
        app, ["tests/test_files/intersection.log", "--first", 5, "--ipv4", "172.16.0.1"]
    )
    assert result.exit_code == 0
    assert "L1" in result.stdout
    assert "L3" not in result.stdout
    print(result.stdout)


def test_intersection_4():
    result = runner.invoke(
        app,
        [
            "tests/test_files/intersection.log",
            "--first",
            5,
            "--ipv6",
            "2001:db8:0:0:0::1",
        ],
    )
    assert result.exit_code == 0
    assert "L2" in result.stdout
    assert "L4" in result.stdout
    assert "L1" not in result.stdout
    assert "L5" not in result.stdout
    print(result.stdout)


def test_intersection_5():
    result = runner.invoke(
        app,
        [
            "tests/test_files/intersection.log",
            "--first",
            20,
            "--timestamps",
            "11:11:11",
        ],
    )
    assert result.exit_code == 0
    assert "L12" in result.stdout
    assert "L17" in result.stdout
    assert "L21" not in result.stdout
    print(result.stdout)


def test_intersection_6():
    result = runner.invoke(
        app, ["tests/test_files/intersection.log", "--last", 8, "--ipv4", "192.168.1.1"]
    )
    assert result.exit_code == 0
    assert "L20" in result.stdout
    assert "L19" in result.stdout
    assert "14" not in result.stdout
    print(result.stdout)


def test_intersection_7():
    result = runner.invoke(
        app,
        ["tests/test_files/intersection.log", "--last", 8, "--ipv6", "1:2:3:4:5::8"],
    )
    assert result.exit_code == 0
    assert "L20" in result.stdout
    assert "L22" in result.stdout
    assert "21" not in result.stdout
    print(result.stdout)


def test_intersection_8():
    result = runner.invoke(
        app,
        ["tests/test_files/intersection.log", "--last", 8, "--timestamps", "12:03:59"],
    )
    assert result.exit_code == 0
    assert "L18" in result.stdout
    assert "L20" in result.stdout
    assert "13" not in result.stdout
    print(result.stdout)


def test_intersection_9():
    result = runner.invoke(
        app,
        [
            "tests/test_files/intersection.log",
            "--ipv4",
            "192.168.1.1",
            "--ipv6",
            "2001:db8:0:0:0::1",
        ],
    )
    assert result.exit_code == 0
    assert "L8" in result.stdout
    assert "L19" in result.stdout
    assert "18" in result.stdout
    assert "L3" not in result.stdout
    print(result.stdout)


def test_intersection_10():
    result = runner.invoke(
        app,
        [
            "tests/test_files/intersection.log",
            "--ipv6",
            "2001:db8:0:0:0::1",
            "--timestamps",
            "11:11:11",
        ],
    )
    assert result.exit_code == 0
    assert "L21" in result.stdout
    assert "L17" in result.stdout
    assert "L12" not in result.stdout
    print(result.stdout)


def test_intersection_11():
    result = runner.invoke(
        app,
        [
            "tests/test_files/intersection.log",
            "--first",
            15,
            "--last",
            15,
            "--ipv4",
            "172.16.0.1",
        ],
    )
    assert result.exit_code == 0
    assert "L12" in result.stdout
    assert "L1 " not in result.stdout
    assert "L3" not in result.stdout
    print(result.stdout)


def test_intersection_12():
    result = runner.invoke(
        app,
        [
            "tests/test_files/intersection.log",
            "--last",
            14,
            "--ipv4",
            "192.168.1.1",
            "--ipv6",
            "2001:db8:0::1",
        ],
    )
    assert result.exit_code == 0
    assert "L18" in result.stdout
    assert "L14" not in result.stdout
    assert "L19" in result.stdout
    print(result.stdout)


def test_intersection_13():
    result = runner.invoke(
        app,
        [
            "tests/test_files/intersection.log",
            "--ipv4",
            "192.168.1.1",
            "--ipv6",
            "2001:db8:0::1",
            "--timestamps",
            "12:03:59",
        ],
    )
    assert result.exit_code == 0
    assert "L18" in result.stdout
    assert "L13" not in result.stdout
    print(result.stdout)


def test_intersection_14():
    result = runner.invoke(
        app,
        [
            "tests/test_files/intersection.log",
            "--first",
            20,
            "--last",
            "20",
            "--ipv4",
            "192.168.1.10",
            "--ipv6",
            "2001:db8:0::1",
        ],
    )
    assert result.exit_code == 0
    assert "L3" in result.stdout
    print(result.stdout)


def test_intersection_15():
    result = runner.invoke(
        app,
        [
            "tests/test_files/intersection.log",
            "--last",
            5,
            "--ipv4",
            "192.168.1.1",
            "--ipv6",
            "2001:db8:0::1",
            "--timestamps",
            "12:03:59",
        ],
    )
    assert result.exit_code == 0
    assert "L18" in result.stdout
    print(result.stdout)
