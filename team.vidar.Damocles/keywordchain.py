#!/usr/bin/env python2
# -*- coding:gbk -*-
# this file will be run on windows, please save as gbk encoding

import traceback
import functools

# ########  KEY CHAINS STRUCTURE:
# #####     chains: [chain1,chain2,...]
# ####      layers: {l1:(l1_linked1,l1_linked2,...),l2:(l2_linked,),...} in chain
# ###       keywords: (keyword1,keyword2,...) in layer
# ##        FULL: [chain1{l1:(c1l2,c2l2,c3l3,...),l2:(c1l3,)},chain2{...}]
# #         _trigger: triggers when existing ...
# #         _head: keyword chain begins with ...
# #         _silence: do nothing when existing ...
# #         kw_xxx : (trigger,head,chains,silence)


# isa
kw_isa_chain1_l1 = (u'信安', u'网安', u'信息安全',
                    u'网络安全', u'vidar')
kw_isa_chain1_l2 = (u'协会', u'安协', u'实验室')
kw_isa_chain1_l3 = (u'哪', u'位置', u'怎么走',
                    u'地址', u'怎么去', u'咋去')
kw_isa_trigger = kw_isa_chain1_l3
kw_isa_silence = tuple()
kw_isa_head = kw_isa_chain1_l1 + kw_isa_chain1_l2
kw_isa_chain1 = {kw_isa_chain1_l1: (
    kw_isa_chain1_l2,), kw_isa_chain1_l2: (kw_isa_chain1_l3,)}
kw_chains_isa = [kw_isa_chain1]
kw_isa = (kw_isa_trigger, kw_isa_head, kw_chains_isa, kw_isa_silence)


# learn
kw_learn_chain1_l1 = (u'c', u'c语言', u'编程')
kw_learn_chain2_l1 = (u'黑客', u'信息安全', u'安全', u'信安')
kw_learn_chain3_l1 = ('看', '读', '用', '推荐')

kw_learn_chain1_l2 = (u'怎么', u'如何', u'怎样', u'咋')
kw_learn_chain2_l2 = (u'有没有', u'哪些', u'什么', u'有关', u'啥')
kw_learn_chain3_l2 = ('想', '教', '要')

kw_learn_chain1_l3 = (u'入门', u'学', u'开始')
kw_learn_chain2_l3 = (u'书', u'教材', u'资料', u'方法')
kw_learn_chain3_l3 = (u'我', u'当', u'做', u'成为', u'搞')
kw_learn_trigger = kw_learn_chain1_l1 + kw_learn_chain2_l1 + \
    kw_learn_chain2_l2 + kw_learn_chain1_l3 + kw_learn_chain2_l3
kw_learn_silence = (u'不', u'拒绝', u'禁', u'别')
kw_learn_head = kw_learn_chain1_l1 + kw_learn_chain2_l1 + kw_learn_chain3_l1

kw_learn_chain1 = {kw_learn_chain1_l1: (kw_learn_chain1_l2, kw_learn_chain2_l2), kw_learn_chain1_l2: (
    kw_learn_chain1_l3,), kw_learn_chain2_l2: (kw_learn_chain2_l3,)}
kw_learn_chain2 = {kw_learn_chain2_l1: (kw_learn_chain1_l2, kw_learn_chain3_l2), kw_learn_chain1_l2: (
    kw_learn_chain1_l3,), kw_learn_chain3_l2: (kw_learn_chain3_l3,)}
kw_learn_chain3 = {kw_learn_chain3_l1: (kw_learn_chain2_l2,), kw_learn_chain2_l2: (
    kw_learn_chain1_l3, kw_learn_chain2_l3)}
kw_chains_learn = [kw_learn_chain1, kw_learn_chain2, kw_learn_chain3]
kw_learn = (kw_learn_trigger, kw_learn_head, kw_chains_learn, kw_learn_silence)


# hack
kw_hack_chain1_l1 = (u'日', u'黑', u'拿', u'入侵', u'攻击', u'扫')
kw_hack_chain2_l1 = (u'拖', u'扫')
kw_hack_chain3_l1 = (u'盗',)
kw_hack_chain4_l1 = (u'刷',)
kw_hack_chain5_l1 = (u'制作', u'写', u'做')

kw_hack_chain1_l2 = (u'站', u'杭电', u'学校', u'官网',
                     u'hdu', u'论坛', u'电脑', u'服务器')
kw_hack_chain2_l2 = (u'库', u'数据', u'资料')
kw_hack_chain3_l2 = (u'q', u'号')
kw_hack_chain4_l2 = (u'会员', u'钻')
kw_hack_chain5_l2 = (u'挂',)
kw_hack_trigger = kw_hack_chain1_l2 + kw_hack_chain2_l2 + \
    kw_hack_chain3_l2 + kw_hack_chain4_l2 + kw_hack_chain5_l2 + kw_hack_chain1_l1
kw_hack_silence = (u'禁', u'别', u'不能', u'不要',
                   u'拒绝', u'low', u'脚本小子', u'法', u'罪')
kw_hack_head = kw_hack_chain1_l1 + kw_hack_chain2_l1 + \
    kw_hack_chain3_l1 + kw_hack_chain4_l1 + kw_hack_chain5_l1

kw_hack_chain1 = {kw_hack_chain1_l1: (kw_hack_chain1_l2,)}
kw_hack_chain2 = {kw_hack_chain2_l1: (kw_hack_chain2_l2,)}
kw_hack_chain3 = {kw_hack_chain3_l1: (kw_hack_chain3_l2,)}
kw_hack_chain4 = {kw_hack_chain4_l1: (kw_hack_chain4_l2,)}
kw_hack_chain5 = {kw_hack_chain5_l1: (kw_hack_chain5_l2,)}
kw_chains_hack = [kw_hack_chain1, kw_hack_chain2,
                  kw_hack_chain3, kw_hack_chain4, kw_hack_chain5]
kw_hack = (kw_hack_trigger, kw_hack_head, kw_chains_hack, kw_hack_silence)


# reg
kw_reg_chain1_l1 = (u'招新', u'报名', u'注册', u'加入')
kw_reg_chain1_l2 = (u'怎么', u'哪',u'在')
kw_reg_chain2_l2 = (u'有', u'坏', u'开')
kw_reg_chain2_l3 = (u'地址', u'线',u'吗')
kw_reg_trigger = kw_reg_chain1_l1
kw_reg_silence = (u'还', u'已经', u'好了', u'过', u'的话',u'为什么',u'为啥',u'早')
kw_reg_head = kw_reg_chain1_l1

kw_reg_chain1 = {kw_reg_chain1_l1: (
    kw_reg_chain1_l2, kw_reg_chain2_l2, kw_reg_chain2_l3), kw_reg_chain2_l2: (kw_reg_chain2_l3,)}
kw_chains_reg = [kw_reg_chain1]
kw_reg = (kw_reg_trigger, kw_reg_head, kw_chains_reg, kw_reg_silence)


# dress
kw_dress_chain1_l1 = (u'女装', u'rbq')
kw_dress_chain1_l2 = (u'有', u'给', u'去', u'穿', u'买', u'奖')
kw_dress_chain1_l3 = (u'群主', u'管理员', u'你', u'大佬', u'dalao')

kw_dress_trigger = kw_dress_chain1_l1
kw_dress_silence = (u'我',)
kw_dress_head = kw_dress_chain1_l1 + kw_dress_chain1_l2
kw_chains_dress = [{kw_dress_chain1_l1: (kw_dress_chain1_l2, kw_dress_chain1_l3), kw_dress_chain1_l2: (
    kw_dress_chain1_l3,), kw_dress_chain1_l3: (kw_dress_chain1_l1, kw_dress_chain1_l2)}]
kw_dress = (kw_dress_trigger, kw_dress_head, kw_chains_dress, kw_dress_silence)


# there is person on duty
kw_duty_chain1_l1 = kw_isa_chain1_l2  # = ('协会', '安协', '实验室')
kw_duty_chain1_l1 += (u'111', u'613', u'3楼')
kw_duty_chain1_l2 = (u'有', u'在', u'值班')
kw_duty_chain1_l3 = (u'人', u'学长', u'姐', u'大佬', u'dalao', u'谁')
kw_duty_trigger = kw_duty_chain1_l1
kw_duty_head = kw_duty_chain1_l1
kw_duty_silence = (u'不', u'没', u'走了')
kw_chains_duty = [{kw_duty_chain1_l1: (
    kw_duty_chain1_l2,), kw_duty_chain1_l2: (kw_duty_chain1_l3,)}]
kw_duty = (kw_duty_trigger, kw_duty_head, kw_chains_duty, kw_duty_silence)

# ##
# ###
# ####
# ######   DONT FORMAT THIS AREA


def noexcept(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            traceback.print_exc()
            return False
    return wrapped


class KeywordChain(object):
    def __init__(self, kwtype):
        if kwtype not in ('reg', 'hack', 'learn', 'isa', 'dress', 'duty'):
            raise Exception
        if kwtype == 'reg':
            self.__trigger, self.__head, self.__chains, self.__silence = kw_reg
        elif kwtype == 'hack':
            self.__trigger, self.__head, self.__chains, self.__silence = kw_hack
        elif kwtype == 'learn':
            self.__trigger, self.__head, self.__chains, self.__silence = kw_learn
        elif kwtype == 'isa':
            self.__trigger, self.__head, self.__chains, self.__silence = kw_isa
        elif kwtype == 'dress':
            self.__trigger, self.__head, self.__chains, self.__silence = kw_dress
        elif kwtype == 'duty':
            self.__trigger, self.__head, self.__chains, self.__silence = kw_duty

    @noexcept
    def check(self, s):
        s = s.strip().lower().decode('gbk')
        print ('checking=>',s.encode('gbk'))
        for w in self.__trigger:
            if s.find(w) >= 0:
                break
        else:
            return False

        for w in self.__silence:
            if s.find(w) >= 0:
                return False

        def trace(keywords, chain, s, recursed=False):
            if keywords is None:
                return True

            while True:  # find layer contains keywords
                if chain.get(keywords):  # keywords itself is key
                    break  # just break out
                for layer in chain:  # search every word
                    for w in keywords:
                        if w in layer:
                            break  # at leat 1 keyword found in layer
                    else:
                        continue  # keyword not found in this layer, jump next layer
                    # found, break out if-in-layer  loop
                    keywords = layer
                    break
                else:
                    # not in any layer
                    # if recursing => succeeded tracing to tail
                    # if not, means current chain doesn contains thses keywords at all, return False
                    if not recursed:
                        return False
                    # finally check if msg contains keywords
                    for w in keywords:
                        if s.find(w) >= 0:
                            return True
                            break
                    else:
                        return False
                break

            # had found a keyword tuple in layer
            for w in keywords:
                if s.find(w) >= 0:  # msg should contain at least 1 keyword
                    # if it's real, than trace in
                    nextlayer = chain.get(keywords)
                    del chain[keywords]  # prevent circular trace
                    if nextlayer is None:  # traced to the end
                        return True  # succeeded
                    for nextkeywords in nextlayer:
                        if trace(nextkeywords, chain, s, True):  # at leat 1 chain succeeded
                            return True
                            break  # here had broken out, would not into else
                    else:  # all chains failed, so return False
                        return False
                    break
            else:  # msg doesnt contain any keyword so return False
                return False

        ret = False
        for trace_start_word in self.__head:
            if s.find(trace_start_word) >= 0:
                for chain in self.__chains:
                    ret = ret or bool(
                        trace((trace_start_word,), chain.copy(), s))
                    print('R=>', ret)
                    if ret:
                        break
                if ret:
                    break
        else:
            return False

        return ret
