from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
posts = {
    0: {"post_id": 0, "title": "Hello, world", "content": "This is my first blog post!"}
}


@app.route("/")
def home():
    return "Hello, world!"


@app.route("/post/<int:post_id>")  # /post/0
def posts_page(post_id):
    post = posts.get(post_id)
    if not post:
        return render_template(
            "404.jinja2", message=f"A post with id {post_id} was not found."
        )
    return render_template("post.jinja2", post=post)


@app.route("/post/form")
def form():
    return render_template("create.jinja2")


@app.route("/post/create", methods=["POST"])
def create():
    title = request.form.get("title")
    content = request.form.get("content")
    post_id = len(posts)
    posts[post_id] = {"id": post_id, "title": title, "content": content}

    return redirect(url_for("posts_page", post_id=post_id))


if __name__ == "__main__":
    app.run(debug=True)
