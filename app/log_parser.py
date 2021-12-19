import ipaddress
import os
import re
import sys
from abc import ABCMeta, abstractmethod
from datetime import datetime
from typing import Any, List, Optional


class LogParser(metaclass=ABCMeta):
    @abstractmethod
    def get_lines(self, file_name: Optional[str]) -> List[str]:
        pass

    @abstractmethod
    def get_head(self, lines: List[str], num_lines: int) -> List[str]:
        pass

    @abstractmethod
    def get_tail(self, lines: List[str], num_lines: int) -> List[str]:
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

    @abstractmethod
    def get_ipv6_enhanced(
        self, lines: List[str], ipv6: ipaddress.IPv6Address
    ) -> List[str]:
        pass

    @abstractmethod
    def get_result(
        self,
        lines: List[str],
        head_num_lines: Any,
        tail_num_lines: Any,
        timestamp: Any,
        ipv4: Any,
        ipv6: Any,
    ) -> List[str]:
        pass


class LogParserMock(LogParser):
    def get_lines(self, file_name: Optional[str]) -> List[str]:
        return [
            "First Line",
            "Second Line",
            "13:13:13 Log file timestamp",
            "172.16.0.14 ipv4 log file entry",
            "2001:DB8::1 ipv6 log file entry",
            "::8 iv6 too compressed file entry",
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

    def get_ipv6_enhanced(
        self, lines: List[str], ipv6: ipaddress.IPv6Address
    ) -> List[str]:
        return ["::8 iv6 too compressed file entry"]

    def get_result(
        self,
        lines: List[str],
        head_num_lines: Any,
        tail_num_lines: Any,
        timestamp: Any,
        ipv4: Any,
        ipv6: Any,
    ) -> List[str]:
        return ["First Line"]


class LogParserUtils(LogParser):
    def get_head(self, lines: List[str], num_lines: int) -> List[str]:
        # print(f"lets make a head oper with {num_lines} lines")
        max_lines = num_lines if (num_lines < (len(lines))) else (len(lines))
        lines_filtered = lines[0:max_lines]
        return lines_filtered

    def get_tail(self, lines: List[str], num_lines: int) -> List[str]:
        # print(f"lets make a tail oper with {num_lines} lines")
        max_lines = num_lines if (num_lines < (len(lines))) else (len(lines))
        lines_filtered = lines[-(max_lines):]
        return lines_filtered

    def get_timestamp(self, lines: List[str], timestamp: datetime) -> List[str]:
        # print(
        # f"lets grep {timestamp.hour}:{timestamp.minute}:{timestamp.second} "
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

    def get_ipv6_enhanced(
        self, lines: List[str], ipv6: ipaddress.IPv6Address
    ) -> List[str]:
        lines_filtered = []
        for line in lines:
            words = line.split()
            for word in words:
                try:
                    ip_address = ipaddress.IPv6Address(word)
                    if ip_address == ipv6:
                        lines_filtered.append(line)
                        break
                except ValueError:
                    continue
        return lines_filtered

    def _intersect_results(
        self, lines: List[str], more_lines: Optional[List[str]]
    ) -> List[str]:
        try:
            return list(set(lines).intersection(set(more_lines)))
        except NameError:
            return lines

    def get_result(
        self,
        lines: List[str],
        head_num_lines: Any,
        tail_num_lines: Any,
        timestamp: Any,
        ipv4: Any,
        ipv6: Any,
    ) -> List[str]:

        no_options = (
            True
            if (
                not head_num_lines
                and not tail_num_lines
                and not timestamp
                and not ipv4
                and not ipv6
            )
            else False
        )

        if no_options:
            common_lines = lines
        if head_num_lines:
            head_lines = self.get_head(lines, head_num_lines)
            common_lines = head_lines
        if tail_num_lines:
            tail_lines = self.get_tail(lines, tail_num_lines)
            if "common_lines" in vars():
                common_lines = self._intersect_results(tail_lines, common_lines)
            else:
                common_lines = tail_lines
        if timestamp:
            timestamp_lines = self.get_timestamp(lines, timestamp)
            if "common_lines" in vars():
                common_lines = self._intersect_results(timestamp_lines, common_lines)
            else:
                common_lines = timestamp_lines
        if ipv4:
            ipv4_lines = self.get_ipv4(lines, ipv4)
            if "common_lines" in vars():
                common_lines = self._intersect_results(ipv4_lines, common_lines)
            else:
                common_lines = ipv4_lines
        if ipv6:
            ipv6_lines = self.get_ipv6_enhanced(lines, ipv6)
            if "common_lines" in vars():
                common_lines = self._intersect_results(ipv6_lines, common_lines)
            else:
                common_lines = ipv6_lines

        return common_lines


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
