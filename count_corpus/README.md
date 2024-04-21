Here's a bunch of scripts to count stuff in corpora and other text datasets. They are language agnostic and very useful.

### `count_and_identify_unicode_chars.py`

Example applications:
- run it on a big text dataset and see if you don't have any weird unwanted characters or quotes in languages using other character set
- identify encoding errors
- tell apart é from é and a from а

Example output:
(it doesn't give a Unicode name of tab and newline)
```
 	24	0x20	SPACE
a	14	0x61	LATIN SMALL LETTER A
k	12	0x6b	LATIN SMALL LETTER K
o	12	0x6f	LATIN SMALL LETTER O
t	12	0x74	LATIN SMALL LETTER T
e	12	0x65	LATIN SMALL LETTER E
z	8	0x7a	LATIN SMALL LETTER Z
'\n'	7	0xa
'\t'	6	0x9
n	6	0x6e	LATIN SMALL LETTER N
i	6	0x69	LATIN SMALL LETTER I
,	6	0x2c	COMMA
ł	5	0x142	LATIN SMALL LETTER L WITH STROKE
r	4	0x72	LATIN SMALL LETTER R
u	4	0x75	LATIN SMALL LETTER U
w	3	0x77	LATIN SMALL LETTER W
p	3	0x70	LATIN SMALL LETTER P
g	3	0x67	LATIN SMALL LETTER G
d	3	0x64	LATIN SMALL LETTER D
s	3	0x73	LATIN SMALL LETTER S
c	3	0x63	LATIN SMALL LETTER C
K	3	0x4b	LATIN CAPITAL LETTER K
l	2	0x6c	LATIN SMALL LETTER L
m	2	0x6d	LATIN SMALL LETTER M
!	2	0x21	EXCLAMATION MARK
j	2	0x6a	LATIN SMALL LETTER J
ó	1	0xf3	LATIN SMALL LETTER O WITH ACUTE
ś	1	0x15b	LATIN SMALL LETTER S WITH ACUTE
́	1	0x301	COMBINING ACUTE ACCENT
é	1	0xe9	LATIN SMALL LETTER E WITH ACUTE
а	1	0x430	CYRILLIC SMALL LETTER A
```

### `count_wordforms.py`

Example applications:
- count word frequency in a text
- identify frequently appearing words that you might want to anonymize or do something else with

Example output:
(it's case sensitive!)
```
,	6
kot	4
Kot	3
niedługa	2
!	2
raz	2
	2
wlazł	1
kotek	1
na	1
płotek	1
i	1
mruga	1
ładna	1
to	1
piosenka	1
niekrótka	1
lecz	1
w	1
sam	1
zaśpiewaj	1
koteczku	1
jeszcze	1
é	1
é	1
а	1
```

