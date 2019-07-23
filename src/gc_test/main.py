# -*- coding: utf-8 -*-
import argparse
import sys
import logging
from .utils import prods_str_to_dict
from .utils import get_models

from gc_test import __version__

__author__ = "Kewei Duan"
__copyright__ = "Kewei Duan"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def calculate(str_products):
    """Calculate the total price based on the products list in str

    Args:
      str_products (string): string

    Returns:
      float: total price
    """
    assert str_products is not None
    _logger.info("Total price calculation started.")
    dict_products = prods_str_to_dict(str_products)
    query_sku_list = list(dict_products.keys())
    results = get_models(query_sku_list)
    result_sku_list = []
    _logger.debug("Filtering result is: " + results)
    total_price = 0
    for product in results:
        result_sku_list.append(product.sku)
        trigger = product.trigger
        if trigger != 0:
            fdiv = (dict_products[product.sku])//(product.trigger)
            mod = (dict_products[product.sku])%(product.trigger)
            total_price += fdiv*(product.tprice) + (mod*product.price)
        else:
            total_price += (dict_products[product.sku])*(product.price)
    diff_skus = list(set(query_sku_list) - set(result_sku_list))
    _logger.info("Total price calcuation finished.")
    return total_price, diff_skus




def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Just a total price calculator")
    parser.add_argument(
        "--version",
        action="version",
        version="gc_test {ver}".format(ver=__version__))
    parser.add_argument(
        dest="n",
        help="String formed by SKU chars",
        type=str,
        metavar="STRING")
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO)
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG)
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting crazy calculations...")
    result, diff = calculate(args.n)
    print("The product {} total price is {}".format(args.n, result))
    if diff != []:
        print("The skus {} are not in system and not counted in.".format(diff))
    _logger.info("Script ends here")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
