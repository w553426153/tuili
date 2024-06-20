import requests
import json
from agentscope.message import Msg
from format_wang import format_wang

def condition(i,x):

    try:
        x_xuqiu = format_wang(x)
    except:
        x_xuqiu = None

    if x_xuqiu==None:
        # print(x_xuqiu)
        return True
    else:
        return False


# if __name__ == '__main__':
# #     x= {
# #         "results":[{
# #          "意图":"对流浪狗的关注",
# #          "想让我干什么":"我还不清晰，可能需要我观察、安慰他，或者提供一些帮助方案",
# #          "背景":"用户在路上遇到了一只流浪狂",
# #          "意图达成的好处":"可能会帮助这只流浪狗得到更好的待遇，同时也让用户感到满足",
# #          "意图未达成的坏处":"流浪狗可能需要向食物、住所，可能会生病，用户可能会感到有些难过",
# #          "意图的需求层次":"这属于马斯洛的贡献需求，想要帮助别人。",
# #          "下一个问题":"你遇到这只流浪狗想要做些什么呢？"
# # }
# # ]
# #     }
# #     x=Msg(name="test",content=x)
# #     x_xuqiu = x['content']['results'][0]['意图']
# #     i=1
#     x={'id': '11296e28917a492db925bd788cdc0d1c', 'timestamp': '2024-06-18 13:29:32', 'name': 'assistant', 'content': '您好! 请问有什么我可以帮助您的事吗？', 'role': 'assistant', 'url': None, 'metadata': None}
#     x=x['content']
#     print(x)
#     # print(condition(i,x))
