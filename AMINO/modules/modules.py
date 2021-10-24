import os
import sys
import logging

from AMINO.utils.dynamic_import import dynamic_import

def init_module(module_conf):
    try:
        net_class = dynamic_import(module_conf['select'])
    except Exception as e:
        logging.warning(
            f"""
                net class implement error: {e}, 
                please check {os.path.realpath(__file__)} to check net class
            """
        )
        sys.exit(1)
    try:
        net = net_class(**module_conf['conf'])
    except Exception as e:
        logging.warning(
            f"""
                net class object error: {e}, 
                please check {os.path.realpath(__file__)} 
                to check net class's in parameters
            """
        )
        sys.exit(2)
    return net