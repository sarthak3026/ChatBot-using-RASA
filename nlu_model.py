from rasa_nlu.model import Trainer
import rasa_nlu.config 
from rasa_nlu.training_data import load_data
from rasa_nlu.model import Metadata,Interpreter 
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu import config

def train_nlu_model(data,config,model_dir):
    training_data=load_data(data)
    trainer=Trainer(rasa_nlu.config.load(config))
    trainer.train(training_data)
    model_directory=trainer.persist(model_dir, fixed_model_name='hotelbot')
    
def run_model():
    inter=Interpreter.load('./models/nlu/default/hotelbot')
    print(inter.parse("Hi I want to book rooms"))
    
if __name__=="__main__":
    #train_nlu_model("./data/data.json","config.json",'./models/nlu')
    run_model()
    
