from currency_converter import CurrencyConverter

cc = CurrencyConverter()
print(cc.currencies)  # 지원 되는 통화 목록 확인

cc = CurrencyConverter("http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip")
print(cc.convert(1, "USD", "KRW"))
