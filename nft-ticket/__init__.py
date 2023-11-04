from importlib.util import find_spec

if find_spec("taipy"):
    if find_spec("taipy.config"):
        from taipy.config._init import *  # type: ignore

    if find_spec("taipy.gui"):
        from taipy.gui._init import *  # type: ignore
        
    if find_spec("taipy.core"):
        from taipy.core._init import *  # type: ignore

    if find_spec("taipy.rest"):
        from taipy.rest._init import *  # type: ignore

    if find_spec("taipy.gui_core"):
        from taipy.gui_core._init import *  # type: ignore

    if find_spec("taipy.enterprise"):
        from taipy.enterprise._init import *  # type: ignore

    if find_spec("taipy._run"):
        from taipy._run import _run as run  # type: ignore
