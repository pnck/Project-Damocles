#!/usr/bin/env python2
# -*- coding:gbk -*-

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

kw_isa_chain1_l1 = ('信安', '网安', '信息安全', '网络安全', 'vidar')
kw_isa_chain1_l2 = ('协会', '安协', '实验室')
kw_isa_chain1_l3 = ('哪', '位置', '怎么走', '地址', '怎么去', '咋去')
kw_isa_trigger = kw_isa_chain1_l3
kw_isa_silence = tuple()
kw_isa_head = kw_isa_chain1_l1
kw_isa_chain1 = {kw_isa_chain1_l1: (
    kw_isa_chain1_l2,), kw_isa_chain1_l2: (kw_isa_chain1_l3,)}
kw_chains_isa = [kw_isa_chain1]


kw_learn_chain1_l1 = ('c', 'c语言', '编程')
kw_learn_chain2_l1 = ('黑客', '信息安全', '安全', '信安')
kw_learn_chain3_l1 = ('看', '读', '用', '推荐')

kw_learn_chain1_l2 = ('怎么', '如何', '怎样', '咋')
kw_learn_chain2_l2 = ('有没有', '哪些', '什么', '有关', '啥')
kw_learn_chain3_l2 = ('想', '教', '要')

kw_learn_chain1_l3 = ('入门', '学', '开始')
kw_learn_chain2_l3 = ('书', '教材', '资料', '方法')
kw_learn_chain3_l3 = ('我', '当', '做', '成为', '搞')
kw_learn_trigger = kw_learn_chain1_l1 + kw_learn_chain2_l1 + \
    kw_learn_chain2_l2 + kw_learn_chain1_l3 + kw_learn_chain2_l3
kw_learn_silence = ('不', '拒绝', '禁', '别')
kw_learn_head = kw_learn_chain1_l1 + kw_learn_chain2_l1 + kw_learn_chain3_l1

kw_learn_chain1 = {kw_learn_chain1_l1: (kw_learn_chain1_l2, kw_learn_chain2_l2), kw_learn_chain1_l2: (
    kw_learn_chain1_l3,), kw_learn_chain2_l2: (kw_learn_chain2_l3,)}
kw_learn_chain2 = {kw_learn_chain2_l1: (kw_learn_chain1_l2, kw_learn_chain3_l2), kw_learn_chain1_l2: (
    kw_learn_chain1_l3,), kw_learn_chain3_l2: (kw_learn_chain3_l3,)}
kw_learn_chain3 = {kw_learn_chain3_l1: (kw_learn_chain2_l2,), kw_learn_chain2_l2: (
    kw_learn_chain1_l3, kw_learn_chain2_l3)}
kw_chains_learn = [kw_learn_chain1, kw_learn_chain2, kw_learn_chain3]


kw_hack_chain1_l1 = ('日', '黑', '拿', '入侵', '攻击', '扫')
kw_hack_chain2_l1 = ('拖', '扫')
kw_hack_chain3_l1 = ('盗',)
kw_hack_chain4_l1 = ('刷',)
kw_hack_chain5_l1 = ('制作', '写', '做')

kw_hack_chain1_l2 = ('站', '杭电', '学校', '官网', 'hdu', '论坛', '电脑', '服务器')
kw_hack_chain2_l2 = ('库', '数据', '资料')
kw_hack_chain3_l2 = ('q', '号')
kw_hack_chain4_l2 = ('会员', '钻')
kw_hack_chain5_l2 = ('挂',)
kw_hack_trigger = kw_hack_chain1_l2 + kw_hack_chain2_l2 + \
    kw_hack_chain3_l2 + kw_hack_chain4_l2 + kw_hack_chain5_l2 + kw_hack_chain1_l1
kw_hack_silence = tuple()
kw_hack_head = kw_hack_chain1_l1 + kw_hack_chain2_l1 + \
    kw_hack_chain3_l1 + kw_hack_chain4_l1 + kw_hack_chain5_l1

kw_hack_chain1 = {kw_hack_chain1_l1: (kw_hack_chain1_l2,)}
kw_hack_chain2 = {kw_hack_chain2_l1: (kw_hack_chain2_l2,)}
kw_hack_chain3 = {kw_hack_chain3_l1: (kw_hack_chain3_l2,)}
kw_hack_chain4 = {kw_hack_chain4_l1: (kw_hack_chain4_l2,)}
kw_hack_chain5 = {kw_hack_chain5_l1: (kw_hack_chain5_l2,)}
kw_chains_hack = [kw_hack_chain1, kw_hack_chain2,
                  kw_hack_chain3, kw_hack_chain4, kw_hack_chain5]

kw_reg_chain1_l1 = ('招新', '报名', '注册', '加入')
kw_reg_chain1_l2 = ('怎么', '哪')
kw_reg_chain2_l2 = ('有', '坏', '开')
kw_reg_chain2_l3 = ('地址', '吗')
kw_reg_trigger = kw_reg_chain1_l1
kw_reg_silence = ('还', '已经', '好了', '过', '的话')
kw_reg_head = kw_reg_chain1_l1

kw_reg_chain1 = {kw_reg_chain1_l1: (
    kw_reg_chain1_l2, kw_reg_chain2_l2), kw_reg_chain2_l2: (kw_reg_chain2_l3,)}
kw_chains_reg = [kw_reg_chain1]

kw_dress_chain1_l1 = ('女装')
kw_dress_trigger = kw_dress_chain1_l1
kw_dress_silence = tuple()
kw_dress_head = kw_dress_chain1_l1
kw_chains_dress = [{}]
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
            return None
    return wrapped


class KeywordChain(object):
    def __init__(self, kwtype):
        if kwtype not in ('reg', 'hack', 'learn', 'isa', 'dress'):
            raise Exception
        if kwtype == 'reg':
            self.__trigger = kw_reg_trigger
            self.__head = kw_reg_head
            self.__chains = kw_chains_reg
            self.__silence = kw_reg_silence
        elif kwtype == 'hack':
            self.__trigger = kw_hack_trigger
            self.__head = kw_hack_head
            self.__chains = kw_chains_hack
            self.__silence = kw_hack_silence
        elif kwtype == 'learn':
            self.__trigger = kw_learn_trigger
            self.__head = kw_learn_head
            self.__chains = kw_chains_learn
            self.__silence = kw_learn_silence
        elif kwtype == 'isa':
            self.__trigger = kw_isa_trigger
            self.__head = kw_isa_head
            self.__chains = kw_chains_isa
            self.__silence = kw_isa_silence
        elif kwtype == 'dress':
            self.__trigger = kw_dress_trigger
            self.__head = kw_dress_head
            self.__chains = kw_chains_dress
            self.__silence = kw_dress_silence

    @noexcept
    def check(self, s):
        s = s.strip().lower()
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

            # had found a keyword in layer
            for w in keywords:
                if s.find(w) >= 0:  # msg should contain at least 1 keyword
                    # if it's real, than trace in
                    nextlayer = chain.get(keywords)
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
                    ret = ret or bool(trace((trace_start_word,), chain, s))
                    print('R=>', ret)
                    if ret:
                        break
                if ret:
                    break
        else:
            return False

        return ret
