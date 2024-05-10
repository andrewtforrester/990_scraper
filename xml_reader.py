import xml.etree.ElementTree as ET
import csv

tree = ET.parse('xml/ffa_2022 990.xml')
root = tree.getroot()

def find_element(xml_root, target_tag):
    target = xml_root
    for level in target_tag:
        target = target.find("{http://www.irs.gov/efile}" + level)
    return target.text

cdata = {}

cdata["EIN"] = find_element(root, ["ReturnHeader", "Filer", "EIN"])
cdata["Address"] = find_element(root, ["ReturnHeader", "Filer", "USAddress", "AddressLine1Txt"]).title() + ", " + find_element(root, ["ReturnHeader", "Filer", "USAddress", "CityNm"]).title() + " " + find_element(root, ["ReturnHeader", "Filer", "USAddress", "StateAbbreviationCd"]) + " " + find_element(root, ["ReturnHeader", "Filer", "USAddress", "ZIPCd"])
cdata["Mission Statement"] = find_element(root, ["ReturnData", "IRS990", "ActivityOrMissionDesc"]).lower().capitalize()

cdata["Current Year Revenue"] = find_element(root, ["ReturnData", "IRS990", "CYTotalRevenueAmt"])
cdata["Current Year Expenses"] = find_element(root, ["ReturnData", "IRS990", "CYTotalExpensesAmt"])

cdata["EOY Assets"] = find_element(root, ["ReturnData", "IRS990", "TotalAssetsEOYAmt"])
cdata["EOY Liabilities"] = find_element(root, ["ReturnData", "IRS990", "TotalLiabilitiesEOYAmt"])
cdata["EOY Net Assets"] = find_element(root, ["ReturnData", "IRS990", "NetAssetsOrFundBalancesEOYAmt"])

for line in cdata:
    print(line + ": " + cdata[line])

filename = "sample_output.csv"

with open(filename, 'w', newline='') as csvfile:
	# creating a csv dict writer object
    writer = csv.writer(csvfile, delimiter=",")
    

    writer.writerow([item for item in cdata])
    writer.writerow([cdata[item] for item in cdata])
