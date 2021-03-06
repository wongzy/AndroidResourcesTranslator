# AndroidResourcesTranslator

一个用来翻译Android资源的python脚本

# 使用方法：
1. 安装googletrans
```pip
pip install googletrans==4.0.0-rc1 --upgrade-strategy only-if-needed
```

> googletrans 目前有些问题，需要安装4.0.0-rc1版本问题才不会出现，可见[py-googletrans](https://github.com/ssut/py-googletrans)

2. 编辑**translate_config.json**:

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

source_language: 需要被翻译的语言
source_path: 资源文件所在目录
files_names: 需要翻译的文件列表
translate_languages：需要翻译的语言

3. 运行main.py


# supported language

所有支持的语言及他们的代码：

语言 | 代码 |
 --- | --- |
南非荷兰语|af|
阿尔巴尼亚|sq|
阿姆哈拉语|am|
阿拉伯语|ar|
亚美尼亚|hy|
阿塞拜疆|az|
巴斯克|eu|
白俄罗斯|be|
孟加拉|bn|
波斯尼亚|bs|
保加利亚|bg|
加泰罗尼亚语|ca|
宿务语 |ceb|
齐佩瓦语|ny|
中文(简体)|zh-cn|
中文(繁体)|zh-tw|
科西嘉|co|
克罗地亚|hr|
捷克|cs|
丹麦|da|
荷兰|nl|
英语|en|
世界语|eo|
爱沙尼亚|et|
菲律宾|tl|
芬兰|fi|
法语|fr|
弗里斯兰语|fy|
加利西亚|gl|
格鲁吉亚|ka|
德国|de|
希腊|el|
古吉拉特语|gu|
海地克里奥尔语|ht|
豪萨语|ha|
夏威夷|haw|
希伯来语|iw|
印地语|hi|
苗族|hmn|
匈牙利|hu|
冰岛|is|
伊博|ig|
印尼|id|
爱尔兰|ga|
意大利|it|
日本|ja|
爪哇|jw|
埃纳德语|kn|
哈萨克斯坦|乐|
红色|公里|
韩国|ko|
库尔德语(土耳其) |ku|
吉尔吉斯|ky|
老挝|lo|
拉丁语|la|
拉脱维亚|lv|
立陶宛|lt|
卢森堡语|lb|
马其顿|mk|
马达加斯加|mg|
马来语|ms|
马拉雅拉姆语|ml|
马耳他|mt|
毛利|mi|
马拉地语|mr|
蒙古|mn|
缅甸|my|
尼泊尔|ne|
挪威|no|
普什图语|ps|
波斯|fa|
波兰|pl|
葡萄牙|pt|
旁遮普|pa|
罗马尼亚|ro|
俄罗斯|ru|
萨摩亚|sm|
苏格兰盖尔语|gd|
塞尔维亚|sr|
塞索托语|st|
修纳|sn|
信德语|sd|
僧伽罗语|si|
斯洛伐克|sk|
斯洛文尼亚|sl|
索马里|so|
西班牙语|es|
巽他语|su|
斯瓦希里语|sw|
瑞典|sv|
塔吉克族|tg|
泰米尔语|ta|
泰卢固语|te|
泰国|th|
土耳其|tr|
乌克兰|uk|
乌尔都语|ur|
乌兹别克斯坦|uz|
越南|vi|
威尔士|cy|
科萨|xh|
意第绪语|yi|
约鲁巴|yo|
祖鲁语|zu|
菲律宾|fil|
希伯来语|he|