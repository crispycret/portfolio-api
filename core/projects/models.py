from .. import db


class ProjectStatus(db.Model):
    __tablename__ = 'project_status'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False, unique=True)



class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False, unique=True)
    summary = db.Column(db.String(128), nullable=False)
    version = db.Column(db.String(64), nullable=False)
    status = db.Column(db.Integer, db.ForeignKey('project_status.id'))
    githubUrl = db.Column(db.String(128))
    websiteUrl = db.Column(db.String(128))
    imageUrl = db.Column(db.String(128))
    created = db.Column(db.DateTime())
    updated = db.Column(db.DateTime())



