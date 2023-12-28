# This file is part of Xpra.
# Copyright (C) 2014, 2015 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

# posix: assume cups support (no overrides needed here)
from xpra.platform.pycups_printing import (
    get_printers,
    print_files,
    printing_finished,
    init_printing,
    cleanup_printing,
    get_info,
)

assert get_printers and print_files and printing_finished and init_printing and cleanup_printing and get_info   # noqa: E501 type: ignore[truthy-function]
