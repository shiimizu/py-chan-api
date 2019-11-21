#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
import os
import json
import ast


class Json():
    db: dict

    def load(self, db):
        if isinstance(db, str):
            if os.path.exists(db):
                with open(db, 'rb') as f:
                    try:
                        return json.loads(f.read())
                    except Exception as e:
                        return ast.literal_eval(f.read().decode())
            else:  # If path doesn't exist. Could be a JSON string.
                try:
                    return json.loads(db)
                except Exception as e:
                    raise Exception(e)
        else:
            return db

    def __str__(self):
        """Flatmap this object to primitive values and then to a string"""
        return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

    @property
    def json(self):
        """Return data structure as json dictionary.
        Useful for manually accessing keys/values"""
        return json.loads(self.__str__())


class BigJson(Json):
    def load(self, db):
        if isinstance(db, str):
            if os.path.exists(db):
                with open(db, 'rb') as f:
                    try:
                        return json.loads(f.read())
                    except Exception as e:
                        return ast.literal_eval(f.read().decode())
            else:  # If path doesn't exist
                try:
                    return json.loads(db)
                except Exception as e:
                    raise Exception(e)
        else:
            return db


class Post(Json):
    def __init__(self, db):
        self.__dict__.update(self.load(db))


class Thread(Json):
    def __init__(self, db):
        self.posts = [Post(x) for x in self.load(db)['posts']]


class ThreadIndex(Json):
    def __init__(self, db):
        self.threads = [Thread(x) for x in self.load(db)['threads']]


class Board(Json):
    """The directory the board is located in."""
    board: str

    def __init__(self, db):
        self.__dict__.update(self.load(db))

        """Docstring for class variable A.x"""
        self.y = 1


class TrollFlags(Json):
    def __init__(self, db):
        self.__dict__.update(self.load(db))


class Boards(list):
    def __init__(self):
        super().__init__()
        with open("tests/boards.json", mode='r', encoding='utf-8') as f:
            j = json.load(f)
            self.__db__: dict = j
            for a in j.get('boards', None):
                self.append(a)

    def huh(self):
        """List of all meme flags"""
        return

    def __str__(self):
        return json.dumps(self.__db__, indent=2)

    @property
    def trollflags(self):
        """List of all meme flags"""
        return {}

    @property
    def memeflags(self):
        """List of all meme flags"""
        return self.trollflags


class BoardList(Json):
    def __init__(self, db):
        self.boards = [Board(x) for x in self.load(db)['boards']]
        self.trollflags = TrollFlags(self.load(db)['troll_flags'])


class Page(Json):
    def __init__(self, db):
        self.page = self.load(db)['page']
        self.threads = [Post(x) for x in self.load(db)['threads']]


class Catalog(Json):
    def __init__(self, db):
        # print(type(self.load(db)[0]['threads'][0]))
        self.pages = len(self.load(db)) - 1
        self.page = [Page(p) for p in self.load(db)]


class ThreadList(Json):
    # Same as Catalog
    def __init__(self, db):
        self.pages = len(self.load(db)) - 1
        self.page = [Page(p) for p in self.load(db)]


class ArchivedThread(Json):
    def __new__(self, db):
        return self.load(self, db)


class FourChan(Json):
    def __new__(self, db):
        db = self.load(self, db)
        self.db = db
        if isinstance(db, dict):
            # Single Thread
            if db.get('posts', None):
                return Thread(db)

            # Thread Index
            elif db.get('threads', None):
                return ThreadIndex(db)

            # Board List
            elif db.get('boards', None):
                return BoardList(db)

            else:
                raise Exception("Unkown input type")

        elif isinstance(db, list):
            if len(db) <= 0: raise Exception("List is empty!")
            # Board Catalog
            if db[0].get('page', None):
                return Catalog(db)

            # Thread List
            elif ['no', 'last_modified', 'replies'] == [element for element in db[0]['threads'][0]]:
                return ThreadList(db)

            # Archived Threads
            else:
                newdb = [s for s in db if not isinstance(s, int)]
                if len(db) != 0 and len(newdb) == 0: return ArchivedThread(db)

        else:
            raise Exception("Unknown input type: {}".format(type(db)))
