import logging, configparser
from flask_ask import Ask, request, session, question, statement

from web.flask import app
from .aliases import *
from flask import render_template

ask = Ask(app, "/ask")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['DEFAULT']['APIkey']

@ask.launch
def start_soccer_stat():
    welcome_msg = "this is a test message"
    return question(welcome_msg)

@ask.intent('LastMatchResultIntent')
def last_match_result(team):
    #TODO get actual data
    #TODO handle games determined by penalty kicks
    if team_score > opp_score:
        speech_text = render_template('last_result_win', team=team, team_score=team_score, opponent=opponent, opp_score=opp_score)
    elif opp_score > team_score:
        speech_text = render_template('last_result_loss', team=team, team_score=team_score, opponent=opponent, opp_score=opp_score)
    else opp_score == team_score:
        speech_text = render_template('last_result_draw', team=team, team_score=team_score, opponent=opponent, opp_score=opp_score)
    return statement(speech_text)


@ask.intent('CurrentMatchStatusIntent')
def current_match_score(team):
    #TODO: call api to get match score data, set score
    one_score="1"
    two_score="123"
    opp="bad guys"
<<<<<<< HEAD
    minute ="20"
    speech_text = render_template('current_status', team=team, team_score=one_score, opponent=opp, opp_score=two_score, minute = minute)
    return statement(speech_text)

@ask.intent('NextMatchTimeIntent')
def match_time(team)
    #TODO actually get the right data
    timestamp = "1234000000"

    speech_text = render_template('next_match_time', team=team, time=time)
    return statement(speech_text)
=======
    speech_text = render_template('score', team=team, team_score=one_score, opponent=opp, opp_score=two_score)
    return statement(speech_text).simple_card("Match Score", speech_text)
>>>>>>> d065e451f277722a22b3ae372fae018ae8b1d9da

@ask.intent('HelloWorldIntent')
def hello_world():
    speech_text = 'Hello world'
    return statement(speech_text).simple_card('HelloWorld', speech_text)

@ask.intent('HelpIntent')
def help():
    """Offer relevant help for HelpIntent
    """
    speech_text = 'You can say hello to me!'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)

@ask.intent('AliasIntent')
def alias_team(alias, team):
    """Add alias to alias database, called by Alexa

    Keyword arguments:
    alias, team
    """
    add = add_alias(alias, team)
    result = 'fail'
    if add == 1:
        result = 'success'
    elif add == 2:
        result = 'replace'
    elif add == 3:
        result = 'same'
    speech_text = render_template('alias_' + result, alias=alias, team=team)
    return statement(speech_text).simple_card("Alias", speech_text)

@ask.session_ended
def session_ended():
    return "{}", 200
