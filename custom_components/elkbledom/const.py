from enum import Enum

DOMAIN = "elkbledom"
CONF_RESET = "reset"
CONF_DELAY = "delay"


class EFFECTS (Enum):
    effect_0 = 0x0
    effect_1 = 0x1
    effect_2 = 0x2
    effect_3 = 0x3
    effect_4 = 0x4
    effect_5 = 0x5
    effect_6 = 0x6
    effect_7 = 0x7
    effect_8 = 0x8
    effect_9 = 0x9
    effect_10 = 0xa
    effect_11 = 0xb
    effect_12 = 0xc
    effect_13 = 0xd
    effect_14 = 0xe
    effect_15 = 0xf
    effect_16 = 0x10
    effect_17 = 0x11
    effect_18 = 0x12
    effect_19 = 0x13
    effect_20 = 0x14
    effect_21 = 0x15
    effect_22 = 0x16
    effect_23 = 0x17
    effect_24 = 0x18
    effect_25 = 0x19
    effect_26 = 0x1a
    effect_27 = 0x1b
    effect_28 = 0x1c
    effect_29 = 0x1d
    effect_30 = 0x1e
    effect_31 = 0x1f
    effect_32 = 0x20
    effect_33 = 0x21
    effect_34 = 0x22
    effect_35 = 0x23
    effect_36 = 0x24
    effect_37 = 0x25
    effect_38 = 0x26
    effect_39 = 0x27
    effect_40 = 0x28
    effect_41 = 0x29
    effect_42 = 0x2a
    effect_43 = 0x2b
    effect_44 = 0x2c
    effect_45 = 0x2d
    effect_46 = 0x2e
    effect_47 = 0x2f
    effect_48 = 0x30
    effect_49 = 0x31
    effect_50 = 0x32
    effect_51 = 0x33
    effect_52 = 0x34
    effect_53 = 0x35
    effect_54 = 0x36
    effect_55 = 0x37
    effect_56 = 0x38
    effect_57 = 0x39
    effect_58 = 0x3a
    effect_59 = 0x3b
    effect_60 = 0x3c
    effect_61 = 0x3d
    effect_62 = 0x3e
    effect_63 = 0x3f
    effect_64 = 0x40
    effect_65 = 0x41
    effect_66 = 0x42
    effect_67 = 0x43
    effect_68 = 0x44
    effect_69 = 0x45
    effect_70 = 0x46
    effect_71 = 0x47
    effect_72 = 0x48
    effect_73 = 0x49
    effect_74 = 0x4a
    effect_75 = 0x4b
    effect_76 = 0x4c
    effect_77 = 0x4d
    effect_78 = 0x4e
    effect_79 = 0x4f
    effect_80 = 0x50
    effect_81 = 0x51
    effect_82 = 0x52
    effect_83 = 0x53
    effect_84 = 0x54
    effect_85 = 0x55
    effect_86 = 0x56
    effect_87 = 0x57
    effect_88 = 0x58
    effect_89 = 0x59
    effect_90 = 0x5a
    effect_91 = 0x5b
    effect_92 = 0x5c
    effect_93 = 0x5d
    effect_94 = 0x5e
    effect_95 = 0x5f
    effect_96 = 0x60
    effect_97 = 0x61
    effect_98 = 0x62
    effect_99 = 0x63
    effect_100 = 0x64
    effect_101 = 0x65
    effect_102 = 0x66
    effect_103 = 0x67
    effect_104 = 0x68
    effect_105 = 0x69
    effect_106 = 0x6a
    effect_107 = 0x6b
    effect_108 = 0x6c
    effect_109 = 0x6d
    effect_110 = 0x6e
    effect_111 = 0x6f
    effect_112 = 0x70
    effect_113 = 0x71
    effect_114 = 0x72
    effect_115 = 0x73
    effect_116 = 0x74
    effect_117 = 0x75
    effect_118 = 0x76
    effect_119 = 0x77
    effect_120 = 0x78
    effect_121 = 0x79
    effect_122 = 0x7a
    effect_123 = 0x7b
    effect_124 = 0x7c
    effect_125 = 0x7d
    effect_126 = 0x7e
    effect_127 = 0x7f
    effect_128 = 0x80
    effect_129 = 0x81
    effect_130 = 0x82
    effect_131 = 0x83
    effect_132 = 0x84
    effect_133 = 0x85
    effect_134 = 0x86
    effect_135 = 0x87
    effect_136 = 0x88
    effect_137 = 0x89
    effect_138 = 0x8a
    effect_139 = 0x8b
    effect_140 = 0x8c
    effect_141 = 0x8d
    effect_142 = 0x8e
    effect_143 = 0x8f
    effect_144 = 0x90
    effect_145 = 0x91
    effect_146 = 0x92
    effect_147 = 0x93
    effect_148 = 0x94
    effect_149 = 0x95
    effect_150 = 0x96
    effect_151 = 0x97
    effect_152 = 0x98
    effect_153 = 0x99
    effect_154 = 0x9a
    effect_155 = 0x9b
    effect_156 = 0x9c
    effect_157 = 0x9d
    effect_158 = 0x9e
    effect_159 = 0x9f
    effect_160 = 0xa0
    effect_161 = 0xa1
    effect_162 = 0xa2
    effect_163 = 0xa3
    effect_164 = 0xa4
    effect_165 = 0xa5
    effect_166 = 0xa6
    effect_167 = 0xa7
    effect_168 = 0xa8
    effect_169 = 0xa9
    effect_170 = 0xaa
    effect_171 = 0xab
    effect_172 = 0xac
    effect_173 = 0xad
    effect_174 = 0xae
    effect_175 = 0xaf
    effect_176 = 0xb0
    effect_177 = 0xb1
    effect_178 = 0xb2
    effect_179 = 0xb3
    effect_180 = 0xb4
    effect_181 = 0xb5
    effect_182 = 0xb6
    effect_183 = 0xb7
    effect_184 = 0xb8
    effect_185 = 0xb9
    effect_186 = 0xba
    effect_187 = 0xbb
    effect_188 = 0xbc
    effect_189 = 0xbd
    effect_190 = 0xbe
    effect_191 = 0xbf
    effect_192 = 0xc0
    effect_193 = 0xc1
    effect_194 = 0xc2
    effect_195 = 0xc3
    effect_196 = 0xc4
    effect_197 = 0xc5
    effect_198 = 0xc6
    effect_199 = 0xc7
    effect_200 = 0xc8
    effect_201 = 0xc9
    effect_202 = 0xca
    effect_203 = 0xcb
    effect_204 = 0xcc
    effect_205 = 0xcd
    effect_206 = 0xce
    effect_207 = 0xcf
    effect_208 = 0xd0
    effect_209 = 0xd1
    effect_210 = 0xd2
    effect_211 = 0xd3
    effect_212 = 0xd4
    effect_213 = 0xd5
    effect_214 = 0xd6
    effect_215 = 0xd7
    effect_216 = 0xd8
    effect_217 = 0xd9
    effect_218 = 0xda
    effect_219 = 0xdb
    effect_220 = 0xdc
    effect_221 = 0xdd
    effect_222 = 0xde
    effect_223 = 0xdf
    effect_224 = 0xe0
    effect_225 = 0xe1
    effect_226 = 0xe2
    effect_227 = 0xe3
    effect_228 = 0xe4
    effect_229 = 0xe5
    effect_230 = 0xe6
    effect_231 = 0xe7
    effect_232 = 0xe8
    effect_233 = 0xe9
    effect_234 = 0xea
    effect_235 = 0xeb
    effect_236 = 0xec
    effect_237 = 0xed
    effect_238 = 0xee
    effect_239 = 0xef
    effect_240 = 0xf0
    effect_241 = 0xf1
    effect_242 = 0xf2
    effect_243 = 0xf3
    effect_244 = 0xf4
    effect_245 = 0xf5
    effect_246 = 0xf6
    effect_247 = 0xf7
    effect_248 = 0xf8
    effect_249 = 0xf9
    effect_250 = 0xfa
    effect_251 = 0xfb
    effect_252 = 0xfc
    effect_253 = 0xfd
    effect_254 = 0xfe


EFFECTS_list = ['effect_0',
                'effect_1',
                'effect_2',
                'effect_3',
                'effect_4',
                'effect_5',
                'effect_6',
                'effect_7',
                'effect_8',
                'effect_9',
                'effect_10',
                'effect_11',
                'effect_12',
                'effect_13',
                'effect_14',
                'effect_15',
                'effect_16',
                'effect_17',
                'effect_18',
                'effect_19',
                'effect_20',
                'effect_21',
                'effect_22',
                'effect_23',
                'effect_24',
                'effect_25',
                'effect_26',
                'effect_27',
                'effect_28',
                'effect_29',
                'effect_30',
                'effect_31',
                'effect_32',
                'effect_33',
                'effect_34',
                'effect_35',
                'effect_36',
                'effect_37',
                'effect_38',
                'effect_39',
                'effect_40',
                'effect_41',
                'effect_42',
                'effect_43',
                'effect_44',
                'effect_45',
                'effect_46',
                'effect_47',
                'effect_48',
                'effect_49',
                'effect_50',
                'effect_51',
                'effect_52',
                'effect_53',
                'effect_54',
                'effect_55',
                'effect_56',
                'effect_57',
                'effect_58',
                'effect_59',
                'effect_60',
                'effect_61',
                'effect_62',
                'effect_63',
                'effect_64',
                'effect_65',
                'effect_66',
                'effect_67',
                'effect_68',
                'effect_69',
                'effect_70',
                'effect_71',
                'effect_72',
                'effect_73',
                'effect_74',
                'effect_75',
                'effect_76',
                'effect_77',
                'effect_78',
                'effect_79',
                'effect_80',
                'effect_81',
                'effect_82',
                'effect_83',
                'effect_84',
                'effect_85',
                'effect_86',
                'effect_87',
                'effect_88',
                'effect_89',
                'effect_90',
                'effect_91',
                'effect_92',
                'effect_93',
                'effect_94',
                'effect_95',
                'effect_96',
                'effect_97',
                'effect_98',
                'effect_99',
                'effect_100',
                'effect_101',
                'effect_102',
                'effect_103',
                'effect_104',
                'effect_105',
                'effect_106',
                'effect_107',
                'effect_108',
                'effect_109',
                'effect_110',
                'effect_111',
                'effect_112',
                'effect_113',
                'effect_114',
                'effect_115',
                'effect_116',
                'effect_117',
                'effect_118',
                'effect_119',
                'effect_120',
                'effect_121',
                'effect_122',
                'effect_123',
                'effect_124',
                'effect_125',
                'effect_126',
                'effect_127',
                'effect_128',
                'effect_129',
                'effect_130',
                'effect_131',
                'effect_132',
                'effect_133',
                'effect_134',
                'effect_135',
                'effect_136',
                'effect_137',
                'effect_138',
                'effect_139',
                'effect_140',
                'effect_141',
                'effect_142',
                'effect_143',
                'effect_144',
                'effect_145',
                'effect_146',
                'effect_147',
                'effect_148',
                'effect_149',
                'effect_150',
                'effect_151',
                'effect_152',
                'effect_153',
                'effect_154',
                'effect_155',
                'effect_156',
                'effect_157',
                'effect_158',
                'effect_159',
                'effect_160',
                'effect_161',
                'effect_162',
                'effect_163',
                'effect_164',
                'effect_165',
                'effect_166',
                'effect_167',
                'effect_168',
                'effect_169',
                'effect_170',
                'effect_171',
                'effect_172',
                'effect_173',
                'effect_174',
                'effect_175',
                'effect_176',
                'effect_177',
                'effect_178',
                'effect_179',
                'effect_180',
                'effect_181',
                'effect_182',
                'effect_183',
                'effect_184',
                'effect_185',
                'effect_186',
                'effect_187',
                'effect_188',
                'effect_189',
                'effect_190',
                'effect_191',
                'effect_192',
                'effect_193',
                'effect_194',
                'effect_195',
                'effect_196',
                'effect_197',
                'effect_198',
                'effect_199',
                'effect_200',
                'effect_201',
                'effect_202',
                'effect_203',
                'effect_204',
                'effect_205',
                'effect_206',
                'effect_207',
                'effect_208',
                'effect_209',
                'effect_210',
                'effect_211',
                'effect_212',
                'effect_213',
                'effect_214',
                'effect_215',
                'effect_216',
                'effect_217',
                'effect_218',
                'effect_219',
                'effect_220',
                'effect_221',
                'effect_222',
                'effect_223',
                'effect_224',
                'effect_225',
                'effect_226',
                'effect_227',
                'effect_228',
                'effect_229',
                'effect_230',
                'effect_231',
                'effect_232',
                'effect_233',
                'effect_234',
                'effect_235',
                'effect_236',
                'effect_237',
                'effect_238',
                'effect_239',
                'effect_240',
                'effect_241',
                'effect_242',
                'effect_243',
                'effect_244',
                'effect_245',
                'effect_246',
                'effect_247',
                'effect_248',
                'effect_249',
                'effect_250',
                'effect_251',
                'effect_252',
                'effect_253',
                'effect_254'
                ]


class WEEK_DAYS (Enum):
    monday = 0x01
    tuesday = 0x02
    wednesday = 0x04
    thursday = 0x08
    friday = 0x10
    saturday = 0x20
    sunday = 0x40
    all = (0x01 + 0x02 + 0x04 + 0x08 + 0x10 + 0x20 + 0x40)
    week_days = (0x01 + 0x02 + 0x04 + 0x08 + 0x10)
    weekend_days = (0x20 + 0x40)
    none = 0x00

# print(EFFECTS.blink_red.value)
