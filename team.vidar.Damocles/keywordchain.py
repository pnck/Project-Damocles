#!/usr/bin/env python2
# -*- coding:utf-8 -*-


# ########  KEY CHAINS STRUCTURE:
# #####     chains: [chain1,chain2,...] in chains
# ####      layers: {l1:(l1_linked1,l1_linked2,...),l2:(l2_linked,),...} in chain
# ###       keywords: (keyword1,keyword2,...) in layer
# ##        FULL: [chain1{l1:(c1l2,c2l2,c3l3,...),l2:(c1l3,)},chain2{...}]

kw_isa_chain1_l1 = ('信安', '网安', '信息安全', '网络安全', 'vidar')
kw_isa_chain1_l2 = ('协会', '安协', '实验室')
kw_isa_chain1_l3 = ('哪', '位置', '怎么走', '地址', '怎么去', '咋去')
kw_isa_trigger = kw_isa_chain1_l3
kw_isa_head = kw_isa_chain1_l1
kw_isa_chain1 = {kw_isa_chain1_l1: (
    kw_isa_chain1_l2,), kw_isa_chain1_l2: (kw_isa_chain1_l3,)}
kw_chains_isa = [kw_isa_chain1]


kw_learn_chain1_l1 = ('c', 'c语言', '编程')
kw_learn_chain2_l1 = ('黑客', '信息安全', '安全')

kw_learn_chain1_l2 = ('怎么', '如何', '怎样', '咋')
kw_learn_chain2_l2 = ('有没有', '哪些', '什么', '有关', '啥')
kw_learn_chain3_l2 = ('想', '教')

kw_learn_chain1_l3 = ('入门', '学', '开始')
kw_learn_chain2_l3 = ('书', '教材', '资料', '方法')
kw_learn_chain3_l3 = ('我', '当', '做', '成为', '搞')
kw_learn_trigger = kw_learn_chain1_l1 + kw_learn_chain2_l1 + \
    kw_learn_chain2_l2 + kw_learn_chain1_l3 + kw_learn_chain2_l3
kw_learn_head = kw_learn_chain1_l1 + kw_learn_chain2_l1

kw_learn_chain1 = {kw_learn_chain1_l1: (kw_learn_chain1_l2, kw_learn_chain2_l2), kw_learn_chain1_l2: (
    kw_learn_chain1_l3,), kw_learn_chain2_l2: (kw_learn_chain2_l3,)}
kw_learn_chain2 = {kw_learn_chain2_l1: (kw_learn_chain1_l2, kw_learn_chain3_l2), kw_learn_chain1_l2: (
    kw_learn_chain1_l3,), kw_learn_chain3_l2: (kw_learn_chain3_l3,)}
kw_chains_learn = [kw_learn_chain1, kw_learn_chain2]


kw_hack_chain1_l1 = ('日', '黑', '拿', '入侵', '攻击')
kw_hack_chain2_l1 = ('拖',)
kw_hack_chain3_l1 = ('盗',)
kw_hack_chain4_l1 = ('刷',)
kw_hack_chain5_l1 = ('制作', '写', '做')

kw_hack_chain1_l2 = ('站', '杭电', '学校', '官网', 'hdu', '论坛', '电脑', '服务器')
kw_hack_chain2_l2 = ('库', '数据', '资料')
kw_hack_chain3_l2 = ('q', '号')
kw_hack_chain4_l2 = ('会员', '钻')
kw_hack_chain5_l2 = ('挂',)
kw_hack_trigger = kw_hack_chain1_l2 + kw_hack_chain2_l2 + \
    kw_hack_chain3_l2 + kw_hack_chain4_l2 + kw_hack_chain5_l2
kw_hack_head = kw_hack_chain1_l1 + kw_hack_chain2_l1 + \
    kw_hack_chain3_l1 + kw_hack_chain4_l1 + kw_hack_chain5_l1

kw_hack_chain1 = {kw_hack_chain1_l1: (kw_hack_chain1_l2,)}
kw_hack_chain2 = {kw_hack_chain2_l1: (kw_hack_chain2_l2,)}
kw_hack_chain3 = {kw_hack_chain3_l1: (kw_hack_chain3_l2,)}
kw_hack_chain4 = {kw_hack_chain4_l1: (kw_hack_chain4_l2,)}
kw_hack_chain4 = {kw_hack_chain5_l1: (kw_hack_chain5_l2,)}
kw_chains_hack = [kw_hack_chain1, kw_hack_chain2,
                  kw_hack_chain3, kw_hack_chain4, kw_hack_chain5]

kw_reg_chain1_l1 = ('招新', '报名', '注册', '加入')
kw_reg_chain1_l2 = ('怎么', '哪')
kw_reg_chain2_l2 = ('有', '坏', '开')
kw_reg_chain2_l3 = ('地址', '吗')
kw_reg_trigger = kw_reg_chain1_l1
kw_reg_head = kw_reg_chain1_l1

kw_reg_chain1 = {kw_reg_chain1_l1: (
    kw_reg_chain1_l2, kw_reg_chain2_l2), kw_reg_chain2_l2: (kw_reg_chain2_l3,)}
kw_chains_reg = [kw_reg_chain1]

kw_dress_chain1_l1 = ('女装')
kw_dress_trigger = kw_dress_chain1_l1
kw_dress_head = kw_dress_chain1_l1
kw_chains_dress = [{}]
# ##
# ###
# ####
# ######   DONT FORMAT THIS AREA


class KeywordChain(object):
    def __init__(kwtype):
        if kwtype not in ('reg', 'hack', 'learn', 'isa', 'dress'):
            raise Exception
        if kwtype == 'reg':
            self.__trigger = kw_reg_trigger
            self.__head = kw_reg_head
            self.__chains = kw_chains_reg
        elif kwtype == 'hack':
            self.__trigger = kw_hack_trigger
            self.__head = kw_hack_head
            self.__chains = kw_chains_hack
        elif kwtype == 'learn':
            self.__trigger = kw_learn_trigger
            self.__head = kw_learn_head
            self.__chains = kw_chains_learn
        elif kwtype == 'isa':
            self.__trigger = kw_isa_trigger
            self.__head = kw_isa_head
            self.__chains = kw_chains_isa
        elif kwtype == 'dress':
            self.__trigger = kw_dress_trigger
            self.__head = kw_dress_head
            self.__chains = kw_chains_dress

    def check(self, s):
        s = s.strip()
        for w in self.__trigger:
            if s.find(w) >= 0:
                break
        else:
            return False

        trace_word = ''
        for w in self.__head:
            if s.find(w) >= 0:
                trace_word = w
                break
        else:
            return False

        def trace(kw, s):
            if kw is None:
                return True
            if s.find(kw) >= 0:
                p = self.__chains.get(kw)
                if p is None:
                    return True
                for tracing_word in p:
                    return trace(tracing_word, s)
            else:
                return False
        
        return trace(trace_word,s)
