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

bot = commands.Bot(command_prefix='', intents=intents)
with open('setting.json', 'r', encoding='utf-8') as tk:
  token = json.load(tk)

rmsg = [
     '說了就是有'
    ,'絕對是的'
    ,'沒可能'
    ,'你媽媽表現此次'
    ,'我現在不想理你'
    ,'操你媽'
    ,'一定可以的 對吧'
    ,'？？？'
    ,'割'
    ,'欸'
    ,'對'
    ,'好'
    ,'100%表示認同'
    ,'完全正確'
    ,'Yes'
    ,'Fuck you'
    ,'我表示非常認同'
    ,'你在想什麼'
    ,'我不知道'
    ,'無法理解'
    ,'衝三小'
    ,'當然'
    ,'是喔'
    ,'沒錯'
    ,'救命'
    ,'笑死'
    ,'確實'
    ,'答錯了'
    ,'嗯嗯嗯嗯是是是你說的都對'
    ,'有時間在這裡講幹話還不如去打手槍'] #30個隨機回答
luck = [
       '大吉 去買個樂透看看'
      ,'中吉 可能會有意料外的小驚喜'
      ,'小吉 今天非常適合刷分 ~~不是曉極~~'
      ,'普通 就跟平常一樣 普通的一天'
      ,'小凶 感覺會有點不太順利'
      ,'大凶 唉沒救了 準備等死吧'
]

@bot.event
async def on_ready():
  print("Pan#6699 已登入")
  status_w = discord.Status.online
  activity_w = discord.Activity(type=discord.ActivityType.playing,name="我的主人很懶...")
  await bot.change_presence(status=status_w, activity=activity_w)

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

      elif x1 == 'version': #查目前版本
        ver = ('目前版本 1.04' + '\n' +'增加功能：查單曲R值')
        await ctx.reply(ver)

      elif x1 == 'luck': #測運氣
        rl = choice(luck) 
        await ctx.reply(rl)

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
              x3x4 = x3*(x4)
              if x3 >= 100.5:
                rank = 100.5*x4*22.4*0.01
                await ctx.reply('定數 '+str(x4)+' 的譜面打到 '+str(x3)+'% 的R值是 '+ str(rank))
              elif x3 < 100.5 and x3 >= 100:
                rank = x3x4*21.6*0.01
                await ctx.reply('定數 '+str(x4)+' 的譜面打到 '+str(x3)+'% 的R值是 '+ str(rank))
              elif x3 < 100 and x3 >= 99.5: 
                rank = x3x4*21.1*0.01
                await ctx.reply('定數 '+str(x4)+' 的譜面打到 '+str(x3)+'% 的R值是 '+ str(rank))
              elif x3 < 99.5 and x3 >= 99: 
                rank = x3x4*20.8*0.01
                await ctx.reply('定數 '+str(x4)+' 的譜面打到 '+str(x3)+'% 的R值是 '+ str(rank))
              elif x3 < 99 and x3 >= 98:
                rank = x3x4*20.3*0.01
                await ctx.reply('定數 '+str(x4)+' 的譜面打到 '+str(x3)+'% 的R值是 '+ str(rank))
              elif x3 < 98 and x3 >= 97:
                rank = x3x4*20*0.01
                await ctx.reply('定數 '+str(x4)+' 的譜面打到 '+str(x3)+'% 的R值是 '+ str(rank))
              elif x3 < 97 and x3 >= 94:
                rank = x3x4*16.8*0.01
                await ctx.reply('定數 '+str(x4)+' 的譜面打到 '+str(x3)+'% 的R值是 '+ str(rank))
              elif x3 < 94 and x3 >= 90:
                rank = x3x4*15.2*0.01
                await ctx.reply('定數 '+str(x4)+' 的譜面打到 '+str(x3)+'% 的R值是 '+ str(rank))
              elif x3 < 80 and x3 >= 90:
                rank = x3x4*13.6*0.01
                await ctx.reply('定數 '+str(x4)+' 的譜面打到 '+str(x3)+'% 的R值是 '+ str(rank))
              else:
                await ctx.reply('分數太低了！廢物！')
            else:
              await ctx.reply('無法計算 你行你上')
          else:
            await ctx.reply('你要算什麼')
        else:
          await ctx.reply('你要算什麼')

          
      else:
        rm = choice(rmsg) #隨機抽一條回覆
        await ctx.reply(rm)

keep_alive.keep_alive()
bot.run(token["token"])
