import datetime
from .. import db


class ProjectStatus(db.Model):
    __tablename__ = 'project_status'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False, unique=True)

    @property
    def serialize (self):
        return {
            'id': self.id,
            'name': self.name
        }



class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    version = db.Column(db.String(64))
    status = db.Column(db.Integer, db.ForeignKey('project_status.id'))
    githubUrl = db.Column(db.String(128))
    websiteUrl = db.Column(db.String(128))
    imageUrl = db.Column(db.String(128))
    created = db.Column(db.DateTime())
    updated = db.Column(db.DateTime())


    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'version': self.version,
            'status': self.status,
            'githubUrl': self.githubUrl,
            'websiteUrl': self.websiteUrl,
            'imageUrl': self.imageUrl,
            'created': self.created,
            'updated': self.updated,
        }


    @staticmethod
    def create(**kwargs):
        try:
            kwargs['created'] = datetime.datetime.now()
            project = Project(**kwargs)
            return project
        except: 
            return None


