#! /usr/bin/python

from flask import Flask, request
app = Flask(__name__)
# Create the appropriate app.route functions, test and see if they work, and paste your URIs in the boxes below.

# Make an app.route() decorator here


@app.route('/puppies', methods = ['GET', 'POST'])
def puppiesFunction():
    if request.method == 'GET':
        return getAllPuppies()
    elif request.method == 'POST':
        return makeANewPuppy()
# Make another app.route() decorator here that takes in an integer id in the


@app.route('/puppies/<int:id>', methods= ['GET','PUT','DELETE'])
def puppiesFunctionId(id):
    if request.method == 'GET':
        getPuppy(id)
    if request.method == 'PUT':
        updatePuppy(id)
    elif request.method == 'DELETE':
        deletePuppy(id)


def getAllPuppies():
    return "Getting All the puppies!"


def makeANewPuppy():
    return "Creating A New Puppy!"


def getPuppy(id):
    return "Getting Puppy with id %s" % id


def updatePuppy(id):
    return "Updating a Puppy with id %s" % id


def deletePuppy(id):
    return "Removing Puppy with id %s" % id

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)	