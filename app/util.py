#! /usr/local/bin/python3.7
import ipaddress
from datetime import datetime
from typing import Optional

import typer
from log_parser import get_log_parser
from print_output import get_print_output

app = typer.Typer()


def validate_ipv6address(ip: str):
    if ip is not None:
        try:
            ip_address = ipaddress.IPv6Address(ip)
        except ValueError:
            raise typer.BadParameter(
                "Only valid IPv6 address with -I, --ipv6 parameter"
            )

        return ip_address


def validate_ipv4address(ip: str):
    if ip is not None:
        try:
            ip_address = ipaddress.IPv4Address(ip)
        except ValueError:
            raise typer.BadParameter(
                "Only valid IPv4 address with -i, --ipv4 parameter"
            )

        return ip_address


@app.command()
def log_parser(
    first: int = typer.Option(None, "--first", "-f", help="Print first NUM lines"),
    last: int = typer.Option(None, "--last", "-l", help="Print last NUM lines "),
    timestamps: datetime = typer.Option(
        None,
        "--timestamps",
        "-t",
        formats=["%H:%M:%S"],
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
        lines = log_parser.get_lines(file)

    else:

        log_parser = get_log_parser("stdin")
        lines = log_parser.get_lines(file)

    common_elements = log_parser.get_result(lines, first, last, timestamps, ipv4, ipv6)
    printer = get_print_output()

    for element in common_elements:
        printer.print_output_to_stdout(element, ipv4, ipv6)


if __name__ == "__main__":
    app()
