from flask import Flask, request, Response
from altgraph import GraphAlgo, Graph
import json

app = Flask(__name__)


def fail_no_solution():
    return fail("status", "No solution found")


def fail_invalid_input():
    return fail("error", "Invalid input")


def fail(msg_type, msg):
    return Response(response=json.dumps({
                "solution": None,
                "length": None,
                msg_type: msg
            }), status=200)


def solve_maze(task_str):
    task = json.loads(task_str)
    try:
        start = task["start"]
        end = task["end"]
        rooms = task["rooms"]
        corrs = task["corridors"]
    except KeyError:
        return fail_invalid_input()

    if max(map(lambda x: rooms.count(x), rooms)) > 1\
            or start not in rooms\
            or end not in rooms:
        return fail_invalid_input()

    graph = Graph.Graph()
    for room in rooms:
        graph.add_node(room)
    for src, dst in corrs:
        if src not in rooms or dst not in rooms:
            return fail_invalid_input()
        graph.add_edge(src, dst)
        graph.add_edge(dst, src)

    try:
        path = GraphAlgo.shortest_path(graph, start, end)
        resp = json.dumps({
            "solution": path,
            "length": len(path),
            "status": "OK"
        })
        return Response(response=resp, status=200)
    except KeyError:
        return fail_no_solution()


@app.route('/', methods=['GET', 'POST'])
def maze_solver():
    if request.method == 'GET':
        return Response(response="", status=200)
    if request.method == 'POST':
        return solve_maze(request.data)


if __name__ == '__main__':
    app.run()
