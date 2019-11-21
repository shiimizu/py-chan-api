#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import sys
import shutil
import pychan
import pytest

def test_fourchan_empty_dict():
    with pytest.raises(Exception):
        thread = pychan.FourChan("{}")
        
def test_fourchan_unknown_dict():
    with pytest.raises(Exception):
        thread = pychan.FourChan("""{ "zxc": "qwe", "cvz": 123 }""")
def test_fourchan_unknown_string():
    with pytest.raises(Exception):
        thread = pychan.FourChan("""n78yo342v>{?>L}?~!@#+_)|}{\\|""")
        
def test_fourchan_empty_list():
    with pytest.raises(Exception):
        thread = pychan.FourChan("[]")
        
def test_fourchan_unknown_list():
    with pytest.raises(Exception):
        thread = pychan.FourChan("[1]")

def test_fourchan_unknown_list_2():
    with pytest.raises(Exception):
        thread = pychan.FourChan("[1,2,34,5]")
        
def test_fourchan_unknown_list_3():
    with pytest.raises(Exception):
        thread = pychan.FourChan("['zxc', 'qwe']")
    
#@pytest.mark.xfail(raises=Exception)
def test_fourchan_parse_fuuka_thread():
    with pytest.raises(Exception):
        thread = pychan.FourChan("tests/desu_thread.json")
    
def test_fuuka_thread_conversion():
    fuukaThread = pychan.Fuuka("tests/desu_thread.json")
    assert isinstance(fuukaThread, pychan.fourchan.Thread)
    
def test_fuuka_thread_to_json_conversion():
    fuukaThread = pychan.Fuuka("tests/desu_thread.json")
    assert isinstance(fuukaThread.json, dict)
    
def main():
    fuukaThread = pychan.Fuuka("desu_thread.json")
    fthread1 = pychan.Fuuka({"desu_thread.json" : "out1.json"})
    fthread = pychan.FourChan("out1.json")
    #print(repr(str(fthread1.posts[1])))
    
    # repr(str(fthread1.posts[1]))
    assert str(fthread1.posts[1]) == """'{\n  "doc_id": 259727564,\n  "name": "Anonymous",\n  "comment": ">>192166777\\nShould have watched Madoka instead.",\n  "comment_sanitized": ">>192166777\\nShould have watched Madoka instead.",\n  "com": "<span class=\\"greentext\\"><a href=\\"http://desuarchive.org/a/thread/192166777/#192166777\\" class=\\"backlink op\\" data-function=\\"highlight\\" data-backlink=\\"true\\" data-board=\\"a\\" data-post=\\"192166777\\">&gt;&gt;192166777</a></span><br />\\nShould have watched Madoka instead.",\n  "no": 192166871,\n  "now": "8/19/19(Mon)16:54",\n  "time": 1566248070,\n  "tim": 1566248070000,\n  "resto": 192166777\n}'""".strip("'")

if __name__ == '__main__':
    test_main()
