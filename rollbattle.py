#!/usr/bin/env python3
# coding:utf8

import time
import random
import math

cheat_group = [407508177]
cached_players = {}
last_battle_day = time.localtime(time.time()).tm_yday
player_default = {'qq': 0, 'linked_qq': None,
                  'ban_minutes': 0, 'rp_val': 0,'last_roll':0}


def refresh():
    cached_players = {}
    last_fight_hour = time.localtime(time.time()).tm_hour
    last_battle_day = time.localtime(time.time()).tm_yday


def roll(challenger, against, request_time):
    day = time.localtime(time.time()).tm_yday
    random.seed(time.time() * 1337)
    if day != last_battle_day:
        refresh()
    challenger = int(challenger)
    against = int(against)
    request_time = int(request_time)
    p = cached_players.get(challenger)
    if p:
        challenger = p
    else:
        p = player_default.copy()
        p['qq'] = challenger
        cached_players.update({challenger: p})
        challenger = p
    p = cached_players.get(against)
    if p:
        p['ban_minutes'] = request_time
        against = p
    else:
        p = player_default.copy()
        p['qq'] = against
        p['ban_minutes'] = request_time
        cached_players.update({against: p})
        against = p

    p1roll = int(random.random() * 1337) % 100
    random.seed(p1roll * time.time())
    p2roll = int(random.random() * 1337) % 100
    # 根据rp修正结果
    for p in (challenger, against):
        v = p['rp_val']
        if v > 1000:
            p['rp_val'] = 1
        elif v < -500:
            p['rp_val'] = -1
    p1rp, p2rp = (p['rp_val'] for p in (challenger, against))
    if challenger['qq'] in cheat_group:  # 作弊buff
        p1rp += 200
    if against['qq'] in cheat_group:
        p2rp += 200
    # rp值最高提供1+1.2倍点数加成
    # 但也有可能是负的导致减益
    correction_ratio = p1rp * 1.2 / 1000.0
    p1roll *= 1 + correction_ratio
    correction_ratio = p2rp * 1.2 / 1000.0
    p2roll *= 1 + correction_ratio

    p1roll = math.floor(p1roll)
    p2roll = math.floor(p2roll)

    challenger['last_roll'] = p1roll
    against['last_roll'] = p2roll

    #//根据请求时间修正阈值
    #// 1min  -> 60%
    #// 5min  -> 40%
    #// y=-0.05x+0.65
    #// 10min -> 15%
    #// 10min > ? < 30min:
    #// y=1/x
    #// >30min=>impossible
    threshold = 0
    if request_time == 0:  # save
        threshold = 10
    elif request_time <= 10:
        threshold = 55 - 5 * request_time
    elif request_time > 10 and request_time <= 30:
        threshold = 100 / request_time
    threshold = 100 - threshold
    # 判断输赢
    result = {'threshold':threshold,'succeeded': [], 'challenger_ban_time': 0, 'against_ban_time': 0,'players':(challenger,against)}
    if request_time != 0:  # kill
        p1pass = bool(p1roll > threshold)
        p2pass = bool(p2roll > (100 - threshold))
        if request_time > 30:
            p2pass = bool(p2roll > 1)
            request_time = 5
        if p1pass:  # 挑战成功
            result['succeeded'].append(challenger['qq'])
            if p2pass:  # 同时成功，反噬
                result['succeeded'].append(against['qq'])
                t = math.ceil(request_time * 1.0 / 6.0)
                result['challenger_ban_time'] = t
                challenger['ban_minutes'] = t
                result['against_ban_time'] = request_time
                against['ban_minutes'] = request_time
                # 相互仇恨，下次一定要你死我活
                challenger['linked_qq'] = against['qq']
                against['linked_qq'] = challenger['qq']
                # 挑战成功rp一定会降的
                challenger['rp_val'] -= random.randint(1, 30)
            else:  # 完美成功
                result['challenger_ban_time'] = 0
                result['against_ban_time'] = request_time
                challenger['ban_minutes'] = 0
                challenger['linked_qq'] = None  # 杀成，不得复仇
                against['ban_minutes'] = request_time
                against['linked_qq'] = challenger['qq']  # 准备复仇
                challenger['rp_val'] -= random.randint(30, 100)  # 完美杀会急剧掉rp
                against['rp_val'] += random.randint(20, 50)  # 被杀，rp奖励
        else:  # 挑战失败
            if p2pass:  # 被反杀
                result['succeeded'].append(against['qq'])
                challenger['linked_qq'] = challenger['qq']  # 打不赢怨天尤人怼自己
                challenger['ban_minutes'] = request_time
                challenger['rp_val'] += random.randint(5, 50)
                against['rp_val'] -= random.randint(10, 30)  # 被挑战者波澜不惊
                result['challenger_ban_time'] = request_time
                result['against_ban_time'] = 0
            else:  # 菜鸡互啄相安无事
                result['challenger_ban_time'] = 0
                result['against_ban_time'] = 0
                # 继续互啄
                challenger['linked_qq'] = against['qq']
                against['linked_qq'] = challenger['qq']
                # 掐这个时间相互复仇
                challenger['ban_minutes'] = request_time
                against['ban_minutes'] = request_time
                # 大量rp，别丢人现眼
                challenger['rp_val'] += random.randint(50, 100)
                against['rp_val'] += random.randint(50, 100)

    else:  # 救，只对救人者判定
        against['linked_qq'] = None  # 被救失去复仇机会
        if p1roll >= threshold:  # 成功
            against['ban_minutes'] = 0  # 防止2次救误伤
            result['succeeded'].append(challenger['qq'])
            result['challenger_ban_time'] = 0
            result['against_ban_time'] = 0
            challenger['rp_val'] += random.randint(-50, 100)
        else:  # 失败
            # 失败也不加rp值
            result['against_ban_time'] = against['ban_minutes']
            t = math.ceil(against['ban_minutes'] / 2.5)
            # 连坐
            result['challenger_ban_time'] = t
            challenger['ban_minutes'] = t
            # 人心险恶，我救你，你害我，恼羞成怒
            challenger['linked_qq'] = against['qq']
    return result
