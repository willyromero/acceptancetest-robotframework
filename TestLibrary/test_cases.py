import cv2
import recognize.src.acceptancetest.recognizeFaceTest as rf1
import recognize.src.acceptancetest.recognizeFaceTest2 as rf2
import recognize.src.acceptancetest.recognizeFaceTest3 as rf3
import socketio

socket = socketio.Client()

def test_case_1(probability, name):
    cap = cv2.VideoCapture()
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    socket.connect("http://localhost:3000/")
    response = rf1.recognize(int(probability), cap, faceClassif, socket, name)
    socket.disconnect()
    return response

def test_case_2(probability, name):
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    print("prob   ", probability)
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    socket.connect("http://localhost:3000/")
    response = rf2.recognize(int(probability), cap, faceClassif, socket, name)
    socket.disconnect()
    return response

def test_case_3(probability, name):
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    socket.connect("http://localhost:3000/")
    response = rf2.recognize(int(probability), cap, faceClassif, socket, name)
    socket.disconnect()
    return response


def test_case_4(probability, name):
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    socket.connect("http://localhost:3000/")
    response = rf3.recognize(int(probability), cap, faceClassif, socket, name)
    socket.disconnect()
    return response


def test_case_5(probability, name):
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    socket.connect("http://localhost:3000/")
    response = rf3.recognize(int(probability), cap, faceClassif, socket, name)
    socket.disconnect()
    return response
