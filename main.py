#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import logging
import jinja2
import os
from google.appengine.ext import ndb
from datetime import datetime

#template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
DATE_FORMAT = "%b %d %Y %I:%M%p"
BEGINNING_OF_TIME = 'Jan 1 1000 12:01AM'

#eg Jun 1 2005 1:33PM

class User(ndb.Model):
	username = ndb.StringProperty()
	task_ids = ndb.IntegerProperty(repeated=True)

class Task(ndb.Model):
	title = ndb.StringProperty()
	start = ndb.DateTimeProperty()
	end = ndb.DateTimeProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class createTaskHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('createTask.html')
		#todo: pass user variables to customize page
		self.response.write(template.render())

	def post(self):
		title = self.request.get('title')
		start = self.request.get('start')
		end = self.request.get('end')
		start = datetime.strptime(start, DATE_FORMAT)
		end = datetime.strptime(end, DATE_FORMAT)
		new_task = Task(title=title, start=start, end=end)
		new_task.put()
		#maybe reply with a success message

class showTasksHandler(webapp2.RequestHandler):
	def get(self):
		now = datetime.strftime(datetime.now(), DATE_FORMAT)
		start = self.request.get('start') or BEGINNING_OF_TIME
		end = self.request.get('end') or now
		start = datetime.strptime(start, DATE_FORMAT)
		end = datetime.strptime(end, DATE_FORMAT)
		
		tasks = Task.query(Task.start>start and Task.end<end).fetch()
		
		template = jinja_environment.get_template('schedule.html')
		self.response.write(template.render({'tasks':tasks}))
		#todo: separate >20 tasks into multiple pages

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/createTask', createTaskHandler),
    ('/schedule', showTasksHandler),
], debug=True)
