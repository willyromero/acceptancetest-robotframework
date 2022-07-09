import robot.api.logger
import robot.utils.asserts
import sys
sys.path.append('../')
import test_cases as ft

_test_case_response = {'rtc1': None, 'rtc2': None, 'rtc3': None, 'rtc4': None, 'rtc5': None}

def camera_no_started(probability, name):
    robot.api.logger.info('Test case 1 tested with probability of %f' % float(probability))
    _test_case_response['rtc1'] =ft.test_case_1(probability, name)

def check_camera_no_started(expected):
    _actual = _test_case_response['rtc1']
    robot.utils.asserts.assert_equal(expected, _actual)

def unrecognized_face(probability, name):
    robot.api.logger.info('Test case 2 tested with probability of %f' % float(probability))
    _test_case_response['rtc2'] =ft.test_case_2(probability, name)

def check_unrecognized_face(expected):
    _actual = _test_case_response['rtc2']
    robot.utils.asserts.assert_equal(expected, _actual)

def recognized_face(probability, name):
    robot.api.logger.info('Test case 3 tested with probability of %f' % float(probability))
    _test_case_response['rtc3'] =ft.test_case_3(probability, name)

def check_recognized_face(expected):
    _actual = _test_case_response['rtc3']
    robot.utils.asserts.assert_equal(expected, _actual)

def unrecognized_face_key(probability, name):
    robot.api.logger.info('Test case 4 tested with probability of %f' % float(probability))
    _test_case_response['rtc4'] =ft.test_case_4(probability, name)

def check_unrecognized_face_key(expected):
    _actual = _test_case_response['rtc4']
    robot.utils.asserts.assert_equal(expected, _actual)

def recognized_face_key(probability, name):
    robot.api.logger.info('Test case 5 tested with probability of %f' % float(probability))
    _test_case_response['rtc5'] =ft.test_case_5(probability, name)

def check_recognized_face_key(expected):
    _actual = _test_case_response['rtc5']
    robot.utils.asserts.assert_equal(expected, _actual)
