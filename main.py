#!/usr/bin/env python

"""main.py - This file contains handlers that are called by taskqueue and/or
cronjobs."""

import webapp2
from google.appengine.api import mail, app_identity

from models import User, Game


class SendReminderEmail(webapp2.RequestHandler):
    def get(self):
        """Send a reminder email to each User with
        an email that has been part of a cancelled game
        and the reminder has not been already sent.
        Called every 5 minutes using a cron job"""
        app_id = app_identity.get_application_id()
        cancelled_games = Game.query(Game.cancelled == True,
                                     Game.email_reminder_sent == False)

        for game in cancelled_games:
            user11 = User.query(User.key == game.user1).get()
            user22 = User.query(User.key == game.user2).get()

            subject = 'This is a reminder!'
            body = 'Hello {}, your Tic Tac Toe game with {} has been '
            'cancelled. Please send a reply if you want to'
            ' continue this game!'
            # This will send test emails, the arguments to send_mail are:
            # from, to, subject, body
            mail.send_mail('noreply@{}.appspotmail.com'.format(app_id),
                           user11.email,
                           subject,
                           body.format(user11.name, user22.name))

            mail.send_mail('noreply@{}.appspotmail.com'.format(app_id),
                           user22.email,
                           subject,
                           body.format(user22.name, user11.name))

            game.email_reminder_sent = True
            game.put()


app = webapp2.WSGIApplication([
    ('/crons/send_reminder', SendReminderEmail)
], debug=True)
