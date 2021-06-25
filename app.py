from flask import Flask, jsonify, request
from db import Database



if __name__ == "__main__":
    app = Flask("API_Base_Noticias")
    db = Database("mongodb+srv://dbadmin:LF8arsE78T6BFOfj@newsdb.lv5a5.mongodb.net/newsdb?retryWrites=true&w=majority", "news_database")

    @app.route("/view", methods=["GET"])
    def view():
        result = db.list_posts()
        if result["error"]:
            return jsonify(result["error"])
        else:
            return jsonify(result["output"])

    @app.route("/search", methods=["GET"])
    def search():
        query = request.args.get("q")
        result = db.search_post(query)
        if result["error"]:
            return jsonify(result["error"])
        else:
            return jsonify(result["output"])

    @app.route("/insert", methods=["POST"])
    def insert():
        news_post = request.get_json()
        author_name = news_post["author"]
        author = db.search_author(author_name)
        if author["error"]:
            db.insert_author({"name": author_name})
        result = db.insert_post(news_post)
        if result["error"]:
            return jsonify(result["error"])
        else:
            return jsonify("Inserted.")

    @app.route("/update", methods=["PUT"])
    def update():
        query = request.args.get("q")
        news_post = request.get_json()
        author_name = news_post["author"]
        author = db.search_author(author_name)
        if author["error"]:
            db.insert_author({"name": author_name})
        result = db.update_post(query, news_post)
        if result["error"]:
            return jsonify(result["error"])
        else:
            return jsonify("Updated.")

    @app.route("/delete", methods=["DELETE"])
    def delete():
        query = request.args.get("q")
        result = db.delete_post(query)
        if result["error"]:
            return jsonify(result["error"])
        else:
            return jsonify("Deleted.")

    @app.route("/authors", methods=["GET"])
    def authors():
        result = db.list_authors()
        if result["error"]:
            return jsonify(result["error"])
        else:
            return jsonify(result["output"])

    app.run(host="127.0.0.1", port=3000, debug=True)
