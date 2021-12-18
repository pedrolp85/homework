from typer.testing import CliRunner
from util import app

runner = CliRunner()


def test_stdin(capsys, monkeypatch):

    result = runner.invoke(app, ["--ipv4", "172.16.0.14"], input="172.16.0.14\n")
    assert result.exit_code == 0
    print(result.stdout)
    assert "172.16.0.14" in result.stdout


# def test_one(capsys, monkeypatch):
#
#     app.ask_one()
#     out, err = capsys.readouterr()
#     assert err == ''
#     #print(out)
#     assert out == 'Please enter your name: Your name is Foo\n'

# def test_two(monkeypatch, capsys):
#     monkeypatch.setattr(sys, 'stdin', io.StringIO('3\n4'))
#     app.ask_two()
#     out, err = capsys.readouterr()
#     assert err == ''
#     #print(out)
#     assert out == 'Please enter width: Please enter length: 3.0*4.0 is 12.0\n
