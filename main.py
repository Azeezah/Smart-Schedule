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

#template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

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
		#todo: write createTask.html template
		#todo: pass user variables to customize page
		self.response.write(template.render())

	def post(self):
		title = self.request.get('title')
		start = self.request.get('start')
		end = self.request.get('end')
		#todo: define str_to_datetime
		#start, end = str_to_datetime(start), str_to_datetime(end)
		new_task = Task(title=title, start=start, end=end)
		task.put()
		#maybe reply with a success message



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/createTask', createTaskHandler),
], debug=True)
