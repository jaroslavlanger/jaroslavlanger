import re

string = " \t \r124.561.123 " # 'Cat \n eND'
string = "04.1 a–c"

number = r"(\d+(\.\d+)*)"
letter = r"[a-zA-Z]"
dash = r"[-–]"
comma = r"(\s*,\s*)"
letters = fr"({letter}+(({dash}|{comma}){letter}+)?)"
pattern = fr"\A\s*{number}\s*{letters}?\s*\Z"

# pattern = fr"\A\s*{number}{letter}+.*\Z"

findings = re.match( pattern, string, flags=re.I | re.DOTALL)

finding = findings.group(0) if (findings is not None) else findings
# print(finding)


string = "X.124.561.123 " # 'Cat \n eND'
string = "CoXoliv 1245.345.235"
string = "CoKo1iv 1245.345.235"
# string = "124.561.123 "
# string = "2124.561.123 "

pattern = r"[^1-9]+"
pattern = r"[^\dX]+"
findings = re.match(pattern, string, flags=re.IGNORECASE | re.DOTALL)

finding = findings.group(0) if (findings is not None) else findings
# print(finding)

# print("# Match space")

string = "X.12 "
# string = " 12 "

# pattern = r".*(X\.| \d)"
pattern = r".*((?<= )\d*|X(?=\.\d))"
# pattern = r".*(X(?=\.\d)|(?<= )\d*)"
# pattern = r".*(?<= )\d*"
# pattern = r"(?<=\s)\d*"
# pattern = r"\s\d*"
# findings = re.match(pattern, string, flags=re.IGNORECASE | re.DOTALL)
findings = re.match(pattern, string)

finding = findings.group(0) if (findings is not None) else findings
# print(finding)


# m = re.search(r"(?<= )\d*", ' 1124')
# print(m.group(0))

# ----------------------------------------------------------------------
ON = FEATURE = "Object Number"
BEF = "before"
AYE = FEATURE_TMP = "accession_year_extracted"
AFT = "after"

string = "CoKo1iv 1245.345.235"

string = " 1979.486.1"
string = "X.1979.486.1"
string = "Inst.1979.486.1"


# extract_pattern = fr'\A(?P<{BEF}>[^\dX]\D*)(?P<{FEATURE_TMP}>X\.d*\d*)(?P<{AFT}>.*)\Z'
# extract_pattern = fr'\A(?P<{BEF}>\D*)(?P<{FEATURE_TMP}>(?<= )\d*|X(?=\.\d))(?P<{AFT}>.*)\Z'
extract_pattern = fr'(?P<{BEF}>\D*)(?P<{FEATURE_TMP}>(\b|(?<= ))\d*|X(?=\.\d))(?P<{AFT}>.*)\Z'

extract_pattern = fr"(?P<{BEF}>\D*)(?P<{FEATURE_TMP}>\d)"
extract_pattern = fr"(?P<{BEF}>\D*)(?P<{FEATURE_TMP}>X)(?P<{AFT}>\.\d)"
extract_pattern = fr"(?P<{BEF}>\D*)(?P<{FEATURE_TMP}>(?<!X\.)\d+|X(?=\.\d))(?P<{AFT}>.*)\Z"
# extract_pattern = fr'\A(?P<{BEF}>\D*)(?P<{FEATURE_TMP}>((?<= )\d*|X(?=\.)))(?P<{AFT}>.*)\Z'
# extract_pattern = fr'\A(?P<{BEF}>\D*)(?P<{FEATURE_TMP}>\d*)(?P<{AFT}>.*)\Z'

findings = re.match(extract_pattern, string, flags=re.IGNORECASE)

# print(findings)

# print(dir(findings))

# for g in findings.groups():
#     print(g)

# finding = findings.group(0) if (findings is not None) else findings
# print(finding)

string = "3.7"
findings = re.match("(\d+)", string, flags=re.IGNORECASE)

# -----------------------------------------------------------------------------

STRINGS = [
    "1979.486.1",
    "2011.604.2.1141",
    "11.151.89",
    "63.350.329.701-16.38",
    "83.18.147",
    "45.24.41a–c",
    "Inst.1979.486.1",
    "I.67.1.2",
    "C.I.43.40.98a–c",
    "x.596",
    "x.451.2a–f",
    "PN2620 .S6 v.1 1763",
    "DC137.1 .B45 1909",
    "TR.124.2020",
    "Ref.MadridMap"
]


# extract_pattern = fr"(?P<{BEF}>(\D*|(\d(?!\.\d)))*)(?P<{AYE}>(?<!X\.|.[\w]|[^t]\.)\d+|X(?=\.\d))(?P<{AFT}>.*)\Z"
extract_pattern = fr"(?P<{BEF}>(\D*|(\d(?!\.\d)))*)(?P<{AYE}>(?<!X\.|.[\w]|[^t]\.)\d+|X(?=\.\d))(?P<{AFT}>.*)\Z"
extract_pattern = fr"(?P<{BEF}>.*)(?P<{AYE}>(?<!.[\w-]|[^ti]\.)(\d{{2}}){{1,2}}(?=\.|\Z|\s)|X)(?P<{AFT}>.*)"
# extract_pattern = fr"(?P<{BEF}>.*)(?P<{AYE}>[\d]{{2,4}})(?P<{AFT}>.*)"

# extract_pattern = fr".*([\.\s]\d+)"

for s in STRINGS:
    findings = re.match(extract_pattern, s, flags=re.IGNORECASE)
    if findings is not None:
        b, m, a = findings.groupdict()[BEF], findings.groupdict()[AYE], findings.groupdict()[AFT]
        # print(f"{s}\nb: {b}\nm: {m}\na: {a}\n")
    else:
        # print(f"{s}\n{findings}\n")
        pass

# print(findings)
# print(findings.group())
# for g in findings.groups():
#     print(g)

# for k,v in findings.groupdict().items():
#     print(k, v)


# ----------------------------------------------------------------------------------

STRINGS = [
    "1979.486.1",
    "2011.604.2.1141",
    "11.151.89",
    "63.350.329.701-16.38",
    "83.18.147",
    "45.24.41a–c",
    "Inst.1979.486.1",
    "I.67.1.2",
    "C.I.43.40.98a–c",
    "x.596",
    "x.451.2a–f",
    "PN2620 .S6 v.1 1763",
    "DC137.1 .B45 1909",
    "TR.124.2020",
    "Ref.MadridMap",
    "C.I.60.11.3",
    "Z270.F8 O4 v.1"
]


# extract_pattern = fr"(?P<{BEF}>(\D*|(\d(?!\.\d)))*)(?P<{AYE}>(?<!X\.|.[\w]|[^t]\.)\d+|X(?=\.\d))(?P<{AFT}>.*)\Z"
extract_pattern = fr"(?P<{BEF}>(\D*|(\d(?!\.\d)))*)(?P<{AYE}>(?<!X\.|.[\w]|[^t]\.)\d+|X(?=\.\d))(?P<{AFT}>.*)\Z"
extract_pattern = fr"(?P<{BEF}>.*)(?P<{AYE}>(?<!.[\w-]|[^ti]\.)(\d{{2}}){{1,2}}(?=\.|\Z|\s)|X)(?P<{AFT}>.*)"
# extract_pattern = fr"(?P<{BEF}>.*)(?P<{AYE}>[\d]{{2,4}})(?P<{AFT}>.*)"

extract_pattern = fr"(?P<{BEF}>.*)(?P<{AYE}>(?<!.[\w-]|[^ti]\.)(\d{{2}}){{1,2}}(?=\.|\Z|\s)|X)(?P<{AFT}>.*)"

extract_pattern = fr"(?P<{BEF}>\D*(t\.|i\.|\s|\A))(?P<{AYE}>(\d{{1,4}}|X)(?=\.))(?P<{AFT}>.*)"

# (?<!.[\w-]|[^ti]\.)

# extract_pattern = fr".*([\.\s]\d+)"

for s in STRINGS:
    findings = re.match(extract_pattern, s, flags=re.IGNORECASE)
    if findings is not None:
        b, m, a = findings.groupdict()[BEF], findings.groupdict()[AYE], findings.groupdict()[AFT]
        print(f"{s}\nb: {b}\nm: {m}\na: {a}\n")
    else:
        print(f"{s}\n{findings}\n")

