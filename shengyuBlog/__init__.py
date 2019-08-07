import os
from flask import Flask

def create_app():
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'shengyuBlog.sqlite')
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import posts
    app.register_blueprint(posts.bp)
    return app
