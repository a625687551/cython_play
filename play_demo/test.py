# -*- coding:utf-8 -*-

import pickle
import os

from hello import say_hello
from viterbi import viterbi

from char_state_tab import P as char_state_tab_P
from prob_start import P as start_P
from prob_trans import P as trans_P
from prob_emit import P as emit_P


def test(sentence=u"很低"):
    prob, pos_list = viterbi(sentence, char_state_tab_P, start_P, trans_P, emit_P)
    print(prob, pos_list)


test()
