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
    (1.00, 'eyn oyro un null tsent'),
    (2.01, 'tsvey oyro un eyn tsent'),
    (8.10, 'akht oyro un tsen tsent'),
    (12.26, 'tsvelf oyro un zeks un tsvantsik tsent'),
    (21.29, 'eyn un tsvantsik oyro un nayn un tsvantsik tsent'),
    (81.25, 'eyn un akhtsik oyro un finf un tsvantsik tsent'),
    (100.00, 'eyn hundert oyro un null tsent'),
)

TEST_CASES_TO_CURRENCY_USD = (
    (1.00, 'eyn dollar un null tsent'),
    (2.01, 'tsvey dollar un eyn tsent'),
    (8.10, 'akht dollar un tsen tsent'),
    (12.26, 'tsvelf dollar un zeks un tsvantsik tsent'),
    (21.29, 'eyn un tsvantsik dollar un nayn un tsvantsik tsent'),
    (81.25, 'eyn un akhtsik dollar un finf un tsvantsik tsent'),
    (100.00, 'eyn hundert dollar un null tsent'),
)

TEST_CASES_TO_CURRENCY_GBP = (
    (1.00, 'eyn punt un null pents'),
    (2.01, 'tsvey punt un eyn peni'),
    (8.10, 'akht punt un tsen pents'),
    (12.26, 'tsvelf punt un zeks un tsvantsik pents'),
    (21.29, 'eyn un tsvantsik punt un nayn un tsvantsik pents'),
    (81.25, 'eyn un akhtsik punt un finf un tsvantsik pents'),
    (100.00, 'eyn hundert punt un null pents'),
)

TEST_CASES_TO_CURRENCY_DEM = (
    (1.00, 'eyn mark un null pennik'),
    (2.01, 'tsvey mark un eyn pennik'),
    (8.10, 'akht mark un tsen pennik'),
    (12.26, 'tsvelf mark un zeks un tsvantsik pennik'),
    (21.29, 'eyn un tsvantsik mark un nayn un tsvantsik pennik'),
    (81.25, 'eyn un akhtsik mark un finf un tsvantsik pennik'),
    (100.00, 'eyn hundert mark un null pennik'),
)


class Num2WordsDETest(TestCase):

    def test_ordinal_less_than_twenty(self):
        self.assertEqual(num2words(0, ordinal=True, lang="yi"), 'nullte')
        self.assertEqual(num2words(1, ordinal=True, lang="yi"), 'erste')
        self.assertEqual(num2words(7, ordinal=True, lang="yi"), 'zibte')
        self.assertEqual(num2words(8, ordinal=True, lang="yi"), 'akhte')
        self.assertEqual(num2words(12, ordinal=True, lang="yi"), 'tsvelfte')
        self.assertEqual(num2words(17, ordinal=True, lang="yi"), 'zibetsnte')

    def test_ordinal_more_than_twenty(self):
        self.assertEqual(
            num2words(81, ordinal=True, lang="yi"), 'eyn un akhtsikste'
        )

    def test_ordinal_at_crucial_number(self):
        self.assertEqual(
            num2words(100, ordinal=True, lang="yi"), 'hundertste'
        )
        self.assertEqual(
            num2words(1000, ordinal=True, lang="yi"), 'toyzntste'
        )
        self.assertEqual(
            num2words(4000, ordinal=True, lang="yi"), 'fir toyzntste'
        )
        self.assertEqual(
           num2words(1000000, ordinal=True, lang="yi"), 'millionste'
        )
        self.assertEqual(
           num2words(2000000, ordinal=True, lang="yi"), 'tsvey millionste'
        )
        self.assertEqual(
           num2words(1000000000, ordinal=True, lang="yi"), 'milliardste'
        )
        self.assertEqual(
           num2words(5000000000, ordinal=True, lang="yi"),
           'finf milliardste'
        )

    def test_cardinal_at_some_numbers(self):
        self.assertEqual(num2words(100, lang="yi"), 'eyn hundert')
        self.assertEqual(num2words(1000, lang="yi"), 'eyn toyznt')
        self.assertEqual(num2words(5000, lang="yi"), 'finf toyznt')
        self.assertEqual(num2words(10000, lang="yi"), 'tsen toyznt')
        self.assertEqual(num2words(1000000, lang="yi"), 'eyne million')
        self.assertEqual(num2words(2000000, lang="yi"), 'tsvey millionen')
        self.assertEqual(num2words(4000000000, lang="yi"), 'fir milliarden')
        self.assertEqual(num2words(1000000000, lang="yi"), 'eyne milliarde')

    def test_cardinal_for_decimal_number(self):
        self.assertEqual(
            num2words(3.486, lang="yi"), 'dray komma fir akht zeks'
        )

    def test_giant_cardinal_for_merge(self):
        self.assertEqual(
            num2words(4500072900000111, lang="yi"),
            'fir billiarden finf hundert billionen ' +
            'tsvey un zibetsik milliarden nayn hundert millionen eyn hundert elf'
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(7, to="ordinal_num", lang="yi"), "7.")
        self.assertEqual(num2words(81, to="ordinal_num", lang="yi"), "81.")

    def test_ordinal_for_negative_numbers(self):
        self.assertRaises(TypeError, num2words, -12, ordinal=True, lang="yi")

    def test_ordinal_for_floating_numbers(self):
        self.assertRaises(TypeError, num2words, 2.453, ordinal=True, lang="yi")

    def test_currency_eur(self):
        for test in TEST_CASES_TO_CURRENCY_EUR:
            self.assertEqual(
                num2words(test[0], lang="yi", to="currency", currency="EUR"),
                test[1]
            )

    def test_currency_usd(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang="yi", to="currency", currency="USD"),
                test[1]
            )

    def test_currency_dem(self):
        for test in TEST_CASES_TO_CURRENCY_DEM:
            self.assertEqual(
                num2words(test[0], lang="yi", to="currency", currency="DEM"),
                test[1]
            )

    def test_currency_gbp(self):
        for test in TEST_CASES_TO_CURRENCY_GBP:
            self.assertEqual(
                num2words(test[0], lang="yi", to="currency", currency="GBP"),
                test[1]
            )

    def test_year(self):
        self.assertEqual(num2words(2002, to="year", lang="yi"),
                         'tsvey toyznt tsvey')

    def test_year_before_2000(self):
        self.assertEqual(num2words(1780, to="year", lang="yi"),
                         'zibetsn hundert akhtsik')
