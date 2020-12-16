# AndroidResourcesTranslator
A python script to translate android language resources.
[Chinese doc](https://github.com/wongzy/AndroidResourcesTranslator/blob/main/README_CN.md)

# Start
1. install googletrans
```pip
pip install googletrans==4.0.0-rc1 --upgrade-strategy only-if-needed
```

> Googletrans is currently having some issues and needs to install version 4.0.0-rc1 to avoid this problem，[py-googletrans](https://github.com/ssut/py-googletrans)

2. Edit **translate_config.json**:

```json
{
  "source_language": "zh-cn",
  "source_path": "/Users/wongzhenyu/Projects/Fukotw/app/src/main/res",
  "files_names": [
    "strings.xml"
  ],
  "translate_languages": [
    "zh-tw",
    "hi",
    "en",
    "es",
    "ar",
    "bn",
    "fr",
    "pt",
    "ms",
    "ru",
    "ja",
    "pa",
    "te"
  ]
}
```

source_language: Languages that need to be translated
source_path: The directory where the resource files are located
files_names: List of files to be translated
translate_languages：Languages in need of translation

3. Run main.py

# supported language

All supported languages with codes:

language | code |
 --- | --- |
afrikaans | af |
albanian | sq |
amharic |am|
arabic |ar|
armenian |hy|
azerbaijani |az|
basque |eu|
belarusian |be|
bengali |bn|
bosnian |bs|
bulgarian |bg|
catalan |ca|
cebuano |ceb|
chichewa |ny|
chinese(simplified) |zh-cn|
chinese(traditional) |zh-tw|
corsican |co|
croatian |hr|
czech |cs|
danish |da|
dutch |nl|
english |en|
esperanto |eo|
estonian |et|
filipino |tl|
finnish |fi|
french |fr|
frisian |fy|
galician |gl|
georgian |ka|
german |de|
greek |el|
gujarati |gu|
haitian creole |ht|
hausa |ha|
hawaiian |haw|
hebrew |iw|
hindi |hi|
hmong |hmn|
hungarian |hu|
icelandic |is|
igbo |ig|
indonesian |id|
irish |ga|
italian |it|
japanese |ja|
javanese |jw|
kannada |kn|
kazakh |kk|
khmer |km|
korean |ko|
kurdish (kurmanji) |ku|
kyrgyz |ky|
lao |lo|
latin |la|
latvian |lv|
lithuanian |lt|
luxembourgish |lb|
macedonian |mk|
malagasy |mg|
malay |ms|
malayalam |ml|
maltese |mt|
maori |mi|
marathi |mr|
mongolian |mn|
myanmar (burmese) |my|
nepali |ne|
norwegian |no|
pashto |ps|
persian |fa|
polish |pl|
portuguese |pt|
punjabi |pa|
romanian |ro|
russian |ru|
samoan |sm|
scots gaelic |gd|
serbian |sr|
sesotho |st|
shona |sn|
sindhi |sd|
sinhala |si|
slovak |sk|
slovenian |sl|
somali |so|
spanish |es|
sundanese |su|
swahili |sw|
swedish |sv|
tajik |tg|
tamil |ta|
telugu |te|
thai |th|
turkish |tr|
ukrainian |uk|
urdu |ur|
uzbek |uz|
vietnamese |vi|
welsh |cy|
xhosa |xh|
yiddish |yi|
yoruba |yo|
zulu |zu|
Filipino |fil|
Hebrew |he|
