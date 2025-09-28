from tests.bad_import import bad_function, BadClass

import tests.bad_import2

import tests.bad_import3 as bi

bad_function()
something = BadClass()
something.bad_method()


tests.bad_import2.bad_function()
bi.bad_function()
