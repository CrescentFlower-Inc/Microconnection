from tortoise import Tortoise
from pathlib import Path

DBLOC = Path(__file__).parents[1] / "database/database.sqlite3"
DBURL = "sqlite:////" + str(DBLOC)

TORTOISE_ORM = {
	"connections": {"default": DBURL},
	"apps": {
		"models": {
			"models": ["microconnection.models", "aerich.models"],
			"default_connections": "default"
		}
	}
}



async init_tortoise():
	await Tortoise.init(TORTOISE_ORM)
