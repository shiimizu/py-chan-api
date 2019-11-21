# py-chan-api

### Objective:
- **Unification:** Have one library to use for multiple imageboards. Convert them to 4chan compliant API specifications.
- **Wrapper:** Parse the JSON to programming-language-specific data structures (in this case, to Python).

### API Documentation
#### 4chan
* [Official](https://github.com/4chan/4chan-API)
* [Alternate](https://github.com/catamphetamine/imageboard/blob/master/docs/engines/4chan.md)

#### FFuuka based Imageboards
* [Official (Github)](https://github.com/FoolCode/FoolFuuka-docs/blob/master/code_guide/documentation/api.rst)
* [Official (Website)](https://4plebs.tech/foolfuuka)
* [Readthedocs](https://foolfuuka.readthedocs.io/en/latest/code_guide/documentation/api.html)

---

|   Feature                     |                        Source                             |
|-------------------------------|-----------------------------------------------------------|
|   ✔️ Single thread             |`a.4cdn.org/{board}/thread/{threadnumber}.json`            |
|   ✔️ Thread index                |`a.4cdn.org/{board}/{pagenumber}.json` (threads @ pg #)    |
|   ✔️ Board list                  |`a.4cdn.org/boards.json`                                   |
|   ✔️ Board catalog             |`a.4cdn.org/{board}/catalog.json`                          |
|   ✔️ Thread list                 |`a.4cdn.org/{board}/threads.json`                          |
|  ✔️ Archived threads            |`a.4cdn.org/{board}/archive.json`                          |
|  🚧 HTTPS                       |On by default in `urllib3`                                 |
|  🚧 Rate limiting               |`x` requests allowed in `n` seconds                        |
|  🚧 `If-Modified-Since`         |`req.headers['last-modified']`                             |
|  🚧 In-place thread updating |`req.headers['last-modified']; difflib`                    |

### Extra Support
|**Extra Imageboards** | Compatibility |
|-------------------------------|----------|
|✔️ [FFuuka](https://archive.4plebs.org/_/articles/credits/#archives)|  `Thread`, `Post` |
|❔ [warosu](https://warosu.org)|
|❔ [yuki.la](https://yuki.la) |

---

### Installation
```console
$ pip install py-chan-api             # NOTE: Only Python 3.7+

# Or with virtualenv
$ pip install virtualenv              # Install virtualenv if you haven't already
$ virtualenv venv                     # Create a virtualenv
$ source venv/bin/activate            # Activate it
$ pip install py-chan-api             # Install py-chan-api
```

### Usage

```python
import pychan

# pychan infers what type of object you're giving it. See the above table.
# Whether its a string pointing to a file/dict/dict in string format.

threadIndex     = pychan.FourChan("thread_index.json")
board           = pychan.FourChan("boards.json")
thread          = pychan.FourChan("thread.json")
threadList      = pychan.FourChan("thread_list.json")
archivedThread  = pychan.FourChan("archived_threads.json")
post            = thread.posts[0]

print(thread.posts[0].com)              # Get the first post and its comment

print(post)                             # If you're unsure of what fields to call
                                        # just print the object itself to see a list of key/values

# Or see the type of the unknown object
print(type(pychan.FourChan("unknown.json")))

print(thread.posts[0])
print(threadIndex.threads[0].posts[1])
print(board.trollflags.AC)
print(board.boards[0].title)
print(catalog.page[0].threads[0])
print(threadList.page[0].threads[0])
print(archivedThread[-1])

# To get individual key value/pairs
jdb = thread.posts[0].json              # Convert the Post object to a dictionary
for k,v in jdb.items():                 # Iterate through the key/value pairs
    print(k, v)
```

### Converting

```python
import pychan
fuukaThread = pychan.Fuuka("desu_thread.json")    # Specify the imageboard implementation

# Parallelism (multiprocessing) is turned on automatically if you supply more
# than one key/value pairs in a dictionary.
# You can override this behaviour by specifying the parallel field
# By using a dictionary, you can also output it to a file.
fthread1 = pychan.Fuuka({"desu_thread.json" : "out1.json"}, parallel = True)

# Which then you could read it as a normal 4chan json
fthread = pychan.FourChan("out1.json")

# We can also just use the outputed value from before
print(fthread1.posts[1])      # Note: fthread1 is the same as fthread and fuukaThread
```

### Tests
Tests are done with [`pytest`](https://pytest.org/en/latest/).
```console
$ pip install -U pytest pytest-xdist
$ pytest tests.py -v
```

### Support
Pull requests are welcome.
Feel free to ping shiimizu @ [this](https://matrix.to/#/#bibanon-chat:matrix.org) Matrix server.


### ⚠️ Archiving (polling)
- Archiving capabilities are beyond the scope of this project.
- Please see:
  - [`eve`](https://github.com/bibanon/eve)
  - [`hayden`](https://github.com/bbepis/Hayden)
  - [`basc-archiver`](https://github.com/bibanon/BASC-Archiver)
  - [`go-4chan-api`](https://github.com/moshee/go-4chan-api)
