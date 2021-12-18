import ipaddress
import os
import re
import sys
from abc import ABCMeta, abstractmethod
from datetime import datetime
from typing import List, Optional


class LogParser(metaclass=ABCMeta):
    @abstractmethod
    def get_lines(self, file_name: Optional[str]) -> List[str]:
        pass

    @abstractmethod
    def get_head(self, lines: List[str], num_lines: Optional[int]) -> List[str]:
        pass

    @abstractmethod
    def get_tail(self, lines: List[str], num_lines: Optional[int]) -> List[str]:
        pass

    @abstractmethod
    def get_timestamp(self, lines: List[str], timestamp: datetime) -> List[str]:
        pass

    @abstractmethod
    def get_ipv4(self, lines: List[str], ipv4: ipaddress.IPv4Address) -> List[str]:
        pass

    @abstractmethod
    def get_ipv6(self, lines: List[str], ipv6: ipaddress.IPv6Address) -> List[str]:
        pass


class LogParserMock(LogParser):
    def get_lines(self, file_name: Optional[str]) -> List[str]:
        return [
            "First Line",
            "Second Line",
            "13:13:13 Log file timestamp",
            "172.16.0.14 ipv4 log file entry",
            "2001:DB8::1 ipv6 log file entry",
        ]

    def get_head(self, lines: List[str], num_lines: Optional[int]) -> List[str]:
        return ["First Line"]

    def get_tail(self, lines: List[str], num_lines: Optional[int]) -> List[str]:
        return ["Second Line"]

    def get_timestamp(self, lines: List[str], timestamp: datetime) -> List[str]:
        return ["13:13:13 Log file timestamp"]

    def get_ipv4(self, lines: List[str], ipv4: ipaddress.IPv4Address) -> List[str]:
        return ["172.16.0.14 ipv4 log file entry"]

    def get_ipv6(self, lines: List[str], ipv6: ipaddress.IPv6Address) -> List[str]:
        return ["2001:DB8::1 ipv6 log file entry"]


class LogParserUtils(LogParser):
    def get_head(self, lines: List[str], num_lines: Optional[int]) -> List[str]:
        # print(f"lets make a head oper with {num_lines} lines")
        max_lines = num_lines if (num_lines < (len(lines))) else (len(lines))
        lines_filtered = lines[0:max_lines]
        return lines_filtered

    def get_tail(self, lines: List[str], num_lines: Optional[int]) -> List[str]:
        # print(f"lets make a tail oper with {num_lines} lines")
        max_lines = num_lines if (num_lines < (len(lines))) else (len(lines))
        lines_filtered = lines[-(max_lines):]
        return lines_filtered

    def get_timestamp(self, lines: List[str], timestamp: datetime) -> List[str]:
        # print(
        # f"lets grep with {timestamp.hour}:{timestamp.minute}:{timestamp.second} "
        # )
        regexp = timestamp.strftime("%H:%M:%S")
        lines_filtered = [line for line in lines if re.search(regexp, line)]
        return lines_filtered

    def get_ipv4(self, lines: List[str], ipv4: ipaddress.IPv4Address) -> List[str]:
        # print(f"lets grep with {ipv4} regex")
        regexp = str(ipv4)
        lines_filtered = [line for line in lines if re.search(regexp, line)]
        return lines_filtered

    def get_ipv6(self, lines: List[str], ipv6: ipaddress.IPv6Address) -> List[str]:
        # print(f"lets grep with {ipv6} regex")
        regexp = str(ipv6)

        lines_filtered = [
            line for line in lines if re.search(regexp, line, re.IGNORECASE)
        ]
        return lines_filtered


class LogParserFromFile(LogParserUtils):
    def get_lines(self, file_name: Optional[str]) -> List[str]:

        # print(f"taking lines from file Argument {file_name}")
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, file_name)
        f = open(filename, "r")
        lines = [line.strip() for line in f]
        f.close()

        return lines


class LogParserFromStdin(LogParserUtils):
    def get_lines(self, file_name: Optional[str]) -> List[str]:
        # print(f'{"taking lines from stdin"}')
        lines = []
        for line in sys.stdin:
            lines.append(line.rstrip())
        return lines


def get_log_parser(type: str) -> LogParser:

    DEPENDENCY_RESOLVE_DICT = {
        "file": LogParserFromFile(),
        "stdin": LogParserFromStdin(),
        "mock": LogParserMock(),
    }

    return DEPENDENCY_RESOLVE_DICT[type]
