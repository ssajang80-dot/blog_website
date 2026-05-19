import os
import glob
from flask import Flask, render_template, abort
import frontmatter
import markdown

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

POSTS_DIR = os.path.join(os.path.dirname(__file__), "../posts")


def get_all_posts():
    posts = []
    pattern = os.path.join(POSTS_DIR, "*.md")
    for filepath in sorted(glob.glob(pattern), reverse=True):
        post = frontmatter.load(filepath)
        slug = os.path.splitext(os.path.basename(filepath))[0]
        posts.append({
            "slug": slug,
            "title": post.get("title", "제목 없음"),
            "date": post.get("date", ""),
            "summary": post.get("summary", ""),
            "tags": post.get("tags", []),
        })
    return posts


def get_post(slug):
    filepath = os.path.join(POSTS_DIR, f"{slug}.md")
    if not os.path.exists(filepath):
        return None
    post = frontmatter.load(filepath)
    content_html = markdown.markdown(
        post.content,
        extensions=["fenced_code", "tables", "nl2br"]
    )
    return {
        "slug": slug,
        "title": post.get("title", "제목 없음"),
        "date": post.get("date", ""),
        "tags": post.get("tags", []),
        "content": content_html,
    }


@app.route("/")
def index():
    posts = get_all_posts()
    return render_template("index.html", posts=posts)


@app.route("/post/<slug>")
def post(slug):
    p = get_post(slug)
    if p is None:
        abort(404)
    return render_template("post.html", post=p)


@app.route("/about")
def about():
    return render_template("about.html")


# Vercel 핸들러
handler = app
