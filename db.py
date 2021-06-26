import pymongo
from bson.objectid import ObjectId


class Database:
    def __init__(self, uri: str, database_name: str):
        self.client = pymongo.MongoClient(uri)
        self.db = self.client[database_name]

    def list_posts(self):
        data = []
        for document in self.db["news"].find():
            del document["_id"]
            data.append(document)
        if(len(data) > 0):
            return {
                "error": None,
                "output": data
            }
        else:
            return {
                "error": "Query error.",
                "output": []
            }

    def search_post(self, title: str):
        result = self.db["news"].find_one({"title": title})
        if(result):
            result["_id"] = None
            return {
                "error": None,
                "output": result
            }
        else:
            return {
                "error": "Query error.",
                "output": {}
            }

    def insert_post(self, post: dict):
        assert post["title"] is not None, "Post title is not present."
        assert type(post["title"]) == str, "Post title accepts only string."
        assert post["title"] != "", "Post title can not be empty."
        assert len(post["title"]) <= 255, "Post title size can be less or equal to 255."

        assert post["text"] is not None, "Post text is not present."
        assert type(post["text"]) == str, "Post text accepts only string."
        assert post["text"] != "", "Post text can not be empty."

        assert post["author"] is not None, "Post author is not present."
        assert type(post["author"]) == str, "Post author accepts only string."
        assert post["author"] != "", "Post author can not be empty."
        assert len(post["author"]) <= 128, "Post author size can be less or equal to 128."

        result = self.db["news"].insert_one(post)
        if(result.inserted_id):
            return {
                "error": None,
                "output": None
            }
        else:
            return {
                "error": "Insert error.",
                "output": None
            }

    def update_post(self, title: str, post: dict):
        assert post["title"] is not None, "Post title is not present."
        assert type(post["title"]) == str, "Post title accepts only string."
        assert post["title"] != "", "Post title can not be empty."
        assert len(post["title"]) <= 255, "Post title size can be less or equal to 255."

        assert post["text"] is not None, "Post text is not present."
        assert type(post["text"]) == str, "Post text accepts only string."
        assert post["text"] != "", "Post text can not be empty."

        assert post["author"] is not None, "Post author is not present."
        assert type(post["author"]) == str, "Post author accepts only string."
        assert post["author"] != "", "Post author can not be empty."
        assert len(post["author"]) <= 128, "Post author size can be less or equal to 128."

        result = self.db["news"].update_one({"title": title}, { "$set": post})
        if(result.modified_count > 0):
            return {
                "error": None,
                "output": None
            }
        else:
            return {
                "error": "Update error.",
                "output": None
            }

    def delete_post(self, title: str):
        result = self.db["news"].delete_one({"title": title})
        if(result.deleted_count > 0):
            return {
                "error": None,
                "output": None
            }
        else:
            return {
                "error": "Delete error.",
                "output": None
            }

    def list_authors(self):
        data = []
        for document in self.db["authors"].find():
            del document["_id"]
            data.append(document)
        if(len(data) > 0):
            return {
                "error": None,
                "output": data
            }
        else:
            return {
                "error": "Query error.",
                "output": []
            }

    def search_author(self, name: str):
        result = self.db["authors"].find_one({"name": name})
        if(result):
            del result["_id"]
            return {
                "error": None,
                "output": result
            }
        else:
            return {
                "error": "Query error.",
                "output": {}
            }

    def insert_author(self, author: dict):
        assert author["name"] is not None, "Author name is not present."
        assert type(author["name"]) == str, "Author name accepts only string."

        result = self.db["authors"].insert_one(author)
        if(result.inserted_id):
            return {
                "error": None,
                "output": None
            }
        else:
            return {
                "error": "Insert error.",
                "output": None
            }

    def update_author(self, name: str, author: dict):
        assert author["name"] is not None, "Author name is not present."
        assert type(author["name"]) == str, "Author name accepts only string."

        result = self.db["authors"].update_one({"name": name}, { "$set": author})
        if(result.modified_count > 0):
            return {
                "error": None,
                "output": None
            }
        else:
            return {
                "error": "Update error.",
                "output": None
            }

    def delete_author(self, name: str):
        result = self.db["authors"].delete_one({"name": name})
        if(result.deleted_count > 0):
            return {
                "error": None,
                "output": None
            }
        else:
            return {
                "error": "Delete error.",
                "output": None
            }