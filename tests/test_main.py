# -*- coding: utf-8 -*-

import pytest
from mock import patch
from gc_test.main import setup_logging, main, run, parse_args, calculate
from gc_test.utils import populate_models, data_source, create_db, Product

__author__ = "Kewei Duan"
__copyright__ = "Kewei Duan"
__license__ = "mit"


def test_calculate():
    assert calculate("A") == (50.0, [])
    assert calculate("AB") == (80.0, [])
    assert calculate("CDBA") == (115.0, [])
    assert calculate("AA") == (100.0, [])
    assert calculate("AAA") == (130.0, [])
    assert calculate("AAABB") == (175.0, [])
    with pytest.raises(AssertionError):
        calculate(None)

def test_parse_args():
    assert parse_args(['-v', 'ABCD1436y']).__str__() == "Namespace(loglevel=20, n='ABCD1436y')"

@patch('logging.basicConfig')
def test_logging(loggingconf):
    setup_logging(20)
    loggingconf.called_once()


@patch('gc_test.utils.Product')
def test_populate_models(product):
    populate_models(data_source)
    assert product.create.call_count == 4

@patch('gc_test.utils.database')
def test_create_db(sqldb):
    create_db([Product])
    sqldb.create_tables.assert_called_once_with([Product])

@patch('gc_test.main.parse_args')
@patch('gc_test.main._logger')
@patch('gc_test.main.calculate')
@patch('builtins.print')
def test_main_with_diff(mprint, calc, logger, parse):
    calc.return_value = 100.0, ['A']
    main(['ABCD1436y'])
    parse.called_once()
    calc.called_once()
    logger.debug.called_once()
    logger.info.called_once()
    assert mprint.call_count == 2

@patch('gc_test.main.parse_args')
@patch('gc_test.main._logger')
@patch('gc_test.main.calculate')
@patch('builtins.print')
def test_main_without_diff(mprint, calc, logger, parse):
    calc.return_value = 100.0, []
    main(['ABCD1436y'])
    parse.called_once()
    calc.called_once()
    logger.debug.called_once()
    logger.info.called_once()
    assert mprint.call_count == 1

@patch('gc_test.main.main')
def test_run(tmain):
    run()
    tmain.called_once()
