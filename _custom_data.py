# ----------------------------------------------------------------------
# |
# |  _custom_data.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2019-04-25 11:05:38
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2019
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Data used by both Setup_custom.py and Activate_custom.py"""

import os

from collections import OrderedDict

import CommonEnvironment
from CommonEnvironment.Shell.All import CurrentShell

# ----------------------------------------------------------------------
_script_fullpath                            = CommonEnvironment.ThisFullpath()
_script_dir, _script_name                   = os.path.split(_script_fullpath)
#  ----------------------------------------------------------------------

_CUSTOM_DATA                                = []

if CurrentShell.CategoryName == "Windows":
    _CUSTOM_DATA.append(
        (
            "Clang - 8.0.0",
            "5d340fea17c50f6243f96f72ac3df64d38c437fad31a40ca21507c4fae4a2c0b",
            "Install.7z",
            [
                "Tools",
                "Clang",
                "v8.0.0",
                "Windows",
            ],
        ),
    )
elif CurrentShell.Name == "Ubuntu":
    import distro

    version                                 = distro.version()

    hash_map                                = {
        "18.04": "0f5c314f375ebd5c35b8c1d5e5b161d9efaeff0523bac287f8b4e5b751272f51",
        "16.04": "87b88d620284d1f0573923e6f7cc89edccf11d19ebaec1cfb83b4f09ac5db09c",
    }

    if version not in hash_map:
        raise Exception("'{}' is not a recognized Ubuntu version".format(version))

    _CUSTOM_DATA.append(
        (
            "Clang - 8.0.0",
            hash_map[version],
            "http://releases.llvm.org/8.0.0/clang+llvm-8.0.0-x86_64-linux-gnu-ubuntu-{}.tar.xz".format(
                version,
            ),
            [
                "Tools",
                "Clang",
                "v8.0.0",
                "Ubuntu",
            ],
        ),
    )
else:
    raise Exception("Clang has not been configured for this operating system")
