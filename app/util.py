#! /usr/local/bin/python3.7
import ipaddress
import os
from datetime import datetime
from typing import Optional

import typer
from logparser.logparsercli import get_log_parser
from output.printoutput import get_print_output

app = typer.Typer()


def validate_file(file: str) -> str:

    if not os.path.isabs(file):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, file)
    else:
        filename = file
    if os.path.isfile(filename):
        return filename
    else:
        typer.echo("The File provided does not exist")
        raise typer.Exit(code=2)


def validate_ipv6address(ip: str) -> ipaddress.IPv6Address:
    if ip is not None:
        try:
            ip_address = ipaddress.IPv6Address(ip)
        except ValueError:
            raise typer.BadParameter("Only valid IPv6 addresess")

        return ip_address


def validate_ipv4address(ip: str) -> ipaddress.IPv4Address:
    if ip is not None:     
        if not ip.isnumeric():
            try:
                ip_address = ipaddress.IPv4Address(ip)
            except ValueError:
                raise typer.BadParameter("Only valid IPv4 addresess accepted")
        else:
            try:
                ip_address = ipaddress.IPv4Address(int(ip))
            except ValueError:
                raise typer.BadParameter("Only valid IPv4 addresess accepted")                
        
        return ip_address


def validate_datetime(timestamp: str) -> datetime:
    if timestamp is not None:
        try:
            time_object = datetime.strptime(timestamp, "%H:%M:%S")
            timestr = time_object.strftime("%H:%M:%S")
        except ValueError:
            raise typer.BadParameter("Timestamp provided is not valid")
        if timestr == timestamp:
            return time_object
        else:
            raise typer.BadParameter("Timestamp provided is not zero padded ")


@app.command()
def log_parser(
    first: int = typer.Option(None, "--first", "-f", help="Print first NUM lines"),
    last: int = typer.Option(None, "--last", "-l", help="Print last NUM lines "),
    timestamps: str = typer.Option(
        None,
        "--timestamps",
        "-t",
        callback=validate_datetime,
        help="Print lines that contain a timestamp in HH:MM:SS format",
    ),
    ipv4: str = typer.Option(
        None,
        "--ipv4",
        "-i",
        callback=validate_ipv4address,
        help="Print lines that contain an IPv4 address, matching IPs are highlighted",
    ),
    ipv6: str = typer.Option(
        None,
        "--ipv6",
        "-I",
        callback=validate_ipv6address,
        help="Print lines that contain an IPv6 address, matching IPs are highlighted",
    ),
    file: Optional[str] = typer.Argument(None),
) -> None:

    if file:

        log_parser = get_log_parser("file")
        filename = validate_file(file)
        lines = log_parser.get_lines(filename)
        if not lines:
            typer.echo("Permission denied to operate the file")
            raise typer.Exit(code=2)
    else:

        log_parser = get_log_parser("stdin")
        lines = log_parser.get_lines(file)

    common_elements = log_parser.get_result(lines, first, last, timestamps, ipv4, ipv6)
    printer = get_print_output()

    for element in common_elements:
        printer.print_output_to_stdout(element, ipv4, ipv6)


if __name__ == "__main__":
    app()
