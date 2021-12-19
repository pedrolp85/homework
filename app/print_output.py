import ipaddress
import re
from abc import ABCMeta, abstractmethod
from typing import Any, Optional

from constants import HIGHLIGHT_OPTIONS


class PrintOutput(metaclass=ABCMeta):
    @abstractmethod
    def print_line(self, line: str) -> None:
        pass


class PrintOutputStdout(PrintOutput):
    def print_line(self, line: str) -> None:
        print(f"{line}")

    def _regex_ip_replace(self, line: str, regexp: str, sub_regexp: str) -> str:
        return re.sub(regexp, sub_regexp, line, flags=re.I)

    def _replace_ipv4_ansi_highlight(
        self,
        line: str,
        ipv4: ipaddress.IPv4Address,
        highlight: Optional[str] = HIGHLIGHT_OPTIONS["ON_GREEN"],
    ) -> str:
        sub_regexp = highlight + str(ipv4) + HIGHLIGHT_OPTIONS["END_COLOR"]
        return self._regex_ip_replace(line, str(ipv4), sub_regexp)

    def _replace_ipv6_ansi_highlight(
        self,
        line,
        ipv6: ipaddress.IPv6Address,
        highlight: Optional[str] = HIGHLIGHT_OPTIONS["ON_RED"],
    ) -> str:
        sub_regexp = highlight + str(ipv6) + HIGHLIGHT_OPTIONS["END_COLOR"]
        return self._regex_ip_replace(line, str(ipv6), sub_regexp)

    def print_output_to_stdout(self, line, ipv4: Any, ipv6: Any) -> None:
        if ipv4:
            line = self._replace_ipv4_ansi_highlight(line, ipv4)
        if ipv6:
            words = line.split()
            for word in words:
                try:
                    ip_address = ipaddress.IPv6Address(word)
                    if ip_address == ipv6:
                        line = self._replace_ipv6_ansi_highlight(line, word)
                except ValueError:
                    continue

        self.print_line(line)


def get_print_output() -> PrintOutput:
    return PrintOutputStdout()
