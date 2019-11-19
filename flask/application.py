from flask import Flask, Response, request
from Visualization.VisualizationAPI import VisualizationAPI as vis_tools
from MachineLearning.MachineLearningAPI import MachineLearningAPI as ml_tools
from Helper.geocoder import getLatLong
import json
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

@application.route("/api/visualization/wordcloud", methods=["GET"])
def wordcloud_data():
    parameter = request.args['parameter']
    rsp_data = vis_tools.wordcloud(parameter)
    rsp_status = 200
    full_rsp = Response(json.dumps(rsp_data, default=str),
                            status=rsp_status, content_type="application/json")
    return full_rsp

@application.route("/api/visualization/barchart", methods=["GET"])
def barchart_data():
    parameter1 = request.args['parameter1']
    parameter2 = request.args['parameter2']
    limit = int(request.args['limit'])
    matchValue = request.args['matchValue']
        
    rsp_data = vis_tools.barchart(limit, parameter1, parameter2, matchValue)
    rsp_status = 200
    full_rsp = Response(json.dumps(rsp_data, default=str),
                            status=rsp_status, content_type="application/json")
    return full_rsp

@application.route("/api/visualization/donutchart", methods=["GET"])
def donutchart_data():
    parameter = request.args['parameter']
    limit = request.args['limit']
    rsp_data = vis_tools.donutchart(parameter, limit)
    rsp_status = 200
    full_rsp = Response(json.dumps(rsp_data, default=str),
                            status=rsp_status, content_type="application/json")
    return full_rsp

@application.route("/api/visualization/correlation", methods=["GET"])
def correlation_data():
    rsp_data = vis_tools.correlationmatrix()
    rsp_status = 200
    full_rsp = Response(json.dumps(rsp_data, default=str),
                            status=rsp_status, content_type="application/json")
    return full_rsp

@application.route("/api/visualization/markers", methods=["GET"])
def scatterplot_data():
    rsp_data = vis_tools.markers()
    rsp_status = 200
    full_rsp = Response(json.dumps(rsp_data, default=str),
                            status=rsp_status, content_type="application/json")
    return full_rsp

@application.route("/api/visualization/choropleth", methods=["GET"])
def choropleth_data():
    rsp_data = vis_tools.choropleth()
    rsp_status = 200
    full_rsp = Response(json.dumps(rsp_data, default=str),
                            status=rsp_status, content_type="application/json")
    return full_rsp

@application.route("/api/prediction", methods=["GET"])
def prediction():
    location = request.args['location']
    month = request.args['month']
    dayofweek = request.args['dayofweek']
    latitude, longitude = getLatLong(location)
    rsp_data = ml_tools.prediction(month, dayofweek, latitude, longitude)
    rsp_status = 200
    full_rsp = Response(json.dumps(rsp_data, default=str),
                                status=rsp_status, content_type="application/json")
    return full_rsp

if __name__ == '__main__':
    application.run(debug=True)