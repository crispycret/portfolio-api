from flask import request

from .. import db
from ..auth.decorators import require_admin, require_token

from . import projects
from .models import Project, ProjectStatus


@projects.route('/')
def get_projects ():
    try:
        projects = Project.query.all()
        projects = [p.serialize for p in projects]
        return {'status': 200, 'msg': f'retrieved {len(projects)} projects', 'body': projects}
    except Exception as e:
        return {'status': 400, 'msg': 'could not retrieve projects', 'body': str(e)}



# @require_token
@projects.route('/create', methods=['POST'])
@require_admin
def create_project(user, token):
    try:
        data = request.get_json()

        if (not data):
            return {'status': 400, 'msg': 'expected `project` object in request.', 'body': {}}

        if ('id' in data):
            del data['id']

        # Given a status by name, replace with id
        if ('status' in data and type(data['status'] == str)):
            status = ProjectStatus.query.filter_by(name=data['status']).first()
            if (not status): 
                return {'status': 400, 'msg': f'Could not find the project status "{data["status"]}".', 'body': {}}
            data['status'] = status.id


        # Check if project exists
        project = Project.query.filter_by(title=data['title']).first()
        if (project): return {'status': 400, 'msg': 'Project with title already exists', 'body': {}}

        # Create Project
        project = Project.create(**data)
        db.session.add(project)
        db.session.commit()
        return {'status': 200, 'msg': 'Project created', 'body': {}}
    except Exception as e: 
        # 'failed to create project'
        return {'status': 400, 'msg': str(e), 'body': {}}





@projects.route('/id/<id>/edit', methods=['PATCH'])
@require_admin
def edit_project_by_id(user, token):
    try:
        return {'status': 200, 'msg': 'index', 'body': {}}
    except: pass
    return {'status': 400, 'msg': 'failed to edit project', 'body': {}}



@projects.route('/edit', methods=['PATCH'])
@require_admin
def edit_project(user, token):
    try:
        data = request.get_json()

        if ('description' in data):
            data['summary'] = data['description']
            del data['description']

        # Check if project exists
        # project = Project.query.filter_by(title=data['title']).first()
        project = Project.query.filter_by(id=data['id']).first()
        if (not project): return {'status': 400, 'msg': 'Project does not exists', 'body': {}}

        del data['id']
        try:
            for key, value in data:
                setattr(project, key, value)
            db.session.commit()
            return {'status': 200, 'msg': 'Project edited', 'body': {}}
        except: return {'status': 200, 'msg': 'Failed to edit project', 'body': {}}
    except: return {'status': 400, 'msg': 'failed to edit project', 'body': {}}



@projects.route('/id/<id>/delete', methods=['DELETE'])
@require_admin
def delete_project(id, admin, token):
    try:
        p = Project.query.filter_by(id=id).first()
        db.session.commit(p)
        db.session.commit()
        return {'status': 200, 'msg': 'index', 'body': {}}
    except: pass
    return {'status': 400, 'msg': 'failed to delete project', 'body': {}}




@projects.route('/statuses', methods=['GET'])
def get_statuses (): 
    try:
        statuses = ProjectStatus.query.all()
        data = [status.serialize for status in statuses]
        return {'status': 200, 'msg': 'project statuses retrieved', 'body': data}
    except Exception as e:
        return {'status': 400, 'msg': 'failed to get statuses', 'body': {}}



@projects.route('/status/create', methods=['POST'])
@require_admin
def create_project_status(user, token):
    try:
        data = request.get_json()
        status = ProjectStatus(name=data['name'])
        db.session.add(status)
        db.session.commit()
        return {'status': 200, 'msg': 'index', 'body': {}}
    except: pass
    return {'status': 400, 'msg': 'failed to create project status', 'body': str(e)}



@projects.route('/status/<id>/delete', methods=['POST'])
@require_admin
def delete_project_status(id, admin, token):
    try:
        status = ProjectStatus.query.filter_by(id=id)
        db.session.delete(status)
        db.session.commit()
        return {'status': 200, 'msg': 'index', 'body': {}}
    except: pass
    return {'status': 400, 'msg': 'failed to delete project', 'body': {}}


