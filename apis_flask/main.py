from flask import Flask, request, abort, make_response, jsonify

tasks = [
    {
        "id": 1,
        "title": u"Buy groceries",
        "description": u"Milk, Cheese, Pizza, Fruit, Tylenol",
        "done": False,
    },
    {
        "id": 2,
        "title": u"Learn Python",
        "description": u"Need to find a good Python tutorial on the web",
        "done": False,
    },
]

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


@app.route("/")
def hola():
    return "Bienvenido a Flask"


def _new(title, desc):

    nueva_tarea = {
        "id": int(tasks[-1]["id"]) + 1,
        "title": title,
        "description": desc,
        "done": False,
    }

    tasks.append(nueva_tarea)

    return nueva_tarea


def _replace(task_id, title, desc, done=False):
    # buscar mismo id
    global tasks
    repetido = [t for t in tasks if int(t["id"]) == int(task_id)]
    if repetido:
        tasks.remove(repetido)
        nueva_tarea = {
            "id": int(task_id),
            "title": title,
            "description": desc,
            "done": done,
        }
        tasks.append(nueva_tarea)
        tasks = sorted(tasks, key=lambda x: x["id"])

        return nueva_tarea

    else:
        task = _new(title=title, desc=desc)
        return task
    # si existe
    # eliminar
    # append el nuevo
    # ordenar con tasks = sorted(tasks, key=lambda x: x["id"])

    # si no existe
    # _new(title, desc)


@app.route("/lista/api/v1/tareas", methods=["GET", "POST"])
def get_tasks():
    if request.method == "GET":
        return jsonify({"tareas": tasks})
    ### el json que se recive ahora SI que tiene el parametro id
    #     if "id" in request.args:
    #         parametro_id = int(request.args["id"])
    ### si delete = 1.
    ### Si el id existe: eliminar esa tarea, añadir la
    ### tarea nueva y ordenar las tareas por `id`
    ### Si el id NO existe: generar el siguiente id, aadir la tarea
    ### normalmente con el id incrementado
    ### si delete = 0
    ### nos olvidamos del `id`. Generamos uno nuevo y añadimos a la
    ### lista de tareas
    ### si no delete / delete = 0
    elif request.method == "POST":
        if not request.json:
            abort(404)
        if "delete" in request.args:
            param_del = int(request.args["delete"])

        if param_del == 1:
            nueva_tarea = _replace(
                task_id=request.json["id"],
                title=request.json["title"],
                desc=request.json["desc"],
                done=request.json["done"],
            )

        else:
            nueva_tarea = _new(
                title=request.json["title"], desc=request.json["description"]
            )
            return jsonify({"tarea": nueva_tarea}), 201

        return jsonify({"tarea": nueva_tarea}), 201
    else:
        abort(404)


@app.route("/lista/api/v1/tareas/<int:id_tarea>", methods=["GET"])
def get_taks(id_tarea):

    tarea = None

    for t in tasks:
        if t["id"] == id_tarea:
            tarea = t
            break

    if not tarea:
        abort(404)

    return jsonify({"tarea": tarea})


app.run(host="0.0.0.0", port=5000)
