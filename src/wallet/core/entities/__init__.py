from functools import partial

import attr


dataclass = partial(attr.s, auto_attribs=True, kw_only=True, slots=True)
