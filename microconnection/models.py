from tortoise.models import Model
from tortoise import fields


class AnnouncementSource(Model):
	id = fields.IntField(pk=True) # ID of source

	name = fields.TextField()   # Name of source
	source_cid = fields.IntField() # channel id of source
	source_gid = fields.IntField() # guild id of seource


class AnnouncementSubscription(Model):
	id = fields.IntField(pk=True) # ID of subscription

	receiverServer = fields.IntField() # ID of receiving server
	receiverChannel = fields.IntField() # ID of receiving channel

	source = fields.ForeignKeyField('models.AnnouncementSource')


