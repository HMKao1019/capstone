# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:33:13 2022

@author: hmkao
"""

from linebot import LineBotApi
from linebot.models import TextSendMessage


#-- Link to the "Capstone_bot"

line_bot_api= LineBotApi('channel_access_token') #在 line_developer取得


"""
Push API:      發送 1：1 訊息（指定）。
Multicast API: 一次發送訊息給多個好友（指定）。
Broadcast API: 一次發送訊息給所有的好友。
"""

# In[] Push API

# Specify User ID
user_id= 'your user id'  #在 line_developer取得

# Push text you want
Push_api_str= 'This is a "Push API test" for the capstone course.'

# Push API command
line_bot_api.push_message(user_id, TextSendMessage(text= Push_api_str))

# In[] Broadcast API

# Broadcast text you want
Broadcast_api_str= 'This is a "Broadcast API test" for the capstone course.'

# Broadcast API command
#line_bot_api.broadcast(TextSendMessage(text= Broadcast_api_str))