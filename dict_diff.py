from typing import List, Tuple, Any, Dict
from dataclasses import dataclass
import json

@dataclass
class Diffline():
    path: List[str]
    addition: bool
    content: Any

    def __repr__(self) -> str:
        return "{modifier} {path}: {value}".format(
            modifier="+" if self.addition else "-",
            path=".".join(self.path),
            value=self.content,
        )

################################################################################
# dict_diff
#
# Recursively finds the differences between two dictionaries.
# Returns a dictionary with keys that are different.
################################################################################
def dict_diff(d1: Dict, d2: Dict) -> List[Diffline]:
    diff: List[Diffline] = []
    for key, value in d1.items():
        if key not in d2:
            diff.append(Diffline(path=[key.__repr__()], addition=False, content=value))
        elif isinstance(value, dict) and isinstance(d2[key], dict):
            nested_diff = dict_diff(value, d2[key])
            for nested_diff_line in nested_diff:
                nested_diff_line.path.insert(0, key.__repr__())
                diff.append(nested_diff_line)
        elif value != d2[key]:
            diff.append(Diffline(path=[key.__repr__()], addition=False, content=value))
            diff.append(Diffline(path=[key.__repr__()], addition=True, content=d2[key]))


    for key, value in d2.items():
        if key not in d1:
            diff.append(Diffline(path=[key.__repr__()], addition=True, content=value))

    return sorted(diff, key=lambda x: ".".join(x.path) + str(x.addition))

