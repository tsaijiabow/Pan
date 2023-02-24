import discord
import os
import json
import keep_alive
from datetime import datetime
from discord.ext import commands
from random import choice, choices, randint, random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='=', intents=intents)

with open('setting.json', 'r', encoding='utf-8') as st:
  setjson = json.load(st)
with open('reply.json', 'r', encoding='utf-8') as rp:
  rmsg = json.load(rp)
with open('data.json', 'r' ,encoding='utf-8') as dj:
  data = json.load(dj)
  
@bot.event
async def on_ready():
  print("Pan#6699 已登入")
  status_w = discord.Status.online
  activity_w = discord.Activity(type=discord.ActivityType.playing,name="我的主人很懶...")
  await bot.change_presence(status=status_w, activity=activity_w)
  
ver = ('目前版本 1.10.02\n大更新！初步加入金錢系統')

@bot.event
async def on_message(ctx):
  if ctx.author == bot.user: #防止和其他機器人產生無限迴圈
    return
  else:
    msg = str(ctx.content) #訊息內容
    lst = msg.rsplit() #訊息長度(以空格做分隔)
    user = ctx.author.name #傳訊息的人
    x = len(lst)
    
    print (user +' ' + str(x))
    print (msg) #後台接收所有訊息

    x0 = str(lst[0])
    if x0 == 'P' or x0 == 'pan': #第0層 判斷是否在呼叫機器人

      x1 = str(lst[1]) #第1層 基本指令
      if x1 == 'ping': #測延遲
        await ctx.reply(f'{round(bot.latency*1000)}(ms)')

      elif x1 == 'say':
        lst.pop(1)
        lst.pop(0)
        say = str(lst[0])
        if x > 3:
          say = (' ').join(lst)
        await ctx.delete()
        await ctx.channel.send(user +'說：' + say)

      elif x1 == 'version': #查目前版本
        await ctx.reply(ver)

      elif x1 == 'luck': #抽籤
        rl = randint(50,55)
        await ctx.reply(rmsg[str(rl)])

      elif x1 == 'random': #隨機數字
        if x == 4: #判斷是否為兩個選項
          x2 = str(lst[2])
          x3 = str(lst[3])
          if x2.isdigit() == x3.isdigit() == True: #判斷兩個選項是否為數字
            rd = randint(int(x2),int(x3))
            await ctx.reply(rd)
          else:
            await ctx.reply('給我兩個「正整數」')
        else:
          await ctx.reply('給我「兩個」正整數')

      elif x1 == 'choose': #選擇
        if x > 3: #判斷選項數量是否足夠
          lst.pop(1)
          lst.pop(0)
          if lst[0] == lst[1]:
            await ctx.reply('為什麼讓我在同樣的選項裡選一個出來 是不是有病')
          else:
            rc = choice(lst)
            await ctx.reply(rc)
        else:
          await ctx.reply("這麼少選項我要選什麼")

      elif x1 == 'cal': #計算指令
        if x > 2:
          x2 = str(lst[2])
          if x2 == 'rank': #算單曲r值
            if x == 5:
              x3 = float(lst[3])
              x4 = float(lst[4])
              x3x4 = x3*x4
              if x3 >101:
                await ctx.reply('哇！恭喜 '+user+' 突破理論值 海放眾人！')
              elif x3 <= 101 and x3 >= 100.5:
                rank = 100.5*x4*22.4*0.01
                rank = round(rank,5)
                await ctx.reply('定數 '+str(x4)+' 的譜面打到 '+str(x3)+'% 的R值是 '+ str(rank))
              elif x3 < 100.5 and x3 >= 100:
                rank = x3x4*21.6*0.01
                rank = round(rank,5)
                await ctx.reply('定數 '+str(x4)+' 的譜面打到 '+str(x3)+'% 的R值是 '+ str(rank))
              elif x3 < 100 and x3 >= 99.5: 
                rank = x3x4*21.1*0.01
                rank = round(rank,5)
                await ctx.reply('定數 '+str(x4)+' 的譜面打到 '+str(x3)+'% 的R值是 '+ str(rank))
              elif x3 < 99.5 and x3 >= 99: 
                rank = x3x4*20.8*0.01
                rank = round(rank,5)
                await ctx.reply('定數 '+str(x4)+' 的譜面打到 '+str(x3)+'% 的R值是 '+ str(rank))
              elif x3 < 99 and x3 >= 98:
                rank = x3x4*20.3*0.01
                rank = round(rank,5)
                await ctx.reply('定數 '+str(x4)+' 的譜面打到 '+str(x3)+'% 的R值是 '+ str(rank))
              elif x3 < 98 and x3 >= 97:
                rank = x3x4*20*0.01
                rank = round(rank,5)
                await ctx.reply('定數 '+str(x4)+' 的譜面打到 '+str(x3)+'% 的R值是 '+ str(rank))
              elif x3 < 97 and x3 >= 94:
                rank = x3x4*16.8*0.01
                rank = round(rank,5)
                await ctx.reply('定數 '+str(x4)+' 的譜面打到 '+str(x3)+'% 的R值是 '+ str(rank))
              elif x3 < 94 and x3 >= 90:
                rank = x3x4*15.2*0.01
                rank = round(rank,5)
                await ctx.reply('定數 '+str(x4)+' 的譜面打到 '+str(x3)+'% 的R值是 '+ str(rank))
              elif x3 < 80 and x3 >= 90:
                rank = x3x4*13.6*0.01
                rank = round(rank,5)
                await ctx.reply('定數 '+str(x4)+' 的譜面打到 '+str(x3)+'% 的R值是 '+ str(rank))
              else:
                await ctx.reply('分數太低了！廢物！')
            else:
              await ctx.reply('給我分數跟定數')
          else:
            await ctx.reply('你要算什麼')
        else:
          await ctx.reply('你要算什麼')

      elif x1 == 'register': #新用戶登記
        with open('data.json', 'r', encoding='utf-8') as dj:
          data = json.load(dj)
        if data.get(user,'a') == 'a': #偵測是否為新用戶
          with open('data.json', 'w', encoding='utf-8') as dj:
            data[user] = 1000
            json.dump(data ,dj ,ensure_ascii=False)
            await ctx.reply('用戶名稱：'+user+'\n註冊成功！獲得$1000')
        else:            
          await ctx.reply('用戶名稱：'+user+'\n已註冊')

      elif x1 == 'me':
        with open('data.json', 'r', encoding='utf-8') as dj:
          data = json.load(dj)
        if data.get(user,'a') == 'a':
          await ctx.reply('新用戶請先使用register指令註冊')
        else:
          money = data[user]
          await ctx.reply(user+' 目前資產是 $'+ str(money))

      elif x1 == 'get':
        with open('data.json', 'r', encoding='utf-8') as dj:
          data = json.load(dj)
        if data.get(user,'a') == 'a':
          await ctx.reply('新用戶請先使用register指令註冊')
        else:
          get = randint(1,100)
          with open('data.json', 'w', encoding='utf-8') as dj:
            money = data[user]
            data[user] = money + get
            json.dump(data ,dj ,ensure_ascii=False)
          await ctx.reply(user+'做為廉價勞工賺取了$'+ str(get))
        
      else:
        rm = randint(1,30) #隨機抽一條回覆
        await ctx.reply(rmsg[str(rm)])

keep_alive.keep_alive()
bot.run(setjson["token"])
