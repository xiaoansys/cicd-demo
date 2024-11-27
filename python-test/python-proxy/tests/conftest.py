"""Unit tests fixtures."""

from pathlib import Path
from subprocess import run
import sys
from inspect import getsourcefile
import os


def get_resources_dir() -> Path:
    """Return the directory ./resources relative to this file's directory."""
    script_path = Path(os.path.abspath(getsourcefile(lambda: 0)))
    return script_path.parent

def build_proxy(module: str) -> bool:

    target_dir = get_resources_dir() / ".." / ".." / ".." / "Model" / "Calculator" / "Python_DLL_Build"
    dll = target_dir / ('%s.dll' % module)
    
    # add the directory to sys.path
    if str(target_dir) not in sys.path:
        sys.path.append(str(target_dir))
    return dll.exists()
