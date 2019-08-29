#!/usr/bin/env python
import os
import sys
import json
import time
import re
import copy
import psutil
import gc
import time
import multiprocessing as mp
import concurrent.futures
import bigjson
from .fourchan import FourChan

# Reference
#   db = {"posts": [{"bumplimit": 0, "ext": ".jpg"},{"bumplimit": 1, "ext": ".png"}]}
#   print(json.dumps(db,sort_keys=True,indent=4))

process = psutil.Process(os.getpid())
debug = False # {True: "For useful logging", False: "To sit back and relax"}

ls = ['desu_thread.json','nyafuu_thread.json','desu_onepiece_thread.json']
outs = ['out1.json','out2.json','out3.json','']

def Fuuka(db, parallel = None):
    """Currently only supports an inputted file due to how bigjson works. It would have to be implemented. See line 106"""
    if not db: raise Exception("Input cannot be empty")
    if isinstance(db, dict):
        inputs = list(db.keys())
        outputs = list(db.values())
        if parallel == None: parallel = True
    elif isinstance(db, str):
        inputs = [db]
        outputs = [None]
        if parallel == None: parallel = False
    else: raise Exception("Unknown input and output formats")
    
    if parallel:
        return FourChan(multiprocess(inputs, outputs))
    else:
        return FourChan(sequential(inputs, outputs))
#class Fuuka():
#    name = "Fuuka"
#    def __new__(self, db):
#        return Chan(sequential(db, 'out11.json'))

def main():
    
    for file in ls:
        if not os.path.exists(file): return print(f"[NON-EXISTENT]: {file}")
    
    print(f"\nMax processes available: {mp.cpu_count()} ", end='')
    
    # Test sequential
    #for i in range(4):
    #    pjson('desu_thread.json','out.json')
    
    measure(sequential, 'desu_thread.json', 'out.json')
    #measure(multiprocess)

def measure(method, input=ls[0], output=outs[0]):
    start = time.time()
    if method is sequential:
        method(input, output)
    else:
        method()
    gc.collect()
    print("--- [END] Total: {} ms ---\n".format(float((time.time() - start)*1000)))
    
def sequential(inputs, outputs):
    if debug:
        if not os.path.exists(input): return print(f"[NON-EXISTENT]: {input}\n")
        print("[SEQUENTIAL]\n")
    ls = []
    for i in range(len(inputs)):
        ls.append(pjson(inputs[i], outputs[i]))
    return ls[0] if len(ls) == 1 else ls

def multiprocess(inputs, outputs):
    if debug:
        if len(ls) != len(outs): return print(f"[ERROR]: List of inputs must have the same size as list of outputs.\n")
        print("[MULTIPROCESSING]\n")
    ls = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(inputs, executor.map(pjson,inputs,outputs)):
            ls.append(prime)
            #pass
            #print( number, prime)
    return ls[0] if len(ls) == 1 else ls

def pjson(input,output):
    """Process to JSON"""
    start = time.time()
    proc = psutil.Process()
    d("Start time: {}".format(start))
    d(f'Started PID: {proc.pid} Using affinity: {proc.cpu_affinity()}')
    with open(input,'rb') as file:#, open(output, 'w') as out:
        mem()
        
        # Stream JSON file
        js = bigjson.load(file)
        for (key, value) in js.iteritems():
            thread_id = key
        
        # Migrating OP
        op_post = js[thread_id]['op'].to_python()
        p,i,s = process_post(op_post,int(op_post['num']),0,"")
        op_post = p
        try:
            op_post['unique_ips'] = int(''.join(filter(str.isdigit, op_post.get('exif', None))))
        except:
            pass
        ls = [op_post]
        
        # Deal with the rest of the posts
        replies = 0
        images = 0
        resto = op_post['no']
        semantic_url = ""
        if 'posts' in js[thread_id]:
            posts = js[thread_id]['posts']
            for (key, value) in posts.iteritems():
                replies += 1
                post = value.to_python()
                
                p,i,s = process_post(post,key,resto,semantic_url)
                post = p
                images += i
                semantic_url = s
                    
                ls.append(post)
                
            # OP patching
            op_post['replies'] = replies
            sem_url = re.sub(r"[^a-zA-Z0-9]+", '-', semantic_url).lower().lstrip('-')
            op_post['semantic_url'] = sem_url if sem_url else re.sub(r"[^a-zA-Z0-9]+", '-', op_post['comment']).lower()[:50].lstrip('-')
            op_post['images'] = images
            op_post['bumplimit'] = 0
            op_post['imagelimit'] = 0
            
        
        db = {"posts": ls}
        
        # Output to file
        if output:
            with open(output, 'w') as out:
                json.dump(db,out,sort_keys=True,indent=2)
        del posts
        del ls
        del op_post
        mem()
        d('Finished. PID: {}'.format(os.getpid()))
        d("--- {} ms ---".format(float((time.time() - start)*1000)))
        return db

def process_post(post, key, resto, semantic_url):
    images = 0
    semantic_url = ""
    
    # Accomodate for rare bug in json
    if f'{key}' in post and post[f'{key}']:
        post['media'] = post.pop(f'{key}', None)
        
    
    if 'media' in post and post['media']:
        post.update(post.pop('media', None))
        post['ext'] = os.path.splitext(post['media_filename'])[1]
        post['filename'] = post.pop('media_filename', None)
        post['fsize'] = int(post.pop('media_size', None))
        post['md5'] = post.pop('media_hash', None)
        post['tn_h'] = int(post.pop('preview_h', None))
        post['tn_w'] = int(post.pop('preview_w', None))
        post['h'] = int(post.pop('media_h', None))
        post['w'] = int(post.pop('media_w', None))
        images = 1
    
    # if 'board' in post and post['board']: post['board'] = post['board']['shortname']
    def RepresentsInt(s):
        try: 
            return int(s)
        except:
            return 0
    
    post['com'] = post.pop('comment_processed', None)
    post['id'] = post.pop('poster_hash', None)
    post['no'] = int(post.pop('num', None))
    post['now'] = post.pop('fourchan_date', None)
    post['sub'] = post.pop('title', None)
    post['time'] = post.pop('timestamp',None)
    post['tim'] = post['time'] * 1000 if not post.get('media_orig', None) else int(os.path.splitext(post.get('media_orig', None))[0])
    post['resto'] = resto
    post['locked'] = RepresentsInt(post.get('locked', None)) 
    post['deleted'] = RepresentsInt(post.get('deleted', None))
    post['sticky'] = RepresentsInt(post.get('sticky', None))
    post['spoiler'] = RepresentsInt(post.get('spoiler', None))
    post['banned'] = RepresentsInt(post.get('banned', None))
    post['doc_id'] = RepresentsInt(post.get('doc_id', None))
    #post['thread_num'] = RepresentsInt(post.get('thread_num', None))
    post['unique_ips'] = RepresentsInt(post.get('unique_ips', None))
    
    # OP patching
    if not semantic_url and post['sub']: semantic_url = post['sub']
    
    # Post processing
    post.pop('name_processed', None)
    post.pop('capcode', None)
    post.pop('total', None)
    post.pop('timestamp_expired', None)
    post.pop('op', None)
    post.pop('board', None)
    post.pop('subnum', None)
    post.pop('uniqueIps', None)
    post.pop('extra_data', None)
    post.pop('thread_num', None)
    if post.get('comment_sanitized', None) == post.get('', None): post.pop('comment_sanitized', None)
    empty_keys = [k for k,v in post.items() if not v]
    for k in empty_keys:
        del post[k]
    return [post, images,semantic_url]

def d(s):
    """Debug printer"""
    if debug: print(s)

def pj(jdb):
    """Dumps pretty JSON"""
    return json.dumps(jdb,sort_keys=True,indent=4)

def bget(jdb,s):
    """Better get. Check for nonetype"""
    try:
        return jdb.get(s)
    except:
        pass
    return None

def mem():
    """Get the current memory usage for this program"""
    if debug: print(f"{process.memory_info().rss/1000000} MB") 

def pid_info():
    print(f"Program PID: {os.getpid()}")
    for proc in psutil.process_iter():
        if "python" in proc.name(): print(proc)

#if __name__ == '__main__':
#    main()