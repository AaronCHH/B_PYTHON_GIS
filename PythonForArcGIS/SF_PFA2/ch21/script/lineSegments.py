# lineSegments.py
# Purpose: Define a LineSegment class
# Usage: No arguments required

import math


class LineSegment:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calculateLength(self):
        '''Calculate the length of this line segment'''
        return math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)

    def calculateSlope(self):
        '''Calculate the slope of this line segment.'''
        run = self.x2 - self.x1
        if run == 0:
            return "undefined"
        else:
            return (self.y2 - self.y1)/float(run)

    def translateY(self, yShift):
        '''Translate the line vertically by yShift
        (Shifts the line segment up or down.)'''
        self.y1 = self.y1 + yShift
        self.y2 = self.y2 + yShift
