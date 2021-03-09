## happy path
* greet
  - utter_greet
  
## bible
* ask_chapter_bible
 - action_response_ask_bible

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy
## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy