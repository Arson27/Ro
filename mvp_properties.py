# -*- coding: utf-8 -*-
"""
Contains properties of every MvP in the game.
Used to feed into mvp module and to build the list.
"""

mvp_names = [
              'Amon Ra', 'Angeling (pay_fild04)', 'Angeling (xmas_dun01)',
              'Angeling (yuno_fild04)', 'Angry Student Pyuriel', 'Archangeling',
              'Atroce (gld_dun03_2)', 'Atroce (ra_fild03)', 'Atroce (ra_fild04)',
              'Atroce (ve_fild01)', 'Atroce (ve_fild02)', 'Bacsojin',
              'Baphomet (gld_dun03)', 'Baphomet (prt_maze03)', 'Beelzebub',
              'Bio3 MVP', 'Bio4 MVP', 'Boitata', 'Dark Guardian Kades',
              'Dark Lord (gld_dun04_2)', 'Dark Lord (gl_chyard)', 'Detale',
              'Deviling (pay_fild04)', 'Deviling (yuno_fild03)', 'Doppelganger (gef_dun02)',
              'Doppelganger (gld_dun04)', 'Dracula', 'Drake', 'Eddga (gld_dun01_2)',
              'Eddga (pay_fild10)', 'Egnigem Cenia', 'Evil Snake Lord', 'Fallen Bishop Hibram',
              'Garm', 'General Darhyun', 'Ghostring (gld_dun04)', 'Ghostring (pay_fild04)',
              'Ghostring (prt_maze03)', 'Ghostring (treasure02)', 'Gioia',
              'Gloom Under Night', 'Golden Thief Bug', 'Gopinich', 'Hardrock Mammoth',
              'Ifrit', 'Incantation Samurai', 'Kiel D-01', 'Kraken', 'Ktullanux',
              'Lady Tanee', 'Leak', 'Lord of Death', 'Maya (anthell02)',
              'Maya (gld_dun02_2)', 'Maya Purple (gld2_ald)', 'Maya Purple (gld_dun02_2)',
              'Mistress (gld_dun02)', 'Mistress (mjolnir_04)', 'Moonlight Flower (gld_dun01)',
              'Moonlight Flower (pay_dun04)', 'Nightmare Amon Ra', 'Orc Hero', 'Orc Lord',
              'Osiris', 'Pharaoh', 'Phreeoni', 'Queen Scaraba', 'RSX-0806', 'Stormy Knight',
              'Tao Gunka', 'Tendrillion', 'Thanatos', 'Turtle General', 'Valkyrie Randgris',
              'Vesper', 'Wounded Morroc'
              ]

mvp_respawn_min_minutes = [
                   60, 60, 60, 60, 480, 60, 480, 180, 300, 180, 360, 117, 480,
                   120, 720, 100, 100, 120, 480, 480, 60, 180, 120, 60, 120,
                   480, 60, 120, 480, 120, 120, 94, 120, 120, 480, 240, 60,
                   113, 33, 480, 300, 60, 120, 240, 660, 91, 120, 120, 120,
                   420, 120, 133, 120, 480, 20, 20, 480, 120, 480, 60, 60,
                   60, 120, 60, 60, 120, 120, 125, 60, 300, 60, 120, 60, 480, 120, 720
                   ]

mvp_respawn_max_minutes = [
                   70, 90, 90, 90, 490, 63, 490, 190, 310, 190, 370, 127, 490,
                   130, 730, 130, 130, 130, 490, 490, 70, 190, 180, 90, 130, 490,
                   70, 130, 490, 130, 130, 104, 130, 130, 490, 360, 90, 170, 53,
                   490, 310, 70, 130, 241, 670, 101, 180, 150, 121, 430, 130,
                   134, 130, 490, 21, 30, 490, 130, 490, 70, 70, 70, 130, 70,
                   70, 130, 121, 135, 70, 310, 61, 121, 70, 490, 130, 780
                   ]

#converts from minutes to seconds
mvp_respawn_min = [i * 60 for i in mvp_respawn_min_minutes]
mvp_respawn_max = [i * 60 for i in mvp_respawn_max_minutes]

mvp_location = ['moc_pryd06', 'pay_fild04', 'xmas_dun01', 'yuno_fild03', 'gld2_prt',
                'yuno_fild04', 'gld_dun03_2', 'ra_fild03', 'ra_fild04', 've_fild01',
                've_fild02', 'lou_dun03', 'gld_dun03', 'prt_maze03', 'abbey03',
                'lhz_dun03', 'lhz_dun04', 'bra_dun02', 'gld2_gef', 'gld_dun04_2',
                'gl_chyard', 'abyss_03', 'pay_fild04', 'yuno_fild03', 'gef_dun02',
                'gld_dun04', 'gef_dun01', 'treasure02', 'gld_dun01_2', 'pay_fild10',
                'lhz_dun02', 'gon_dun03', 'abbey02', 'xmas_fild01', 'gld2_pay',
                'gld_dun04', 'pay_fild04', 'prt_maze03', 'treasure02', 'gld2_ald',
                'ra_san05', 'prt_sewb4', 'mosk_dun03', 'man_fild03', 'thor_v03',
                'ama_dun03', 'kh_dun02', 'iz_dun05', 'ice_dun03', 'ayo_dun02', 
                'dew_dun01', 'niflheim', 'anthell02', 'gld_dun02_2', 'gld2_ald',
                'gld_dun02_2', 'gld_dun02', 'mjolnir_04', 'gld_dun01', 'pay_dun04',
                'moc_prydn2', 'gef_fild03', 'gef_fild10', 'moc_pryd04', 'in_sphinx5',
                'moc_fild17', 'dic_dun02', 'ein_dun02', 'xmas_dun02', 'beach_dun',
                'spl_fild03', 'thana_boss', 'tur_dun04', 'odin_tem03', 'jupe_core',
                'moc_fild22']