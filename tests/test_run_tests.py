# -*- coding: utf-8 -*-

# Licensed under a 3-clause BSD style license - see LICENSE.rst

# TEST_UNICODE_LITERALS

from __future__ import (absolute_import, division, print_function,
                         unicode_literals)

import doctest

from textwrap import dedent

# test helper.run_tests function

from ... extern import six

from .. import helper
from ... import _get_test_runner
from .. helper import pytest

# run_tests should raise ValueError when asked to run on a module it can't find
def test_module_not_found():
    with helper.pytest.raises(ValueError):
        _get_test_runner().run_tests('fake.module')


# run_tests should raise ValueError when passed an invalid pastebin= option
def test_pastebin_keyword():
    with helper.pytest.raises(ValueError):
        _get_test_runner().run_tests(pastebin='not_an_option')


# tests that tests are only run in Python 3 out of the 2to3'd build (otherwise
# a syntax error would occur)
try:
    from .run_after_2to3 import test_run_after_2to3
except SyntaxError:
    def test_run_after_2to3():
        helper.pytest.fail("Not running the 2to3'd tests!")


# TODO: Temporarily disabled, as this seems to non-deterministically fail
# def test_deprecation_warning():
#     with pytest.raises(DeprecationWarning):
#         warnings.warn('test warning', DeprecationWarning)


def test_unicode_literal_conversion():
    assert isinstance('ångström', six.text_type)


def test_doctest_float_replacement(tmpdir):
    test1 = dedent("""
        This will demonstrate a doctest that fails due to a few extra decimal
        places::

            >>> 1.0 / 3.0
            0.33333333333333331
    """)

    test2 = dedent("""
        This is the same test, but it should pass with use of
        +FLOAT_COMPARISON::

            >>> 1.0 / 3.0  # doctest: +FLOAT_COMPARISON
            0.33333333333333331
    """)

    test1_rst = tmpdir.join('test1.rst')
    test2_rst = tmpdir.join('test2.rst')
    test1_rst.write(test1)
    test2_rst.write(test2)

    with pytest.raises(doctest.DocTestFailure):
        doctest.testfile(str(test1_rst), module_relative=False,
                         raise_on_error=True, verbose=False, encoding='utf-8')

    doctest.testfile(str(test2_rst), module_relative=False,
                     raise_on_error=True, verbose=False, encoding='utf-8')
