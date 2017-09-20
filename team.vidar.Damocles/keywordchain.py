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
kw_isa_chain1_l1 = (u'�Ű�', u'����', u'��Ϣ��ȫ',
                    u'���簲ȫ', u'vidar')
kw_isa_chain1_l2 = (u'Э��', u'��Э', u'ʵ����')
kw_isa_chain1_l3 = (u'��', u'λ��', u'��ô��',
                    u'��ַ', u'��ôȥ', u'զȥ')
kw_isa_trigger = kw_isa_chain1_l3
kw_isa_silence = tuple()
kw_isa_head = kw_isa_chain1_l1 + kw_isa_chain1_l2
kw_isa_chain1 = {kw_isa_chain1_l1: (
    kw_isa_chain1_l2,), kw_isa_chain1_l2: (kw_isa_chain1_l3,)}
kw_chains_isa = [kw_isa_chain1]
kw_isa = (kw_isa_trigger, kw_isa_head, kw_chains_isa, kw_isa_silence)


# learn
kw_learn_chain1_l1 = (u'c', u'c����', u'���')
kw_learn_chain2_l1 = (u'�ڿ�', u'��Ϣ��ȫ', u'��ȫ', u'�Ű�')
kw_learn_chain3_l1 = ('��', '��', '��', '�Ƽ�')

kw_learn_chain1_l2 = (u'��ô', u'���', u'����', u'զ')
kw_learn_chain2_l2 = (u'��û��', u'��Щ', u'ʲô', u'�й�', u'ɶ')
kw_learn_chain3_l2 = ('��', '��', 'Ҫ')

kw_learn_chain1_l3 = (u'����', u'ѧ', u'��ʼ')
kw_learn_chain2_l3 = (u'��', u'�̲�', u'����', u'����')
kw_learn_chain3_l3 = (u'��', u'��', u'��', u'��Ϊ', u'��')
kw_learn_trigger = kw_learn_chain1_l1 + kw_learn_chain2_l1 + \
    kw_learn_chain2_l2 + kw_learn_chain1_l3 + kw_learn_chain2_l3
kw_learn_silence = (u'��', u'�ܾ�', u'��', u'��')
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
kw_hack_chain1_l1 = (u'��', u'��', u'��', u'����', u'����', u'ɨ')
kw_hack_chain2_l1 = (u'��', u'ɨ')
kw_hack_chain3_l1 = (u'��',)
kw_hack_chain4_l1 = (u'ˢ',)
kw_hack_chain5_l1 = (u'����', u'д', u'��')

kw_hack_chain1_l2 = (u'վ', u'����', u'ѧУ', u'����',
                     u'hdu', u'��̳', u'����', u'������')
kw_hack_chain2_l2 = (u'��', u'����', u'����')
kw_hack_chain3_l2 = (u'q', u'��')
kw_hack_chain4_l2 = (u'��Ա', u'��')
kw_hack_chain5_l2 = (u'��',)
kw_hack_trigger = kw_hack_chain1_l2 + kw_hack_chain2_l2 + \
    kw_hack_chain3_l2 + kw_hack_chain4_l2 + kw_hack_chain5_l2 + kw_hack_chain1_l1
kw_hack_silence = (u'��', u'��', u'����', u'��Ҫ',
                   u'�ܾ�', u'low', u'�ű�С��', u'��', u'��')
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
kw_reg_chain1_l1 = (u'����', u'����', u'ע��', u'����')
kw_reg_chain1_l2 = (u'��ô', u'��',u'��')
kw_reg_chain2_l2 = (u'��', u'��', u'��')
kw_reg_chain2_l3 = (u'��ַ', u'��',u'��')
kw_reg_trigger = kw_reg_chain1_l1
kw_reg_silence = (u'��', u'�Ѿ�', u'����', u'��', u'�Ļ�',u'Ϊʲô',u'Ϊɶ',u'��')
kw_reg_head = kw_reg_chain1_l1

kw_reg_chain1 = {kw_reg_chain1_l1: (
    kw_reg_chain1_l2, kw_reg_chain2_l2, kw_reg_chain2_l3), kw_reg_chain2_l2: (kw_reg_chain2_l3,)}
kw_chains_reg = [kw_reg_chain1]
kw_reg = (kw_reg_trigger, kw_reg_head, kw_chains_reg, kw_reg_silence)


# dress
kw_dress_chain1_l1 = (u'Ůװ', u'rbq')
kw_dress_chain1_l2 = (u'��', u'��', u'ȥ', u'��', u'��', u'��')
kw_dress_chain1_l3 = (u'Ⱥ��', u'����Ա', u'��', u'����', u'dalao')

kw_dress_trigger = kw_dress_chain1_l1
kw_dress_silence = (u'��',)
kw_dress_head = kw_dress_chain1_l1 + kw_dress_chain1_l2
kw_chains_dress = [{kw_dress_chain1_l1: (kw_dress_chain1_l2, kw_dress_chain1_l3), kw_dress_chain1_l2: (
    kw_dress_chain1_l3,), kw_dress_chain1_l3: (kw_dress_chain1_l1, kw_dress_chain1_l2)}]
kw_dress = (kw_dress_trigger, kw_dress_head, kw_chains_dress, kw_dress_silence)


# there is person on duty
kw_duty_chain1_l1 = kw_isa_chain1_l2  # = ('Э��', '��Э', 'ʵ����')
kw_duty_chain1_l1 += (u'111', u'613', u'3¥')
kw_duty_chain1_l2 = (u'��', u'��', u'ֵ��')
kw_duty_chain1_l3 = (u'��', u'ѧ��', u'��', u'����', u'dalao', u'˭')
kw_duty_trigger = kw_duty_chain1_l1
kw_duty_head = kw_duty_chain1_l1
kw_duty_silence = (u'��', u'û', u'����')
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
