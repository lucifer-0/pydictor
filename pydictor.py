#!/usr/bin/env python
# coding:utf-8
# A useful hacker dictionary builder for a brute-force attack
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
from lib.fun.fun import cool
from core.SEDB import SEDB
from core.BASE import get_base_dic
from core.CHAR import get_char_dic
from core.CHUNK import get_chunk_dic
from lib.data.data import paths, pyoptions
from lib.data.text import pydictor_art_text
from lib.parse.command import parse_args
from lib.parse.tricksparse import sedb_tricks
from lib.parse.argsparse import plug_parser, conf_parser, tool_parser


def init():
    args = parse_args()

    pyoptions.leetmode_code = args.mode
    paths.results_path = os.path.abspath(args.output)
    pyoptions.head = args.head
    pyoptions.tail = args.tail
    pyoptions.encode = args.encode
    pyoptions.minlen = args.len[0]
    pyoptions.maxlen = args.len[1]

    pyoptions.args_base = args.base
    pyoptions.args_char = args.char
    pyoptions.args_chunk = args.chunk
    pyoptions.args_plug = args.plug
    pyoptions.args_sedb = args.sedb
    pyoptions.args_conf = args.conf
    pyoptions.args_tool = args.tool
    pyoptions.args_sedb = args.sedb
    pyoptions.args_conf = args.conf
    pyoptions.args_pick = args.pick

    try:
        if not os.path.exists(paths.results_path):
            os.mkdir(paths.results_path)
    except IOError:
        exit(pyoptions.CRLF + cool.red("[-] Cannot create output path: %s " % paths.results_path))


if __name__ == '__main__':
    print("{}".format(cool.green(pydictor_art_text)))
    init()
    if pyoptions.args_base:
        get_base_dic(pyoptions.args_base)
    elif pyoptions.args_char:
        get_char_dic(pyoptions.args_char)
    elif pyoptions.args_chunk:
        get_chunk_dic(pyoptions.args_chunk)
    elif pyoptions.args_plug:
        plug_parser()
    elif pyoptions.args_sedb:
        try:
            sedb_tricks()
            shell = SEDB()
            shell.cmdloop()
        except Exception as e:
            exit(e)
    elif pyoptions.args_conf != 'default':
        conf_parser()
    elif pyoptions.args_tool:
        tool_parser()
