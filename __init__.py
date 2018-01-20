# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.


# Visit https://docs.mycroft.ai/skill.creation for more detailed information
# on the structure of this skill and its containing folder, as well as
# instructions for designing your own skill based on this template.


# Import statements: the list of outside modules you'll be using in your
# skills, whether from other files in mycroft-core or from external libraries
from os.path import dirname, join, exists, splitext
from os import listdir
from time import sleep
from random import choice
from tinytag import TinyTag

#from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.skills.audioservice import AudioService
from mycroft.util.log import getLogger

__author__ = 'Hasinator7'

# Logger: used for debug lines, like "LOGGER.debug(xyz)". These
# statements will show up in the command line when running Mycroft.
LOGGER = getLogger(__name__)


# The logic of each skill is contained within its own class, which inherits
# base methods from the MycroftSkill class with the syntax you can see below:
# "class ____Skill(MycroftSkill)"
class NatureSoundSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(NatureSoundSkill, self).__init__(name="NatureSoundSkill")
        self.audioservice = None
        self.minPlayDuraion = None

    def getPath(self, name):
        return (join(dirname(__file__), "mp3", name))
    
    def getSounds(self):
        sound_files = self.getSoundFiles()
        sounds = []
        for f in sound_files:
            # make the filename speakable
            f = f.replace('.mp3', '')
            f = f.replace('-', ' ')
            sounds.append(f)
        return sounds
    
    def getSoundFiles(self):
        return [f for f in listdir(join(dirname(__file__), 'mp3')) if splitext(f)[1] == '.mp3']
    
    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses
    def initialize(self):
        self.register_intent_file('play.intent', self.handle_play_intent)
        self.register_intent_file('library.intent', self.handle_library_intent)
        
        self.minPlayDuraion = 3600  # set minimum play duraion to 1 hour
        
        if AudioService:
            self.audioservice = AudioService(self.emitter)
            self.audioservice.stop()
        
    # The "handle_xxxx_intent" functions define Mycroft's behavior when
    # each of the skill's intents is triggered: in this case, he simply
    # speaks a response. Note that the "speak_dialog" method doesn't
    # actually speak the text it's passed--instead, that text is the filename
    # of a file in the dialog folder, and Mycroft speaks its contents when
    # the method is called.
    #TODO: Loop mp3s

    def handle_play_intent(self, message):
        LOGGER.info('NatureSoundSkill: playing sound file')
        self.stop()  # ???? Just in case something is already playing ????
        sound = message.data.get('sound')
        try:
            sound = sound.replace(' ', '-')
        except:
            sound = ''
        LOGGER.info('NatureSoundSkill: Looking for ' + sound)
        path = self.getPath(sound + '.mp3')
        if not exists(path):  # can't find the sound file so play a random sound
            if sound:
                self.speak('sorry, I could not find that sound')
                sleep(1)
            self.speak('playing a random sound')
            path = self.getPath(choice(self.getSoundFiles()))
        # queue up about an hour's worth of listening
        tag = TinyTag.get(path)
        playlist = []
        for i in range(int(self.minPlayDuraion / tag.duration)):
            playlist.append(path)
        LOGGER.info('NatureSoundSkill: Playing ' + str(playlist))
        if self.audioservice:
            self.audioservice.play(playlist)  #, message.data['utterance'])

    def handle_library_intent(self, message):
        # list available relaxation music
        LOGGER.info('NatureSoundSkill: listing available sounds')
        sounds = self.getSounds()
        self.speak('Here are the sound files you have in your library')
        sleep(1)
        for sound in sounds:
            self.speak(sound)
            sleep(.75)
    
    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, the method just contains the keyword "pass", which
    # does nothing.
    def stop(self):
        if self.audioservice:
            self.audioservice.stop()

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return NatureSoundSkill()
