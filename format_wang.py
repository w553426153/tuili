import json
import re
from agentscope.message import Msg

def format_wang(x):
    x=x.content
    cleaned_content = re.sub(r'\s+', '', x)
    cleaned_content = json.loads(cleaned_content)
    yitu = cleaned_content['results'][0]['意图']

    return yitu


