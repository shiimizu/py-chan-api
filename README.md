# py-chan-api

### Objective:
- **Unify:** Convert other imageboards to the 4chan api in JSON format
- **Wrapper:** Parse the JSON to programming-language-specific data structures
- **Extra:** Ability to download JSON + media ⚠️

### Why?
I have a lot of threads archived in a plaintext list of links for educational purposes. With the advent of archiving sites cracking down, I realized that it won't always be here and I'd need to save it locally. Later on, it reminded me that not just these need to be archived but everything else on the internet that I value.

### Supports:
|   Feature                     |                        Source                             |
|-------------------------------|-----------------------------------------------------------|
|   ✔️ Single thread             |`a.4cdn.org/{board}/thread/{threadnumber}.json`            |
|   ✔️ Thread index                |`a.4cdn.org/{board}/{pagenumber}.json` (threads @ pg #)    |
|   ✔️ Board list                  |`a.4cdn.org/boards.json`                                   |
|   ✔️ Board catalog             |`a.4cdn.org/{board}/catalog.json`                          |
|   ✔️ Thread list                 |`a.4cdn.org/{board}/threads.json`                          |
|  ✔️ Archived threads            |`a.4cdn.org/{board}/archive.json`                          |
|  ⚠️ HTTPS                       |On by default in `urllib3`                                 |
|  ⚠️ Rate limiting               |`x` requests allowed in `n` seconds                        |
|  ⚠️ `If-Modified-Since`         |`req.headers['last-modified']`                             |
|  ⚠️ In-place thread updating |`req.headers['last-modified']; difflib`                    |

|**Extra Imageboards** | Compatibility |
|-------------------------------|----------|
|✔️ [FFuuka](https://archive.4plebs.org/_/articles/credits/#archives)|  `Thread`, `Post` |
|❔ warosu|
|❔ yuki.la |

### Installation
```python
pip install py-chan-api             # NOTE: Only Python 3.7+

# Or with virtualenv
pip install virtualenv              # Install virtualenv if you havent already
virtualenv venv                     # Create a virtualenv
source venv/bin/activate            # Activate it
pip install -r requirements.txt     # Install required modules
pip install py-chan-api             # Install py-chan-api
```
### Usage

```python
import pychan

# pychan infers what type of object you're giving it. See the above table.
# Whether its a string pointing to a file/dict/dict in string format.

thread          = pychan.FourChan("thread.json")
post            = thread.posts[0]
threadIndex     = pychan.FourChan("thread_index.json")
board           = pychan.FourChan("boards.json")
thread          = pychan.FourChan("thread.json")
threadList      = pychan.FourChan("thread_list.json")
archivedThread  = pychan.FourChan("archived_threads.json")

print(thread.posts[0].com)              # Get the first post and its comment

print(post)                             # If you're unsure of what fields to call
                                        # just print the object itself to see a list of key/values
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

### Support
Pull requests are welcome.
Feel free to ping shiimizu @ this [Matrix](https://matrix.to/#/#bibanon-chat:matrix.org) server.


### ⚠️ Polling (`archiving`)
- Archiving capabilities are beyond the scope of this project.
- Please see :arrow_right:
  - [`eve`](https://github.com/bibanon/eve)
  - [`hayden`](https://github.com/bbepis/Hayden)
  - [`basc-archiver`](https://github.com/bibanon/BASC-Archiver)
  - [`go-4chan-api`](https://github.com/moshee/go-4chan-api)
