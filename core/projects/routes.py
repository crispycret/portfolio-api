from flask import request

from .. import db
from ..auth.decorators import require_admin

from . import projects
from .models import Project, ProjectStatus


@projects.route('/')
def index ():
    return {'status': 200, 'msg': 'index', 'body': {}}



@projects.route('/create')
@require_admin
def create_project(admin, token):
    data = request.get_json()
    try:
        return {'status': 200, 'msg': 'index', 'body': {}}
    except: pass
    return {'status': 400, 'msg': 'failed to create project', 'body': {}}



@projects.route('/id/<id>/edit')
@require_admin
def edit_project(admin, token):
    try:
        return {'status': 200, 'msg': 'index', 'body': {}}
    except: pass
    return {'status': 400, 'msg': 'failed to edit project', 'body': {}}



@projects.route('/id/<id>/delete')
@require_admin
def delete_project(id, admin, token):
    try:
        p = Project.query.filter_by(id=id).first()
        db.session.commit(p)
        db.session.commit()
        return {'status': 200, 'msg': 'index', 'body': {}}
    except: pass
    return {'status': 400, 'msg': 'failed to delete project', 'body': {}}



@projects.route('/status/create')
@require_admin
def create_project_status(admin, token):
    data = request.get_json()
    try:
        status = ProjectStatus(name=data['name'])
        db.session.add(status)
        db.session.commit()
        return {'status': 200, 'msg': 'index', 'body': {}}
    except: pass
    return {'status': 400, 'msg': 'failed to create project', 'body': {}}



@projects.route('/status/<id>/delete')
@require_admin
def delete_project_status(id, admin, token):
    try:
        status = ProjectStatus.query.filter_by(id=id)
        db.session.delete(status)
        db.session.commit()
        return {'status': 200, 'msg': 'index', 'body': {}}
    except: pass
    return {'status': 400, 'msg': 'failed to create project', 'body': {}}


