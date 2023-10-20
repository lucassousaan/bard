from bardapi import Bard
from dotenv import load_dotenv
load_dotenv()
 
def call_bard(query):
   bard = Bard(token="ACA-OxMiPJbJm-RjrdZJ2y9B2RBQLO3ebEPpSTjZTQ6pWo-4AdqQ4w2xbEdLd3m_Seyw0BTdoflp")
   answer = bard.get_answer(query)
   return (answer['content'])

response = call_bard("What movie would you recommend?")

