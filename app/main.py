from app import app
from config import Configuration
import view
from app import db 
from posts.blueprint import posts
from map.blueprint import maps

app.register_blueprint(maps,url_prefix = '/maps')
app.register_blueprint(posts, url_prefix = '/blog')


	







if __name__ == '__main__':
	app.run()