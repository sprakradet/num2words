# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import print_function, unicode_literals

import re

from .lang_EU import Num2Word_EU


class Num2Word_YI(Num2Word_EU):
    CURRENCY_FORMS = {
        'EUR': (("oyro", "oyro"), ("tsent", "tsent")),
        'GBP': (("punt", "punt"), ("peni", "pents")),
        'USD': (("dollar", "dollar"), ("tsent", "tsent")),
        'CNY': (("yuan", "yuan"), ("jiao", "fen")),
        'DEM': (("mark", "mark"), ("pennik", "pennik")),
    }

    GIGA_SUFFIX = "illiarde"
    MEGA_SUFFIX = "illion"

    def setup(self):
        self.negword = "minus "
        self.pointword = "komma"
        # "Cannot treat float %s as ordinal."
        self.errmsg_floatord = (
            "Die Gleitkommazahl %s kann nicht in eine Ordnungszahl " +
            "konvertiert werden."
            )
        # "type(((type(%s)) ) not in [long, int, float]"
        self.errmsg_nonnum = (
            "Nur Zahlen (type(%s)) können in Wörter konvertiert werden."
            )
        # "Cannot treat negative num %s as ordinal."
        self.errmsg_negord = (
            "Die negative Zahl %s kann nicht in eine Ordnungszahl " +
            "konvertiert werden."
            )
        # "abs(%s) must be less than %s."
        self.errmsg_toobig = "Die Zahl %s muss kleiner als %s sein."
        self.exclude_title = []

        lows = ["non", "okt", "sept", "sekst", "kvint", "kvadr", "tr", "b", "m"]
        units = ["", "un", "duo", "tre", "quattuor", "quin", "sex", "sept",
                 "okto", "novem"]
        tens = ["dez", "vigint", "trigint", "quadragint", "quinquagint",
                "sexagint", "septuagint", "oktogint", "nonagint"]
        self.high_numwords = (
            ["zent"] + self.gen_high_numwords(units, tens, lows)
        )
        self.mid_numwords = [(1000, "toyznt"), (100, "hundert"),
                             (90, "nayntsik"), (80, "akhtsik"), (70, "zibetsik"),
                             (60, "zekhtsik"), (50, "fuftsik"),
                             (40, "fertsik"), (30, "draysik")]
        self.low_numwords = ["tsvantsik", "nayntsn", "akhtsn", "zibetsn",
                             "zekhtsn", "fuftsn", "fertsn", "draytsn",
                             "tsvelf", "elf", "tsen", "nayn", "akht",
                             "zibn", "zeks", "finf", "fir", "dray",
                             "tsvey", "eyns", "null"]
        self.ords = {"eyns": "ers",
                     "dray": "drit",
                     "akht": "akh",
                     "zibn": "zib",
                     "ik": "iks",
                     "ert": "erts",
                     "nt": "nts",
                     "ion": "ions",
                     "nen": "ns",
                     "rde": "rds",
                     "rden": "rds"}

    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1:
            if nnum == 100 or nnum == 1000:
                return ("eyn " + ntext, nnum)
            elif nnum < 10 ** 6:
                return next
            ctext = "eyne"

        if nnum > cnum:
            if nnum >= 10 ** 6:
                if cnum > 1:
                    if ntext.endswith("e"):
                        ntext += "n"
                    else:
                        ntext += "en"
                ctext += " "
            val = cnum * nnum
        else:
            if nnum < 10 < cnum < 100:
                if nnum == 1:
                    ntext = "eyn"
                ntext, ctext = ctext, ntext + " un"
            elif cnum >= 10 ** 6:
                ctext += " "
            val = cnum + nnum

        word = ctext + " " + ntext
        word = re.sub("  ", " ", word)
        return (word, val)

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        outword = self.to_cardinal(value).lower()
        for key in self.ords:
            if outword.endswith(key):
                outword = outword[:len(outword) - len(key)] + self.ords[key]
                break

        res = outword + "te"

        # Exception: "hundertste" is usually preferred over "eyn hundertste"
        if res == "eyn toyzntste" or res == "eyn hundertste":
            res = res.replace("eyn ", "", 1)
        # ... similarly for "millionste" etc.
        res = re.sub(r"eyne ([a-z]+(illion|illiard)ste)$",
                     lambda m: m.group(1), res)
        # Ordinals involving "Million" etc. are written without a space.
        # see https://de.wikipedia.org/wiki/Million#Sprachliches
        #res = re.sub(r' ([a-z]+(illion|illiard)ste)$',
        #             lambda m: m.group(1), res)

        return res

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return str(value) + "."

    def to_currency(self, val, currency='EUR', cents=True, separator=" un",
                    adjective=False):
        result = super(Num2Word_YI, self).to_currency(
            val, currency=currency, cents=cents, separator=separator,
            adjective=adjective)
        # Handle exception, in german is "ein Euro" and not "eins Euro"
        return result.replace("eyns ", "eyn ")

    def to_year(self, val, longval=True):
        if not (val // 100) % 10:
            return self.to_cardinal(val)
        return self.to_splitnum(val, hightxt="hundert", longval=longval)#.replace(' ', '')
