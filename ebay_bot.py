import requests
from testing_api import username, pw, receiver_ebay
import smtplib


class Search_Ebay:
    def __init__(self, keyword):
        self.keyword = keyword

        # I cut out my APP-ID so you have to use your own
        try:
            self.get_price = requests.get(
                f"https://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SECURITY-APPNAME=PhilippR-sellinga-PRD-3bcdef085-e041a9f7&RESPONSE-DATA-FORMAT=json&GLOBAL-ID=EBAY-DE&keywords={self.keyword}&REST-PAYLOAD&paginationInput.entriesPerPage=5").json()
        except:
            print("Connection to API failed")

        self.entry_count = self.get_price[
            "findItemsByKeywordsResponse"][0]["searchResult"][0]["@count"]

    def getting_top_5(self):
        self.entry_count = self.get_price[
            "findItemsByKeywordsResponse"][0]["searchResult"][0]["@count"]

        print(f"The Top 5 {self.keyword}'s:")

        for i in range(int(self.entry_count)):
            print(i,
                  self.get_price["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"][i]["title"][0]+":",
                  self.get_price["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"][i]["sellingStatus"][0]["currentPrice"][0]["__value__"])

    def send_mail(self, sender, receiver, threshhold):
        list_of_prices = []

        for i in range(int(self.entry_count)):
            list_of_prices.append(self.get_price["findItemsByKeywordsResponse"][0]["searchResult"]
                                  [0]["item"][i]["sellingStatus"][0]["currentPrice"][0]["__value__"])

        for i, price in enumerate(list_of_prices):
            if float(price) <= threshhold:
                print(
                    f'We have found a match: {self.get_price["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"][i]["viewItemURL"][0]}')
                # Logic for sending Email

                server = smtplib.SMTP("smtp.gmail.com", port=587)
                server.ehlo_or_helo_if_needed()
                server.starttls()
                server.ehlo_or_helo_if_needed()

                server.login(sender, pw)
                print("login worked")

                subject = "Ebay-Suche erfolgreich"

                message = f'Subject:{subject}\n\nDer {self.keyword} kostet nur {float(price)}€. Hier ist der Link:\n{self.get_price["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"][i]["viewItemURL"][0]}'\
                    .encode()

                server.sendmail(
                    sender, receiver, message)

                server.quit()
            else:
                print("No match found")


drucker = Search_Ebay("canon pixma pro 10-s")
drucker.send_mail(username, receiver_ebay, 250)

# Jeden Tag um 20:00 läuft das Programm über den Aufgabenplaner
