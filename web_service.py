# Description: This file contains the web service that will be used to call the flood function
#              from the flood.py file. The web service will be called using a POST from a ReactJS application.
#              The web service will return a 400 error if the parameters are not correct.
#              The web service will return a 201 status code if the parameters are correct.
# Parameters: originalGrid - a grid of cells.
#             cellPosition - a tuple of the form (row, column) that represents
#                            the cell position to be flooded
#             newColor - An Hex RGB color that represents the new color to flood
#                        the cells with.
# Return value: a new grid of cells with the cell position and all the cells
#               connected to it with the same color as the cell position flooded
#               with the new color. The rest of the cells will keep their original color.

from flask import Flask, abort, request, jsonify
from flask_cors import cross_origin
from flood import generated_flooded_grid

app = Flask(__name__)

@app.route('/flood', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def flood():
    if not request.json or not 'originalGrid' in request.json or not 'cellPosition' in request.json or not 'newColor' in request.json:
        abort(400)
    originalGrid = request.json['originalGrid']
    cellPosition = request.json['cellPosition']
    newColor = request.json['newColor']
    floodedGrid = generated_flooded_grid(originalGrid, cellPosition, newColor)
    return jsonify({'floodedGrid': floodedGrid}), 201

if __name__ == '__main__':
    app.run(debug=True)