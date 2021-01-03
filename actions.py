from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import division


from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class hotel(Action):
    def name(self):
        return "action_hotel"
    
    def run_br(self,dispatcher, tracker, domain):
        br=tracker.get_slot('book_room')
        res_br="Room Booked"
        dispatcher.utter_message(res_br)
        return[SlotSet('book_room',br)]
    
    def run_nor(self,dispatcher, tracker, domain,rooms):
        nor=tracker.get_slot('number_of_rooms')
        res_nor="You booked {} rooms".format(rooms)
        dispatcher.utter_message(res_nor)
        return[SlotSet('number_of_rooms',nor)]
    
    
    
    