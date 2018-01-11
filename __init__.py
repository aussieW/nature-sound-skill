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
from os.path import dirname, join
from os import listdir

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
try:
    from mycroft.skills.audioservice import AudioService
except:
    from mycroft.util import play_mp3
    AudioService = None

__author__ = 'Hasinator7'

# Logger: used for debug lines, like "LOGGER.debug(xyz)". These
# statements will show up in the command line when running Mycroft.
LOGGER = getLogger(__name__)

FOREST_WALK_URL = 'http://meditationroom.org/free-nature-sounds/forest-walk-audio/forest-walk.mp3'
MORNING_SEASHORE_URL = 'http://meditationroom.org/free-nature-sounds/morning-seashore-audio/morning-seashore.mp3'
SUMMER_RAIN_URL = 'http://meditationroom.org/free-nature-sounds/summer-rain-audio/summer-rain.mp3'
MOUNTAIN_STREAM_URL = 'http://meditationroom.org/free-nature-sounds/mountain-stream-audio/mountain-stream.mp3'
TROPICAL_BEACH_URL = 'http://meditationroom.org/free-nature-sounds/tropical-beach-audio/tropical-beach.mp3'
WOOD_MASTED_SAILBOAT_URL = 'http://meditationroom.org/free-nature-sounds/wood-masted-sailboat-audio/wood-masted-sailboat.mp3'
DAWN_CHORUS_URL = 'http://meditationroom.org/free-nature-sounds/dawn-chorus-audio/dawn-chorus.mp3'
URBAN_THUNDERSTORM_URL = 'http://meditationroom.org/free-nature-sounds/urban-thunderstorm-audio/urban-thunderstorm.mp3'
TROPICAL_STORM_URL = 'http://meditationroom.org/free-nature-sounds/tropical-storm-audio/tropical-storm.mp3'
RAINFOREST_URL = 'http://meditationroom.org/free-nature-sounds/rainforest-audio/rainforest.mp3'
OCEAN_WAVES_URL = 'http://meditationroom.org/free-nature-sounds/ocean-waves-audio/ocean-waves.mp3'


# The logic of each skill is contained within its own class, which inherits
# base methods from the MycroftSkill class with the syntax you can see below:
# "class ____Skill(MycroftSkill)"
class NatureSoundSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(NatureSoundSkill, self).__init__(name="NatureSoundSkill")
        self.audioservice = None

    def getPath(name):
        return (join(dirname(__file__), "mp3", name))
    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses
    def initialize(self):
        self.load_data_files(dirname(__file__))
        self.audioservice = None
        
        if AudioService:
            self.audioservice = AudioService(self.emitter)
        
        morning_intent = IntentBuilder("MorningSeaShoreIntent").\
                         require("PlayKeyword").\
                         require("MorningSeaShoreKeyword").build()
        self.register_intent(morning_intent, self.handle_morning_intent)
        
        forest_intent = IntentBuilder("ForestWalkIntent").\
                         require("PlayKeyword").\
                         require("ForestWalkKeyword").build()
        self.register_intent(forest_intent, self.handle_forest_intent)
        
        summer_intent = IntentBuilder("SummerRainIntent").\
                         require("PlayKeyword").\
                         require("SummerRainKeyword").build()
        self.register_intent(summer_intent, self.handle_summer_intent)
        
        mountain_intent = IntentBuilder("MountainStreamIntent").\
                         require("PlayKeyword").\
                         require("MountainStreamKeyword").build()
        self.register_intent(mountain_intent, self.handle_mountain_intent)
        
        beach_intent = IntentBuilder("BeachIntent").\
                         require("PlayKeyword").\
                         require("BeachKeyword").build()
        self.register_intent(beach_intent, self.handle_beach_intent)
        
        boat_intent = IntentBuilder("BoatIntent").\
                         require("PlayKeyword").\
                         require("BoatKeyword").build()
        self.register_intent(boat_intent, self.handle_boat_intent)
        
        dawn_intent = IntentBuilder("DawnIntent").\
                         require("PlayKeyword").\
                         require("DawnKeyword").build()
        self.register_intent(dawn_intent, self.handle_dawn_intent)
        
        thunderstorm_intent = IntentBuilder("ThunderstormIntent").\
                         require("PlayKeyword").\
                         require("ThunderstormKeyword").build()
        self.register_intent(thunderstorm_intent, self.handle_thunderstorm_intent)
        
        tropical_storm_intent = IntentBuilder("TropicalStormIntent").\
                         require("PlayKeyword").\
                         require("TropicalStormKeyword").build()
        self.register_intent(tropical_storm_intent, self.handle_tropical_storm_intent)
        
        ocean_intent = IntentBuilder("OceanIntent").\
                         require("PlayKeyword").\
                         require("OceanKeyword").build()
        self.register_intent(ocean_intent, self.handle_ocean_intent)
        
        rainforest_intent = IntentBuilder("RainforestIntent").\
                         require("PlayKeyword").\
                         require("RainforestKeyword").build()
        self.register_intent(rainforest_intent, self.handle_rainforest_intent)

    # The "handle_xxxx_intent" functions define Mycroft's behavior when
    # each of the skill's intents is triggered: in this case, he simply
    # speaks a response. Note that the "speak_dialog" method doesn't
    # actually speak the text it's passed--instead, that text is the filename
    # of a file in the dialog folder, and Mycroft speaks its contents when
    # the method is called.
    def handle_morning_intent(self, message):
        path = getPath("morning-seashore.mp3")
        if self.audioservice:
            self.audioservice.play(path, message.data['utterance'])
        else:
            self.process = play_mp3(path)
        self.speak_dialog("info",{"environment":"Morning Seashore"})
            
    def handle_forest_intent(self, message):
        path = getPath("forest-walk.mp3")
        if self.audioservice:
            self.audioservice.play(path, message.data['utterance'])
        else:
            self.process = play_mp3(path)
        self.speak_dialog("info",{"environment":"Forest"})

    def handle_summer_intent(self, message):
        path = getPath("summer-rain.mp3")
        if self.audioservice:
            self.audioservice.play(path, message.data['utterance'])
        else:
            self.process = play_mp3(path)
        self.speak_dialog("info",{"environment":"Summer rain"})

    def handle_mountain_intent(self, message):
        path = getPath("mountain-stream.mp3")
        if self.audioservice:
            self.audioservice.play(path, message.data['utterance'])
        else:
            self.process = play_mp3(path)
        self.speak_dialog("info",{"environment":"Mountain Stream"})
    
    def handle_beach_intent(self, message):
        path = getPath("tropical-beach.mp3")
        if self.audioservice:
            self.audioservice.play(path, message.data['utterance'])
        else:
            self.process = play_mp3(path)
        self.speak_dialog("info",{"environment":"Tropical Beach"})
    
    def handle_boat_intent(self, message):
        path = getPath("wood-masted-sailboat.mp3")
        if self.audioservice:
            self.audioservice.play(path, message.data['utterance'])
        else:
            self.process = play_mp3(path)
        self.speak_dialog("info",{"environment":"Wood masted sailboat"})

    def handle_dawn_intent(self, message):
        path = getPath("dawn-chorus.mp3")
        if self.audioservice:
            self.audioservice.play(path, message.data['utterance'])
        else:
            self.process = play_mp3(path)
        self.speak_dialog("info",{"environment":"Dawn chorus"})

    def handle_thunderstorm_intent(self, message):
        path = getPath("urban-thunderstorm.mp3")
        if self.audioservice:
            self.audioservice.play(path, message.data['utterance'])
        else:
            self.process = play_mp3(path)
        self.speak_dialog("info",{"environment":"Thunderstorm"})

    def handle_tropical_storm_intent(self, message):
        path = getPath("tropical-storm.mp3")
        if self.audioservice:
            self.audioservice.play(path, message.data['utterance'])
        else:
            self.process = play_mp3(path)
        self.speak_dialog("info",{"environment":"Tropical Storm"})

    def handle_rainforest_intent(self, message):
        path = getPath("rainforest.mp3")
        if self.audioservice:
            self.audioservice.play(path, message.data['utterance'])
        else:
            self.process = play_mp3(path)
        self.speak_dialog("info",{"environment":"Rainforest"})

    def handle_ocean_intent(self, message):
        path = self.getPath("ocean-waves.mp3")
        if self.audioservice:
            self.audioservice.play(path, message.data['utterance'])
        else:
            self.process = play_mp3(path)
        self.speak_dialog("info",{"environment":"Ocean waves"})
    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, the method just contains the keyword "pass", which
    # does nothing.
    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return NatureSoundSkill()
