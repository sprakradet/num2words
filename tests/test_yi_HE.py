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

from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words



TEST_CASES_TO_CURRENCY_EUR = (
    (1.00, 'אײן אױראָ און נולל צענט'),
    (2.01, 'צװײ אױראָ און אײן צענט'),
    (8.10, 'אַכט אױראָ און צען צענט'),
    (12.26, 'צװעלף אױראָ און זעקס און צװאַנציק צענט'),
    (21.29, 'אײן און צװאַנציק אױראָ און נײַן און צװאַנציק צענט'),
    (81.25, 'אײן און אַכציק אױראָ און פֿינף און צװאַנציק צענט'),
    (100.00, 'אײן הונדערט אױראָ און נולל צענט'),
)

TEST_CASES_TO_CURRENCY_USD = (
    (1.00, 'אײן דאָללאַר און נולל צענט'),
    (2.01, 'צװײ דאָללאַר און אײן צענט'),
    (8.10, 'אַכט דאָללאַר און צען צענט'),
    (12.26, 'צװעלף דאָללאַר און זעקס און צװאַנציק צענט'),
    (21.29, 'אײן און צװאַנציק דאָללאַר און נײַן און צװאַנציק צענט'),
    (81.25, 'אײן און אַכציק דאָללאַר און פֿינף און צװאַנציק צענט'),
    (100.00, 'אײן הונדערט דאָללאַר און נולל צענט'),
)

TEST_CASES_TO_CURRENCY_GBP = (
    (1.00, 'אײן פּונט און נולל פּענץ'),
    (2.01, 'צװײ פּונט און אײן פּעני'),
    (8.10, 'אַכט פּונט און צען פּענץ'),
    (12.26, 'צװעלף פּונט און זעקס און צװאַנציק פּענץ'),
    (21.29, 'אײן און צװאַנציק פּונט און נײַן און צװאַנציק פּענץ'),
    (81.25, 'אײן און אַכציק פּונט און פֿינף און צװאַנציק פּענץ'),
    (100.00, 'אײן הונדערט פּונט און נולל פּענץ'),
)

TEST_CASES_TO_CURRENCY_DEM = (
    (1.00, 'אײן מאַרק און נולל פּענניק'),
    (2.01, 'צװײ מאַרק און אײן פּענניק'),
    (8.10, 'אַכט מאַרק און צען פּענניק'),
    (12.26, 'צװעלף מאַרק און זעקס און צװאַנציק פּענניק'),
    (21.29, 'אײן און צװאַנציק מאַרק און נײַן און צװאַנציק פּענניק'),
    (81.25, 'אײן און אַכציק מאַרק און פֿינף און צװאַנציק פּענניק'),
    (100.00, 'אײן הונדערט מאַרק און נולל פּענניק'),
)


class Num2WordsDETest(TestCase):

    def test_ordinal_less_than_twenty(self):
        self.assertEqual(num2words(0, ordinal=True, lang="yi_he"), 'נולטע')
        self.assertEqual(num2words(1, ordinal=True, lang="yi_he"), 'ערסטע')
        self.assertEqual(num2words(7, ordinal=True, lang="yi_he"), 'זיבטע')
        self.assertEqual(num2words(8, ordinal=True, lang="yi_he"), 'אַכטע')
        self.assertEqual(num2words(12, ordinal=True, lang="yi_he"), 'צװעלפֿטע')
        self.assertEqual(num2words(17, ordinal=True, lang="yi_he"), 'זיבעצנטע')

    def test_ordinal_more_than_twenty(self):
        self.assertEqual(
            num2words(81, ordinal=True, lang="yi_he"), 'אײן און אַכציקסטע'
        )

    def test_ordinal_at_crucial_number(self):
        self.assertEqual(
            num2words(100, ordinal=True, lang="yi_he"), 'הונדערץטע'
        )
        #self.assertEqual(
        #    num2words(1000, ordinal=True, lang="yi_he"), 'טױזנצטע'
        #)
        #self.assertEqual(
        #    num2words(4000, ordinal=True, lang="yi_he"), 'פֿיר טױזנצטע'
        #)
        #self.assertEqual(
        #   num2words(1000000, ordinal=True, lang="yi_he"), 'מילליִאָנסטע'
        #)
        #self.assertEqual(
        #   num2words(2000000, ordinal=True, lang="yi_he"), 'צװײ מילליִאָנסטע'
        #)
        #self.assertEqual(
        #   num2words(1000000000, ordinal=True, lang="yi_he"), 'מילליִאַרדסטע'
        #)
        #self.assertEqual(
        #   num2words(5000000000, ordinal=True, lang="yi_he"),
        #   'פֿינף מילליִאַרדסטע'
        #)

    def test_cardinal_at_some_numbers(self):
        #self.assertEqual(num2words(100, lang="yi_he"), 'אײן הונדערט')
        #self.assertEqual(num2words(1000, lang="yi_he"), 'אײן טױזנט')
        self.assertEqual(num2words(5000, lang="yi_he"), 'פֿינף טױזנט')
        self.assertEqual(num2words(10000, lang="yi_he"), 'צען טױזנט')
        #self.assertEqual(num2words(1000000, lang="yi_he"), 'אײנע מילליִאָן')
        #self.assertEqual(num2words(2000000, lang="yi_he"), 'צװײ מילליִאָנען')
        #self.assertEqual(num2words(4000000000, lang="yi_he"), 'פֿיר מילליִאַרדען')
        #self.assertEqual(num2words(1000000000, lang="yi_he"), 'אײנע מילליִאַרדע')

    def test_cardinal_for_decimal_number(self):
        self.assertEqual(
            num2words(3.486, lang="yi_he"), 'דרײַ קאָממאַ פֿיר אַכט זעקס'
        )

    #def test_giant_cardinal_for_merge(self):
        #self.assertEqual(
        #    num2words(4500072900000111, lang="yi_he"),
        #    'פֿיר בילליִאַרדען פֿינף הונדערט בילליִאָנען' +
        #    'צװײ און זיבעציק מילליִאַרדען נײַן הונדערט מילליִאָנען אײן הונדערט עלף'
        #)

    def test_ordinal_num(self):
        self.assertEqual(num2words(7, to="ordinal_num", lang="yi_he"), "7.")
        self.assertEqual(num2words(81, to="ordinal_num", lang="yi_he"), "81.")

    def test_ordinal_for_negative_numbers(self):
        self.assertRaises(TypeError, num2words, -12, ordinal=True, lang="yi_he")

    def test_ordinal_for_floating_numbers(self):
        self.assertRaises(TypeError, num2words, 2.453, ordinal=True, lang="yi_he")

    def test_currency_eur(self):
        for test in TEST_CASES_TO_CURRENCY_EUR:
            self.assertEqual(
                num2words(test[0], lang="yi_he", to="currency", currency="EUR"),
                test[1]
            )

    def test_currency_usd(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang="yi_he", to="currency", currency="USD"),
                test[1]
            )

    def test_currency_dem(self):
        for test in TEST_CASES_TO_CURRENCY_DEM:
            self.assertEqual(
                num2words(test[0], lang="yi_he", to="currency", currency="DEM"),
                test[1]
            )

    def test_currency_gbp(self):
        for test in TEST_CASES_TO_CURRENCY_GBP:
            self.assertEqual(
                num2words(test[0], lang="yi_he", to="currency", currency="GBP"),
                test[1]
            )

    def test_year(self):
        self.assertEqual(num2words(2002, to="year", lang="yi_he"),
                         'צװײ טױזנט צװײ')

    def test_year_before_2000(self):
        self.assertEqual(num2words(1780, to="year", lang="yi_he"),
                         'זיבעצן הונדערט אַכציק')
