#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
import os
import random
import jinja2

def get_fortune():
    #add a list of fortunes to the empty fortune_list array
    fortune_list = ['Sam is going to beat you in your sleep tonight', 'Sam will teach you stack utilization in your bathroom',
                    'You will become fluent in all programing languages, but you can only speak using C++', 'Dr O will come to your house and sing you a lullaby in javascript',
                    'Kristian will engage you in a dance battle at the USU in 10 minutes', 'Sam is watching you',
                    'You will have all of stack overflow in your mind but you can only hear in binary', 'Kristan and Sam will beat you in your sleep tonight',
                    'System.out.println("you live in Java now.")', 'is this base64? .- .... .-. ----- -.-. .... -- -.... .-.. -.-- ----. -. -... ..--- ---.. ..- --.. ..--- .-- ...- .-. -. .-. .... -... -- --.. -.',
                    'add me on league lmao: Apochromatic']
    #use the random library to return a random element from the array
    random_fortune = fortune_list[random.randint(0,len(fortune_list)-1)]
    return(random_fortune)


#remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        mypage = jinja_current_directory.get_template('templates/fortune_start.html')
        self.response.write(mypage.render())
    def post(self):
        user_astro_sign = self.request.get('user_astrological_sign')
        mypage = jinja_current_directory.get_template('templates/fortune_results.html')
        self.response.write(mypage.render({'sign':user_astro_sign, 'fortune':get_fortune()}))


class HelloHandler(webapp2.RequestHandler):
    def get(self):
        mypage = jinja_current_directory.get_template('templates/fortune_start.html')
        self.response.write('Kappa')



class GoodByeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Time to hit the noose')

#the route mapping
app = webapp2.WSGIApplication([
    #this line routes the main url ('/')  - also know as
    #the root route - to the Fortune Handler
    ('/', HelloHandler),
    ('/predict', FortuneHandler), #maps '/predict' to the FortuneHandler
    ('/farewell', GoodByeHandler)
], debug=True)
