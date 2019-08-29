import os
import sys
import json
import time
import pychan
thread = pychan.FourChan("test_json/out.json")
#f = pychan.Fuuka("test_json/desu_thread.json")
post = thread.posts[0]

# Parallelism (multiprocessin) is turned on automatically if you supply more than one.
# You can override this behaviour by specifying parallel
# You can output it to a file by provviding a dictionary
#f = pychan.Fuuka({"test_json/desu_thread.json":"out1.json"}, parallel = False)
#pychan.Fuuka("desu_onepiece_thread.json", out="test", parallel = True)
#pychan.Fuuka("desu_onepiece_thread.json", out=["test","test2"], parallel = True)

# Which then you could read it as a normal 4chan json
#pp = pychan.FourChan("newly_converted.json")
#print(f.posts[1])
print(post)


#post = Post(thread.posts[0])
#thread = Thread("out.json")
#threadIndex = ThreadIndex("thread_index.json")
#board = BoardList("boards.json")
#catalog = Catalog("biz_catalog.json")
#threadList = ThreadList("thread_list.json")
#archivedThread = ArchivedThread("archived_threads.json")
#pt = pychan("out.json")

#print(post)
#print(thread.posts[0])
#print(threadIndex.threads[0].posts[1])
#print(board.trollflags.AC)
#print(board.boards[0].title)
#print(catalog.page[0].threads[0])
#print(threadList.page[0].threads[0])
#print(archivedThread[-1])
#print(pt.posts[0])

#for k,v in thread.posts[0].items():
#    print(k,type(v))