# from flask import jsonify #serializar objetos
from flask import Blueprint

from .models.task import Task
from .responses import response

api_v1 = Blueprint('api',__name__,url_prefix='/api/v1')

@api_v1.route('/tasks',methods=['GET'])
def get_tasks():
    # return jsonify({
    #     'message':'Hola desde el EndPoint- Listado de Tareas'
    # })
    tasks=Task.query.all() #SELECT * FROM TASKS;
    return response(
        [task.serialize() for task in tasks]
    )

@api_v1.route('/tasks/<id>',methods=['GET'])
def get_task():
    pass

@api_v1.route('/tasks',methods=['POST'])
def create_task():
    pass

@api_v1.route('/tasks/<id>',methods=['PUT'])
def update_task():
    pass

@api_v1.route('/tasks/<id>',methods=['DELETE'])
def delete_task():
    pass