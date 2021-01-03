# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 23:28:13 2020

@author: sarth
"""

from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.keras_policy import KerasPolicy
import logging
from rasa_core.agent import Agent

if __name__ == "__main__":
    logging.basicConfig(level="INFO")
    training_data_file="./data/stories.md"
    model_path="./models/dialogues"
    
    agent=Agent("hotel_domain.yml", policies=[MemoizationPolicy,KerasPolicy])
    
    agent.train(training_data_file,augmentation_factor=50, max_history=2,epochs=500,batch_size=10,validation_split=0.2)
    agent.persist(model_path)
