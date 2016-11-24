#!/usr/bin/env python

# @Author: mdrhri-6
# @Date:   2016-11-19T10:31:52+01:00
# @Last modified by:   mdrhri-6
# @Last modified time: 2016-11-24T18:53:58+01:00

from flask import Flask, request, render_template, json, jsonify
import boto3
import datetime

app = Flask(__name__)
app.config['DEBUG'] = True
cwclient = boto3.client('cloudwatch', )

@app.route('/')
def hello():
    return render_template("index.html")


@app.route("/api/get_cpu_utilization")
def get_cpu_utilization():
    kw_args = {
        'Namespace': 'AWS/EC2',
        'MetricName': 'CPUUtilization',
        'StartTime': datetime.datetime.utcnow() - datetime.timedelta(minutes=45),
        'EndTime': datetime.datetime.utcnow(),
        'Period': 60,
        'Statistics': ['SampleCount', 'Average', 'Sum', 'Minimum', 'Maximum'],
        'Dimensions': [
            {'Name': 'InstanceId', 'Value': 'i-0bd38be22ce886804'}
        ]
    }

    response = cwclient.get_metric_statistics(**kw_args)

    idx = 0
    x_data = list()
    y_data = list()

    response['Datapoints'].sort(key=lambda x: x['Timestamp']) #region_name='us-east-2'

    for each in response['Datapoints']:
        t = str(each['Timestamp']).split('+')[0].strip() # 2016-11-04 00:00:04+0:00
        x_data.insert(idx, t.split(' ')[1].strip())
        y_data.insert(idx, each['Average'])
        idx += 1
    resp = list()
    resp.insert(0, x_data)
    resp.insert(1, y_data)
    return jsonify(resp)


@app.route("/api/get_status_check_failed")
def get_status_check_failed():
    kw_args = {
        'Namespace': 'AWS/EC2',
        'MetricName': 'StatusCheckFailed_Instance',
        'StartTime': datetime.datetime.utcnow() - datetime.timedelta(minutes=45),
        'EndTime': datetime.datetime.utcnow(),
        'Period': 60,
        'Statistics': ['SampleCount', 'Average', 'Sum', 'Minimum', 'Maximum'],
        'Dimensions': [
            {'Name': 'InstanceId', 'Value': 'i-0bd38be22ce886804'}
        ]
    }

    response = cwclient.get_metric_statistics(**kw_args)

    idx = 0
    x_data = list()
    y_data = list()

    response['Datapoints'].sort(key=lambda x: x['Timestamp'])

    for each in response['Datapoints']:
        t = str(each['Timestamp']).split('+')[0].strip()
        x_data.insert(idx, t.split(' ')[1].strip())
        y_data.insert(idx, each['Average'])
        idx += 1
    resp = list()
    resp.insert(0, x_data)
    resp.insert(1, y_data)
    return jsonify(resp)

@app.route("/api/get_network_in")
def get_network_in():
    kw_args = {
        'Namespace': 'AWS/EC2',
        'MetricName': 'NetworkIn',
        'StartTime': datetime.datetime.utcnow() - datetime.timedelta(minutes=45),
        'EndTime': datetime.datetime.utcnow(),
        'Period': 60,
        'Statistics': ['SampleCount', 'Average', 'Sum', 'Minimum', 'Maximum'],
        'Unit': 'Bytes',
        'Dimensions': [
            {'Name': 'InstanceId', 'Value': 'i-0bd38be22ce886804'}
        ]
    }

    response = cwclient.get_metric_statistics(**kw_args)

    idx = 0
    x_data = list()
    y_data = list()

    response['Datapoints'].sort(key=lambda x: x['Timestamp'])

    for each in response['Datapoints']:
        t = str(each['Timestamp']).split('+')[0].strip()
        x_data.insert(idx, t.split(' ')[1].strip())
        y_data.insert(idx, each['Average'])
        idx += 1
    resp = list()
    resp.insert(0, x_data)
    resp.insert(1, y_data)
    return jsonify(resp)


@app.route("/api/get_network_out")
def get_network_out():

    kw_args = {
        'Namespace': 'AWS/EC2',
        'MetricName': 'NetworkOut',
        'StartTime': datetime.datetime.utcnow() - datetime.timedelta(minutes=45),
        'EndTime': datetime.datetime.utcnow(),
        'Period': 60,
        'Statistics': ['SampleCount', 'Average', 'Sum', 'Minimum', 'Maximum'],
        'Unit': 'Bytes',
        'Dimensions': [
            {'Name': 'InstanceId', 'Value': 'i-0bd38be22ce886804'}
        ]
    }

    response = cwclient.get_metric_statistics(**kw_args)

    idx = 0
    x_data = list()
    y_data = list()

    response['Datapoints'].sort(key=lambda x: x['Timestamp'])

    for each in response['Datapoints']:
        t = str(each['Timestamp']).split('+')[0].strip()
        x_data.insert(idx, t.split(' ')[1].strip())
        y_data.insert(idx, each['Average'])
        idx += 1
    resp = list()
    resp.insert(0, x_data)
    resp.insert(1, y_data)
    return jsonify(resp)


@app.route("/api/get_disk_read_bytes")
def get_disk_read_bytes():
    kw_args = {
        'Namespace': 'AWS/EC2',
        'MetricName': 'DiskReadBytes',
        'StartTime': datetime.datetime.utcnow() - datetime.timedelta(minutes=45),
        'EndTime': datetime.datetime.utcnow(),
        'Period': 60,
        'Statistics': ['SampleCount', 'Average', 'Sum', 'Minimum', 'Maximum'],
        'Unit': 'Bytes',
        'Dimensions': [
            {'Name': 'InstanceId', 'Value': 'i-0bd38be22ce886804'}
        ]
    }

    response = cwclient.get_metric_statistics(**kw_args)

    idx = 0
    x_data = list()
    y_data = list()

    response['Datapoints'].sort(key=lambda x: x['Timestamp'])

    for each in response['Datapoints']:
        t = str(each['Timestamp']).split('+')[0].strip()
        x_data.insert(idx, t.split(' ')[1].strip())
        y_data.insert(idx, each['Average'])
        idx += 1
    resp = list()
    resp.insert(0, x_data)
    resp.insert(1, y_data)
    return jsonify(resp)


@app.route("/api/get_disk_write_bytes")
def get_disk_write_bytes():
    kw_args = {
        'Namespace': 'AWS/EC2',
        'MetricName': 'DiskWriteBytes',
        'StartTime': datetime.datetime.utcnow() - datetime.timedelta(minutes=45),
        'EndTime': datetime.datetime.utcnow(),
        'Period': 60,
        'Statistics': ['SampleCount', 'Average', 'Sum', 'Minimum', 'Maximum'],
        'Unit': 'Bytes',
        'Dimensions': [
            {'Name': 'InstanceId', 'Value': 'i-0bd38be22ce886804'}
        ]
    }

    response = cwclient.get_metric_statistics(**kw_args)

    idx = 0
    x_data = list()
    y_data = list()

    response['Datapoints'].sort(key=lambda x: x['Timestamp'])

    for each in response['Datapoints']:
        t = str(each['Timestamp']).split('+')[0].strip()
        x_data.insert(idx, t.split(' ')[1].strip())
        y_data.insert(idx, each['Average'])
        idx += 1
    resp = list()
    resp.insert(0, x_data)
    resp.insert(1, y_data)
    return jsonify(resp)


if __name__ == '__main__':
    app.run(host='0.0.0.0')



'''
Further Task:
    - Monitoring Service
        - Collect data for past few days(10days/1month/6months)
        - Get Stat on hourly basis(CPU Utilization)
        - Prediction Service(Based on NB)
'''
