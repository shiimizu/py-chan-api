# testing

### Objective:
- **Unify:** Convert other imageboards to the 4chan api in JSON format
- **Wrapper:** Parse the JSON to programming-language-specific data structures
- **Extra:** Ability to download JSON + media (`--oneshot`)
    - Which would include handling the rate limit

### Why?
I have a lot of threads archived in a plaintext list of links for educational purposes. With the advent of archiving sites cracking down, I realized that it won't always be here and I'd need to save it locally. Later on, it reminded me that not just these need to be archived but everything else on the internet that I value.
```python
Single thread: 'posts'
Thread index: 'threads'
Board List: 'boards'
Board Catalog: 'page'
Thread list: 'post'
Archived Threads: [list of numbers]
Single post: Non existant
```
### Supports:
|   Feature                     |                        Source                             |
|-------------------------------|-----------------------------------------------------------|
|   ✔️ Single thread             |`a.4cdn.org/{board}/thread/{threadnumber}.json`            |
|   ✔️ Thread index                |`a.4cdn.org/{board}/{pagenumber}.json` (threads @ pg #)    |
|   ✔️ Board list                  |`a.4cdn.org/boards.json`                                   |
|    Board catalog             |`a.4cdn.org/{board}/catalog.json`                          |
|   Thread list                 |`a.4cdn.org/{board}/threads.json`                          |
|   Archived threads            |`a.4cdn.org/{board}/archive.json`                          |
|  ⚠️ HTTPS                       |On by default in `urllib3`                                 |
|  ⚠️ Rate limiting               |`x` requests allowed in `n` seconds                        |
|  ⚠️ `If-Modified-Since`         |`req.headers['last-modified']`                             |
|  ⚠️ In-place thread updating |`req.headers['last-modified']; difflib`                    |

|**Extra Imageboards** | Compatibility |
|-------------------------------|----------|
|✔️ [FFuuka](https://archive.4plebs.org/_/articles/credits/#archives)|  `Thread`, `Post` |
|:grey_question: warosu|
|:grey_question: yuki.la |
### Usage

```python
# pychan would infer what type of json you're giving it. See the above table.

post = pychan(thread.posts[0])
thread = pychan("thread.json")
threadIndex = pychan("thread_index.json")
board = pychan("boards.json")
thread = pychan("thread.json")

print(thread)                       # Print to see what keys you can call
print(thread.posts[0].com)          # Get the first post and its comment


###### [REDACTED] ######
catalog = <UNDER CONSTRUCTION>
```
### Converting
```python
thread = pychan.Fuuka("thread.json")    # Just use the imageboard implentation
```

### Todo
- [ ] All the non-checked

### Support
Pull requests are welcome.
Contact shiimizu @ this [Matrix](https://matrix.to/#/#bibanon-chat:matrix.org) server


### ⚠️ Polling (`archiving`)
- Archiving capabilities are beyond the scope of this project.
- Please see :arrow_right:
  - [`eve`](https://github.com/bibanon/eve)
  - [`hayden`](https://github.com/bbepis/Hayden)
  - [`basc-archiver`](https://github.com/bibanon/BASC-Archiver)
  - [`go-4chan-api`](https://github.com/moshee/go-4chan-api)
