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


class Num2Word_YI_HE(Num2Word_EU):
    CURRENCY_FORMS = {
        'EUR': (("אױראָ", "אױראָ"), ("צענט", "צענט")),
        'GBP': (("פּונט", "פּונט"), ("פּעני", "פּענץ")),
        'USD': (("דאָללאַר", "דאָללאַר"), ("צענט", "צענט")),
        'CNY': (("יואַן", "יואַן"), ("jיִאַאָ", "פֿען")),
        'DEM': (("מאַרק", "מאַרק"), ("פּענניק", "פּענניק")),
    }

    GIGA_SUFFIX = "אילליִאַרדע"
    MEGA_SUFFIX = "אילליִאָן"

    def setup(self):
        self.negword = "מינוס"
        self.pointword = "קאָממאַ"
        # "cאַננאָט טרעאַט פֿלאָאַט %ס אַס אָרדינאַל."
        self.errmsg_floatord = (
            "דיִע גלעיִטקאָממאַזאַהל %ס קאַנן ניcהט אין עיִנע אָרדנונגסזאַהל" +
            "קאָנװערטיִערט wערדען."
            )
        # "טיפּה(((טיפּה(%ס)) ) נאָט אין [לאָנג, אינט, פֿלאָאַט]"
        self.errmsg_nonnum = (
            "נור זאַהלען (טיפּה(%ס)) קöננען אין wöרטער קאָנװערטיִערט wערדען."
            )
        # "cאַננאָט טרעאַט נעגאַטיװע נום %ס אַס אָרדינאַל."
        self.errmsg_negord = (
            "דיִע נעגאַטיװע זאַהל %ס קאַנן ניcהט אין עיִנע אָרדנונגסזאַהל" +
            "קאָנװערטיִערט wערדען."
            )
        # "אַבס(%ס) מוסט בע לעסס טהאַן %ס."
        self.errmsg_toobig = "דיִע זאַהל %ס מוסס קלעיִנער אַלס %ס סעיִן."
        self.exclude_title = []

        lows = ["נאָן", "אָקט", "סעפּט", "סעקסט", "קװינט", "קװאַדר", "טר", "ב", "מ"]
        units = ["", "און", "דואָ", "טרע", "qואַטטואָר", "qויִן", "סעx", "סעפּט",
                 "אָקטאָ", "נאָװעם"]
        tens = ["דעז", "װיגינט", "טריגינט", "qואַדראַגינט", "qויִנqואַגינט",
                "סעxאַגינט", "סעפּטואַגינט", "אָקטאָגינט", "נאָנאַגינט"]
        self.high_numwords = (
            ["זענט"] + self.gen_high_numwords(units, tens, lows)
        )
        self.mid_numwords = [(1000, "טױזנט"), (100, "הונדערט"),
                             (90, "נײַנציק"), (80, "אַכציק"), (70, "זיבעציק"),
                             (60, "זעכציק"), (50, "פֿופֿציק"),
                             (40, "פֿערציק"), (30, "דרײַסיק")]
        self.low_numwords = ["צװאַנציק", "נײַנצן", "אַכצן", "זיבעצן",
                             "זעכצן", "פֿופֿצן", "פֿערצן", "דרײַצן",
                             "צװעלף", "עלף", "צען", "נײַן", "אַכט",
                             "זיבן", "זעקס", "פֿינף", "פֿיר", "דרײַ",
                             "צװײ", "אײנס", "נול"]
        self.ords = {"אײנס": "ערס",
                     "דרײַ": "דריט",

                     #HB wrong form of character
                     #"אַכט": "אַך",
                     "אַכט": "אַכ",

                     #HB wrong form for -f in 12
                     "צװעלף":"צװעלפֿ",
                     #HB wrong -n in 17
                     "זיבעצן": "זיבעצנ",

                     "זיבן": "זיב",

                     #HB doesn't match -ik
                     "איק": "איקס",
                     #HB 'carrying' aleph removed
                     "יק": "יקס",
                     

                     "ערט": "ערץ",
                     "נט": "נץ",
                     "איאָן": "איאָנס",
                     "נען": "נס",
                     "רדע": "רדס",
                     "רדען": "רדס"}

    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1:
            if nnum == 100 or nnum == 1000:
                return ("אײן" + ntext, nnum)
            elif nnum < 10 ** 6:
                return next
            ctext = "אײנע"

        if nnum > cnum:
            if nnum >= 10 ** 6:
                if cnum > 1:
                    if ntext.endswith("ע"):
                        ntext += "נ"
                    else:
                        ntext += "ען"
                ctext += " "
            val = cnum * nnum
        else:
            if nnum < 10 < cnum < 100:
                if nnum == 1:
                    ntext = "אײן"
                ntext, ctext = ctext, ntext + " און"
            elif cnum >= 10 ** 6:
                ctext += " "
            val = cnum + nnum

        word = ctext + " " + ntext
        word = re.sub("  ", " ", word)
        return (word, val)

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        outword = self.to_cardinal(value).lower()
        print(f"{outword=}")
        for key in self.ords:
            print(f"{key=}")
            if outword.endswith(key):
                print(f"{outword=} ends with {key=}")
                outword = outword[:len(outword) - len(key)] + self.ords[key]
                break

        res = outword + "טע"

        # Exception: "הונדערטסטע" is usually preferred over "אײן הונדערטסטע"
        #if res == "אײן טױזנצטע" or res == "אײן הונדערטסטע":
        if res == "אײןטױזנצטע" or res == "אײןהונדערץטע":
            res = res.replace("אײן", "", 1)
            print(f"REMOVING ein from: {res=}")
        # ... similarly for "מילליִאָנסטע" etc.
        res = re.sub(r"אײנע ([אַ־ז]+(אילליִאָן|אילליִאַרד)סטע)$",
                     lambda m: m.group(1), res)
        # Ordinals involving "מילליִאָן" etc. are written without a space.
        # see https://de.wikipedia.org/wiki/Million#Sprachliches
        #res = re.sub(r' ([a-z]+(illion|illiard)ste)$',
        #             lambda m: m.group(1), res)

        return res

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return str(value) + "."

    def to_currency(self, val, currency='EUR', cents=True, separator=" און",
                    adjective=False):
        result = super(Num2Word_YI, self).to_currency(
            val, currency=currency, cents=cents, separator=separator,
            adjective=adjective)
        # Handle exception, in german is "עיִן עוראָ" and not "עיִנס עוראָ"
        return result.replace("אײנס", "אײן")

    def to_year(self, val, longval=True):
        if not (val // 100) % 10:
            return self.to_cardinal(val)
        return self.to_splitnum(val, hightxt="הונדערט", longval=longval)#.replace(' ', '')
