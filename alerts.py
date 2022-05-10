"""
This module contains different alert mechanisms
"""

from statistics import calculateStats


class EmailAlert:
    def __init__(self):
        self.emailSent = False


class LEDAlert:
    def __init__(self):
        self.ledGlows = False


class StatsAlerter:
    def __init__(self, max_threshold, alerts):
        self.maxThreshold = max_threshold
        self.email_alert, self.led_alert = alerts

    def checkAndAlert(self, numbers):
        stats = calculateStats(numbers)
        if stats["max"] > self.maxThreshold:
            self.email_alert.emailSent = True
            self.led_alert.ledGlows = True
