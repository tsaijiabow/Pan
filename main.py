import discord
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
with open('data.json', 'r', encoding='utf-8') as dj:
  data = json.load(dj)


@bot.event
async def on_ready():
  print("Pan#6699 已登入")
  status_w = discord.Status.online
  activity_w = discord.Activity(type=discord.ActivityType.playing,
                                name="我的主人很懶...")
  await bot.change_presence(status=status_w, activity=activity_w)


err = ('語法錯誤')
ver = ('目前版本 1.16.15\n大幅度精簡程式碼\n新增功能：輪盤')


@bot.event
async def on_message(ctx):
  if ctx.author == bot.user:  #防止和其他機器人產生無限迴圈
    return
  else:
    msg = str(ctx.content)  #訊息內容
    lst = msg.rsplit()  #訊息長度(以空格做分隔)
    user = ctx.author.name  #傳訊息的人
    userid = str(ctx.author.id) #每個人的ID
    x = len(lst)
    print(user + '\n' + str(userid) + ' ' + str(x) + '\n' + msg)  #後台接收所有訊息
    x0 = str(lst[0])
    if x0 == 'P' or x0 == 'Pan' or x0 == 'pan':  #第0層 判斷是否在呼叫機器人

      x1 = str(lst[1])  #第1層 基本指令
      if x1 == 'ping':  #測延遲
        await ctx.reply(f'{round(bot.latency*1000)}(ms)')

      elif x1 == 'help':
        embed = discord.Embed(title="功能列表", color=0x969632)
        embed.set_thumbnail(url= "https://static.wikia.nocookie.net/maimai/images/0/03/201905104_mms_pandoraparadoxxx.png/revision/latest?cb=20190524085927&path-prefix=zh")
        embed.add_field(name="選擇", value="P choose+兩個或多個選項", inline=False)
        embed.add_field(name="抽籤", value="P luck", inline=False)
        embed.add_field(name="隨機數字", value="P random+兩個整數", inline=False)
        embed.add_field(name="算單曲R值(maimai)", value="P cal rank+分數+定數", inline=False)
        embed.add_field(name="賭博系統 註冊", value="P register", inline=False)
        embed.add_field(name="刪除資料", value="P delete", inline=False)
        embed.add_field(name="查資產", value="P me", inline=False)
        embed.add_field(name="查排行榜", value="P ranking", inline=False)
        embed.add_field(name="賭大小 下注", value="P bet+金額+大or小", inline=False)
        embed.add_field(name="輪盤 下注", value="P roulette+金額", inline=False)
        embed.add_field(name="工作賺錢", value="P get", inline=False)
        embed.add_field(name="轉帳", value="P transfer+金額+人名", inline=False)
        embed.add_field(name="其他隨機的回答", value="P+任意文字", inline=False)
        embed.set_footer(text=ver + "\n目前還在測試階段 有bug請多見諒")
        await ctx.channel.send(embed=embed)

      elif x1 == 'say':
        lst.pop(1)
        lst.pop(0)
        say = str(lst[0])
        if x > 3:
          say = (' ').join(lst)
        await ctx.delete()
        await ctx.channel.send(say)

      elif x1 == 'version':  #查目前版本
        await ctx.reply(ver)

      elif x1 == 'luck':  #抽籤
        rl = randint(50, 55)
        await ctx.reply(rmsg[str(rl)])

      elif x1 == 'random':  #隨機數字
        if x == 4:  #判斷是否為兩個選項
          x2 = str(lst[2])
          x3 = str(lst[3])
          try:  #排除例外
            rd = randint(int(x2), int(x3))
            await ctx.reply(rd)
          except Exception:
            await ctx.reply('給我兩個數字')
        else:
          await ctx.reply('給我兩個數字')

      elif x1 == 'choose':  #選擇
        if x > 3:  #判斷選項數量是否足夠
          lst.pop(1)
          lst.pop(0)
          if lst[0] == lst[1]:
            await ctx.reply('為什麼讓我在同樣的選項裡選一個出來 是不是有病')
          else:
            rc = choice(lst)
            await ctx.reply(rc)
        else:
          await ctx.reply("這麼少選項我要選什麼")

      elif x1 == 'cal':  #計算指令
        if x > 2:
          x2 = str(lst[2])
          ops = {'+': lambda a, b: a+b,
                '-': lambda a, b: a-b,
                '*': lambda a, b: a*b,
                '/': lambda a, b: a/b,
                '×': lambda a, b: a*b,
                '÷': lambda a, b: a/b}

          if x2 in ops:
            if x == 5:
              try:
                lst.pop(2)
                lst.pop(1)
                lst.pop(0)
                result = ops[x2](float(lst[0]), float(lst[1]))
                result = round(result, 10)
                await ctx.reply(str(result))
              except Exception:
                await ctx.reply('給我兩個數字')
            else:
              await ctx.reply('給我兩個數字')

          elif x2 == 'rank':  #算單曲r值
            if x == 5:
              x3 = float(lst[3])
              x4 = float(lst[4])
              x3x4 = x3 * x4
              if x3 > 101:
                await ctx.reply('哇！恭喜 ' + user + ' 突破理論值 海放眾人！')
              else:
                ranks = {
                  (100.5, None): 22.4,
                  (100, 100.5): 21.6,
                  (99.5, 100): 21.1,
                  (99, 99.5): 20.8,
                  (98, 99): 20.3,
                  (97, 98): 20.0,
                  (94, 97): 16.8,
                  (90, 94): 15.2,
                  (80, 90): 13.6}
                
                for (range, value) in ranks.items():
                  if range[0] <= x3 < range[1]:
                    rank = x3x4 * value * 0.01
                    rank = round(rank, 5)
                    await ctx.reply('定數 ' + str(x4) + ' 的譜面打到 ' + str(x3) + '% 的R值是 ' + str(rank))
                    break
                else:
                  await ctx.reply('分數太低了！廢物！')
            else:
              await ctx.reply('給我分數跟定數')
          else:
            await ctx.reply('你要算什麼')
        else:
          await ctx.reply('你要算什麼')

      elif x1 == 'register':  #新用戶登記
        with open('data.json', 'r', encoding='utf-8') as dj:
          data = json.load(dj)
        if data.get(userid) is None: #偵測是否為新用戶
          with open('data.json', 'w', encoding='utf-8') as dj:
            data[userid] = {"money":100, "name":user}
            json.dump(data, dj, ensure_ascii=False)
            dj.close()
          await ctx.reply('用戶名稱：<@' + userid + '>\n註冊成功！獲得$100')
        else:
          await ctx.reply('用戶名稱：<@' + userid + '>\n已註冊')

      elif x1 == 'me':  #查資產
        with open('data.json', 'r', encoding='utf-8') as dj:
          data = json.load(dj)
        if data.get(userid) is None:
          await ctx.reply('新用戶請先使用register指令註冊')
        elif x > 2:
          x2 = str(lst[2]).strip('@<>')
          if data.get(x2) is None:
            await ctx.reply('沒有此註冊資料')
          else:
            money = data[x2]["money"]
            l = len(str(money))
            await ctx.reply('<@' + x2 + '> 目前資產是 $' + str(money) + '\n' +
                            str(l) + '位數')
        else:
          money = data[userid]["money"]
          l = len(str(money))
          await ctx.reply('<@' + userid + '> 目前資產是 $' + str(money) + '\n' +
                          str(l) + '位數')

      elif x1 == 'delete':  #刪除資料
        with open('data.json', 'r', encoding='utf-8') as dj:
          data = json.load(dj)
          if data.get(userid) is None:
            await ctx.reply('沒有此註冊資料')
          else:
            with open('data.json', 'w', encoding='utf-8') as dj:
              p = data.pop(userid, 'a')
              json.dump(data, dj, ensure_ascii=False)
              dj.close()
            await ctx.reply('資料刪除成功')

      elif x1 == 'ranking':  #排行榜
        with open('data.json', 'r', encoding='utf-8') as dj:
          data = json.load(dj)
          v = list(data.values()) #每個人各自的資料
          k = list(data.keys()) #每個人各自的ID
          lk = len(k)
          vm = {}
          vn = {}
          embed = discord.Embed(title="資產排行榜", color=0x969632)
          for i in range(lk):
            vm.update({v[i]["money"]:k[i]})
            vn.update({k[i]:v[i]["name"]})
          s = sorted(vm, reverse=True)
          if len(k) < 10:
            for i in range(lk):
              embed.add_field(name='第' + str(i + 1) + '名：' +str(vn[vm[s[i]]]), value='$' + str(s[i]), inline=False)
          else:
            n = 10
            for i in range(n):
              embed.add_field(name='第' + str(i + 1) + '名：' +str(vn[vm[s[i]]]), value='$' + str(s[i]), inline=False)
          await ctx.channel.send(embed=embed)

      elif x1 == 'get':  #工作
        with open('data.json', 'r', encoding='utf-8') as dj:
          data = json.load(dj)
        if data.get(userid) is None:
          await ctx.reply('新用戶請先使用register指令註冊')
        else:
          with open('data.json', 'w', encoding='utf-8') as dj:
            money = data[userid]["money"]
            if money < 0: #如果資產為負數
              data[userid]["money"] = 0
              json.dump(data, dj, ensure_ascii=False)
              dj.close()
              await ctx.reply('原資產為負數 已歸零\n目前資產： $' + str(data[userid]["money"]))
            elif money == 0: #如果破產了
              data[userid]["money"] += 100
              json.dump(data, dj, ensure_ascii=False)
              dj.close()
              await ctx.reply('哇！一百塊從天上掉下來了！\n請務必振作起來\n目前資產： $' + str(data[userid]["money"]))
            else:
              if money < 1000:
                g = randint(1, 100)
                data[userid]["money"] += g
                msg = '以廉價苦力勞工的身分賺取了 $'+ str(g)
              elif money < 1000000:
                g = randint(1, 100000)
                data[userid]["money"] += g
                msg = '以一般員工的身分賺取了 $'+ str(g)
              elif money < 1000000000:
                g = randint(1, 100000000)
                data[userid]["money"] += g
                msg = '以高薪員工的身分賺取了 $'+ str(g)
              elif money < 1000000000000:
                g = randint(1, 100000000000)
                data[userid]["money"] += g
                msg = '以老闆的身分賺取了 $'+ str(g)
              else:
                msg = '你已經財富自由了！還賺什麼！'
            json.dump(data, dj, ensure_ascii=False)
            msg2 = '\n目前資產： $' + str(data[userid]["money"])
            await ctx.reply(msg + msg2)
            dj.close()  #關閉檔案

      elif x1 == 'roulette': #輪盤
        with open('data.json', 'r', encoding='utf-8') as dj:
          data = json.load(dj)
        if data.get(userid) is None:
          await ctx.reply('新用戶請先使用register指令註冊')
        else:
          if x < 3:
            await ctx.reply('請輸入賭注')
          else:
            x2 = str(lst[2])
            money = int(data[userid]["money"])
            r = str(randint(70, 77))
            word = rmsg[r]["word"]
            num = rmsg[r]["num"]
            text = '8.0 0.0 0.2\n5.0 '+word+'  0.5\n3.0 2.0 0.8'
            try:
              if x2 == 'all':
                before = str(money)
                money = round(int(money) * float(num))
                data[userid]["money"] = money
                with open('data.json', 'w', encoding='utf-8') as dj:
                  json.dump(data, dj, ensure_ascii=False)
                  dj.close()
                await ctx.reply(text +'\n'+ before +'×'+ str(num) +'='+ str(money) +'\n目前資產： $'+ str(data[userid]["money"]))
              elif int(x2) > 0 and int(x2) <= money:
                win = round(int(x2) * float(num))
                money = money - int(x2)
                with open('data.json', 'w', encoding='utf-8') as dj:
                  data[userid]["money"] = money + win
                  json.dump(data, dj, ensure_ascii=False)
                  dj.close()
                await ctx.reply(text +'\n'+ x2 +'×'+ str(num) +'='+ str(win) +'\n目前資產： $'+ str(data[userid]["money"]))
              else:
                await ctx.reply('你不能賭這個金額')
            except Exception:
              await ctx.reply(err)

          
      elif x1 == 'transfer':  #轉帳
        with open('data.json', 'r', encoding='utf-8') as dj:
          data = json.load(dj)
        if data.get(userid) is None:
          await ctx.reply('新用戶請先使用register指令註冊')
        else:
          if x != 4:  #判斷指令格式是否正確
            await ctx.reply('格式不對\n請輸入金額 + 人名')
          else:
            x2 = str(lst[2])
            x3 = str(lst[3]).strip('@<>')
            if data.get(x3) is None:
              await ctx.reply('沒有此註冊資料')
            else:
              try:
                money = data[userid]["money"]
                tran = data[x3]["money"]
                c = round(int(x2) / 100)
                if money >= (int(x2) + c) and int(x2) > 0:
                  with open('data.json', 'w', encoding='utf-8') as dj:
                    data[x3]["money"] = tran + int(x2)
                    data[userid]["money"] = money - round(int(x2) + c)
                    jiabow = data["821894064194453554"]["money"]
                    data["821894064194453554"]["money"] = jiabow + c
                    json.dump(data, dj, ensure_ascii=False)
                    dj.close()
                    await ctx.reply('轉帳成功！<@' + x3 + '>收到了 $' + str(x2) + '\n<@821894064194453554>收到了手續費 $' + str(c) + '\n實際扣款： $' + str(int(x2) + c) + '\n目前資產： $' + str(data[userid]["money"]))
                else:
                  await ctx.reply('你不能轉這個金額')
              except Exception:
                await ctx.reply(err)

      elif x1 == 'bet':  #賭大小
        with open('data.json', 'r', encoding='utf-8') as dj:
          data = json.load(dj)
        if data.get(userid) is None:
          await ctx.reply('新用戶請先使用register指令註冊')
        else:
          if x != 4:  #判斷指令格式是否正確
            await ctx.reply('格式不對\n請輸入金額 + 大/小')
          else:
            bigbool = randint(0, 1)
            money = data[userid]["money"]
            x2, x3 = str(lst[2]), str(lst[3])
            lst.pop(0), lst.pop(0)
            if x3 in ['big', '大', 'small', '小']:
              if x2 == 'all':
                x2 = str(money)
              if int(x2) <= 0 or int(x2) > money:
                await ctx.reply('你不能賭這個金額')
              else:
                if (x3 in ['big', '大'] and bigbool == 1) or (x3 in ['small', '小'] and bigbool == 0):
                  data[userid]["money"] += int(x2)
                  with open('data.json', 'w', encoding='utf-8') as dj:
                    json.dump(data, dj, ensure_ascii=False)
                    dj.close()
                  await ctx.reply('本局結果：' + x3 + '\n<@' + userid + '> 贏得了 $' + str(x2) + '\n目前資產： $' + str(data[userid]["money"]))
                else:
                  data[userid]["money"] -= int(x2)
                  with open('data.json', 'w', encoding='utf-8') as dj:
                    json.dump(data, dj, ensure_ascii=False)
                    dj.close()
                  await ctx.reply('本局結果：' + x3 + '\n<@' + userid + '> 輸掉了 $' + str(x2) + '\n目前資產： $' + str(data[userid]["money"]))
            else:
              await ctx.reply('格式不對\n請輸入金額 + 大/小')

      else:
        rm = randint(1, 30)  #隨機抽一條回覆
        await ctx.reply(rmsg[str(rm)])

keep_alive.keep_alive()
bot.run(setjson["token"])
