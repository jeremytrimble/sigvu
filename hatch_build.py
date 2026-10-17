"""Hatchling build hook that generates src/sigvu/version_info.json."""

import sys
from pathlib import Path

from hatchling.builders.hooks.plugin.interface import BuildHookInterface

ROOT = Path(__file__).parent


class VersionInfoHook(BuildHookInterface):
    PLUGIN_NAME = "custom"

    def initialize(self, version, build_data):
        # An sdist has no .git; keep the file generated when the sdist was built.
        target = ROOT / "src" / "sigvu" / "version_info.json"
        if not (ROOT / ".git").exists() and target.exists():
            return

        sys.path.insert(0, str(ROOT / "build_hooks"))
        try:
            from generate_version_info import generate_version_info
        finally:
            sys.path.pop(0)
        generate_version_info(target.parent)
