# ---------------------------------------------------------------------
# Project "Track 3D-Objects Over Time"
# Copyright (C) 2020, Dr. Antje Muntzinger / Dr. Andreas Haja.
#
# Purpose of this file : Kalman filter class
#
# You should have received a copy of the Udacity license together with this program.
#
# https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013
# ----------------------------------------------------------------------
#

# imports
import numpy as np

# add project directory to python path to enable relative imports
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import misc.params as params 

class Filter:
    '''Kalman filter class'''
    def __init__(self):
        self.dim_state = params.dim_state
        self.dt = params.dt
        self.q = params.q
        #pass

    def F(self):
        ############
        # TODO Step 1: implement and return system matrix F
        ############

        dt = self.dt # get time step increment
        F = np.matrix([
                [1, 0, 0, dt, 0, 0],
                [0, 1, 0, 0, dt, 0],
                [0, 0, 1, 0, 0, dt],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1]])
        #print(F)
        return F
        #return 0
        
        ############
        # END student code
        ############ 

    def Q(self):
        ############
        # TODO Step 1: implement and return process noise covariance Q
        ############

        dt = self.dt
        q = self.q
        q0 = ((dt**3)/3) * q 
        q1 = ((dt**2)/2) * q 
        q2 = dt * q

        return np.matrix([[q0, 0, 0, q1, 0, 0],
                          [0, q0, 0, 0, q1, 0],
                          [0, 0, q0, 0, 0, q1],
                          [q1, 0, 0, q2, 0, 0],
                          [0, q1, 0, 0, q2, 0],
                          [0, 0, q1, 0, 0, q2]])
        
        return 0
        
        ############
        # END student code
        ############ 

    def predict(self, track):
        ############
        # TODO Step 1: predict state x and estimation error covariance P to next timestep, save x and P in track
        ############
        F = self.F()
        x = F*track.x
        P = F*track.P*F.T + self.Q()

        track.set_x(x)
        track.set_P(P)
        
        ############
        # END student code
        ############ 

    def update(self, track, meas):
        ############
        # TODO Step 1: update state x and covariance P with associated measurement, save x and P in track
        ############
        
        x = track.x
        P = track.P
        H = meas.sensor.get_H(x)

        gamma = self.gamma(track, meas)

        S = self.S(track, meas, H)

        # calculate Kalman filter gain matrix
        K = P*H.transpose()*np.linalg.inv(S)
        x = x + K*gamma
        I = np.identity(self.dim_state)
        P = (I - K*H) * P
        track.set_x(x)
        track.set_P(P)
        ############
        # END student code
        ############ 
        track.update_attributes(meas)
    
    def gamma(self, track, meas):
        ############
        # TODO Step 1: calculate and return residual gamma
        ############
        hx = meas.sensor.get_hx(track.x)
        return meas.z - hx
        #return 0
        
        ############
        # END student code
        ############ 

    def S(self, track, meas, H):
        ############
        # TODO Step 1: calculate and return covariance of residual S
        ############
        P = track.P
        return H*P*H.T + meas.R
        #return 0
        
        ############
        # END student code
        ############ 