

import random
import re , csv , sys
import requests
from ..core.logger import log

BINS_DICT ={}
def get_iso(country_code):
    x = {'Afghanistan': 'AF',
         'Albania': 'AL',
         'Algeria': 'DZ',
         'American Samoa': 'AS',
         'Andorra': 'AD',
         'Angola': 'AO',
         'Anguilla': 'AI',
         'Antarctica': 'AQ',
         'Antigua and Barbuda': 'AG',
         'Argentina': 'AR',
         'Armenia': 'AM',
         'Aruba': 'AW',
         'Australia': 'AU',
         'Austria': 'AT',
         'Azerbaijan': 'AZ',
         'Bahamas': 'BS',
         'Bahrain': 'BH',
         'Bangladesh': 'BD',
         'Barbados': 'BB',
         'Belarus': 'BY',
         'Belgium': 'BE',
         'Belize': 'BZ',
         'Benin': 'BJ',
         'Bermuda': 'BM',
         'Bhutan': 'BT',
         'Bolivia, Plurinational State of': 'BO',
         'Bonaire, Sint Eustatius and Saba': 'BQ',
         'Bosnia and Herzegovina': 'BA',
         'Botswana': 'BW',
         'Bouvet Island': 'BV',
         'Brazil': 'BR',
         'British Indian Ocean Territory': 'IO',
         'Brunei Darussalam': 'BN',
         'Bulgaria': 'BG',
         'Burkina Faso': 'BF',
         'Burundi': 'BI',
         'Cambodia': 'KH',
         'Cameroon': 'CM',
         'Canada': 'CA',
         'Cape Verde': 'CV',
         'Cayman Islands': 'KY',
         'Central African Republic': 'CF',
         'Chad': 'TD',
         'Chile': 'CL',
         'China': 'CN',
         'Christmas Island': 'CX',
         'Cocos (Keeling) Islands': 'CC',
         'Colombia': 'CO',
         'Comoros': 'KM',
         'Congo': 'CG',
         'Congo, the Democratic Republic of the': 'CD',
         'Cook Islands': 'CK',
         'Costa Rica': 'CR',
         'Country name': 'Code',
         'Croatia': 'HR',
         'Cuba': 'CU',
         'Curaçao': 'CW',
         'Cyprus': 'CY',
         'Czech Republic': 'CZ',
         "Côte d'Ivoire": 'CI',
         'Denmark': 'DK',
         'Djibouti': 'DJ',
         'Dominica': 'DM',
         'Dominican Republic': 'DO',
         'Ecuador': 'EC',
         'Egypt': 'EG',
         'El Salvador': 'SV',
         'Equatorial Guinea': 'GQ',
         'Eritrea': 'ER',
         'Estonia': 'EE',
         'Ethiopia': 'ET',
         'Falkland Islands (Malvinas)': 'FK',
         'Faroe Islands': 'FO',
         'Fiji': 'FJ',
         'Finland': 'FI',
         'France': 'FR',
         'French Guiana': 'GF',
         'French Polynesia': 'PF',
         'French Southern Territories': 'TF',
         'Gabon': 'GA',
         'Gambia': 'GM',
         'Georgia': 'GE',
         'Germany': 'DE',
         'Ghana': 'GH',
         'Gibraltar': 'GI',
         'Greece': 'GR',
         'Greenland': 'GL',
         'Grenada': 'GD',
         'Guadeloupe': 'GP',
         'Guam': 'GU',
         'Guatemala': 'GT',
         'Guernsey': 'GG',
         'Guinea': 'GN',
         'Guinea-Bissau': 'GW',
         'Guyana': 'GY',
         'Haiti': 'HT',
         'Heard Island and McDonald Islands': 'HM',
         'Holy See (Vatican City State)': 'VA',
         'Honduras': 'HN',
         'Hong Kong': 'HK',
         'Hungary': 'HU',
         'ISO 3166-2:GB': '(.uk)',
         'Iceland': 'IS',
         'India': 'IN',
         'Indonesia': 'ID',
         'Iran, Islamic Republic of': 'IR',
         'Iraq': 'IQ',
         'Ireland': 'IE',
         'Isle of Man': 'IM',
         'Israel': 'IL',
         'Italy': 'IT',
         'Jamaica': 'JM',
         'Japan': 'JP',
         'Jersey': 'JE',
         'Jordan': 'JO',
         'Kazakhstan': 'KZ',
         'Kenya': 'KE',
         'Kiribati': 'KI',
         "Korea, Democratic People's Republic of": 'KP',
         'Korea, Republic of': 'KR',
         'Kuwait': 'KW',
         'Kyrgyzstan': 'KG',
         "Lao People's Democratic Republic": 'LA',
         'Latvia': 'LV',
         'Lebanon': 'LB',
         'Lesotho': 'LS',
         'Liberia': 'LR',
         'Libya': 'LY',
         'Liechtenstein': 'LI',
         'Lithuania': 'LT',
         'Luxembourg': 'LU',
         'Macao': 'MO',
         'Macedonia, the former Yugoslav Republic of': 'MK',
         'Madagascar': 'MG',
         'Malawi': 'MW',
         'Malaysia': 'MY',
         'Maldives': 'MV',
         'Mali': 'ML',
         'Malta': 'MT',
         'Marshall Islands': 'MH',
         'Martinique': 'MQ',
         'Mauritania': 'MR',
         'Mauritius': 'MU',
         'Mayotte': 'YT',
         'Mexico': 'MX',
         'Micronesia, Federated States of': 'FM',
         'Moldova, Republic of': 'MD',
         'Monaco': 'MC',
         'Mongolia': 'MN',
         'Montenegro': 'ME',
         'Montserrat': 'MS',
         'Morocco': 'MA',
         'Mozambique': 'MZ',
         'Myanmar': 'MM',
         'Namibia': 'NA',
         'Nauru': 'NR',
         'Nepal': 'NP',
         'Netherlands': 'NL',
         'New Caledonia': 'NC',
         'New Zealand': 'NZ',
         'Nicaragua': 'NI',
         'Niger': 'NE',
         'Nigeria': 'NG',
         'Niue': 'NU',
         'Norfolk Island': 'NF',
         'Northern Mariana Islands': 'MP',
         'Norway': 'NO',
         'Oman': 'OM',
         'Pakistan': 'PK',
         'Palau': 'PW',
         'Palestine, State of': 'PS',
         'Panama': 'PA',
         'Papua New Guinea': 'PG',
         'Paraguay': 'PY',
         'Peru': 'PE',
         'Philippines': 'PH',
         'Pitcairn': 'PN',
         'Poland': 'PL',
         'Portugal': 'PT',
         'Puerto Rico': 'PR',
         'Qatar': 'QA',
         'Romania': 'RO',
         'Russian Federation': 'RU',
         'Rwanda': 'RW',
         'Réunion': 'RE',
         'Saint Barthélemy': 'BL',
         'Saint Helena, Ascension and Tristan da Cunha': 'SH',
         'Saint Kitts and Nevis': 'KN',
         'Saint Lucia': 'LC',
         'Saint Martin (French part)': 'MF',
         'Saint Pierre and Miquelon': 'PM',
         'Saint Vincent and the Grenadines': 'VC',
         'Samoa': 'WS',
         'San Marino': 'SM',
         'Sao Tome and Principe': 'ST',
         'Saudi Arabia': 'SA',
         'Senegal': 'SN',
         'Serbia': 'RS',
         'Seychelles': 'SC',
         'Sierra Leone': 'SL',
         'Singapore': 'SG',
         'Sint Maarten (Dutch part)': 'SX',
         'Slovakia': 'SK',
         'Slovenia': 'SI',
         'Solomon Islands': 'SB',
         'Somalia': 'SO',
         'South Africa': 'ZA',
         'South Georgia and the South Sandwich Islands': 'GS',
         'South Sudan': 'SS',
         'Spain': 'ES',
         'Sri Lanka': 'LK',
         'Sudan': 'SD',
         'Suriname': 'SR',
         'Svalbard and Jan Mayen': 'SJ',
         'Swaziland': 'SZ',
         'Sweden': 'SE',
         'Switzerland': 'CH',
         'Syrian Arab Republic': 'SY',
         'Taiwan, Province of China': 'TW',
         'Tajikistan': 'TJ',
         'Tanzania, United Republic of': 'TZ',
         'Thailand': 'TH',
         'Timor-Leste': 'TL',
         'Togo': 'TG',
         'Tokelau': 'TK',
         'Tonga': 'TO',
         'Trinidad and Tobago': 'TT',
         'Tunisia': 'TN',
         'Turkey': 'TR',
         'Turkmenistan': 'TM',
         'Turks and Caicos Islands': 'TC',
         'Tuvalu': 'TV',
         'Uganda': 'UG',
         'Ukraine': 'UA',
         'United Arab Emirates': 'AE',
         'United Kingdom': 'GB',
         'United States': 'US',
         'United States Minor Outlying Islands': 'UM',
         'Uruguay': 'UY',
         'Uzbekistan': 'UZ',
         'Vanuatu': 'VU',
         'Venezuela, Bolivarian Republic of': 'VE',
         'Viet Nam': 'VN',
         'Virgin Islands, British': 'VG',
         'Virgin Islands, U.S.': 'VI',
         'Wallis and Futuna': 'WF',
         'Western Sahara': 'EH',
         'Yemen': 'YE',
         'Zambia': 'ZM',
         'Zimbabwe': 'ZW',
         'Åland Islands': 'AX'}
    for y in x:
        if country_code in x[y]:
            return y.upper()
log.info("importing bins.")
with open('configs/bins_all.csv', mode='r', encoding='utf-8') as inp:
    reader = csv.reader(inp)
    length = 366388
    current_index = 0
    for x in reader:
        current_index += 1
        text = "\r Now: {0} - Total: {1} - Percent: {2}% ".format(current_index, length, int(round(current_index / length * 100)))
        sys.stdout.write(text)
        sys.stdout.flush()
        x2 = {
            "country": get_iso(x[1]),
            "iso": x[1],
            "flag": x[2],
            "vendor": x[3],
            "type": x[4],
            "level": x[5],
            "bank_name": x[6],
            "prepaid": True if x[5] == "PREPAID" else False
        }
        BINS_DICT[x[0]] = x2


if len(BINS_DICT) < 1:
    log.critical("Bins Not Imported.")
    sys.exit(1)

log.info("imported bins.")
def get_bin_info(bin_to_find: int):
    if str(bin_to_find[:6]) in BINS_DICT:
        xx = BINS_DICT[str(bin_to_find[:6])]
        return xx if not xx['prepaid'] else False
    else:
        return False
def get_bin_info_all(bin_to_find):
    
    if bin_to_find in BINS_DICT:
        xx = BINS_DICT[bin_to_find]
        return xx
    else:
        return False
def checkLuhn(cardNo):
     
    nDigits = len(cardNo)
    nSum = 0
    isSecond = False
     
    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')
     
        if (isSecond == True):
            d = d * 2
  
        # We add two digits to handle
        # cases that make two digits after
        # doubling
        nSum += d // 10
        nSum += d % 10
  
        isSecond = not isSecond
     
    if (nSum % 10 == 0):
        return True
    else:
        return False