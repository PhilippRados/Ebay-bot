import requests

keyword = "canon pixma pro 10-s"
get_price = requests.get(
    f"https://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SECURITY-APPNAME=PhilippR-sellinga-PRD-3bcdef085-e041a9f7&RESPONSE-DATA-FORMAT=json&GLOBAL-ID=EBAY-DE&keywords={keyword}&REST-PAYLOAD&paginationInput.entriesPerPage=5").json()

price = get_price[
    "findItemsByKeywordsResponse"][0]["searchResult"][0]["item"][1]["sellingStatus"][0]["currentPrice"][0]["__value__"]

entry_count = get_price[
    "findItemsByKeywordsResponse"][0]["searchResult"][0]["@count"]


print(f"The Top 5 {keyword}'s:")

for i in range(int(entry_count)):
    print(i,
          get_price["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"][i]["title"][0]+":",
          get_price["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"][i]["sellingStatus"][0]["currentPrice"][0]["__value__"])
