import xml.etree.ElementTree as ET

tree = ET.parse('xml/safechild 990_FY2021.xml')
root = tree.getroot()

def find_element(xml_root, target_tag):
    target = xml_root
    for level in target_tag:
        target = target.find("{http://www.irs.gov/efile}" + level)
    return target.text

data = {}

data["EIN"] = find_element(root, ["ReturnHeader", "Filer", "EIN"])
data["Address"] = find_element(root, ["ReturnHeader", "Filer", "USAddress", "AddressLine1Txt"]) + ", " + find_element(root, ["ReturnHeader", "Filer", "USAddress", "CityNm"]) + " " + find_element(root, ["ReturnHeader", "Filer", "USAddress", "StateAbbreviationCd"]) + " " + find_element(root, ["ReturnHeader", "Filer", "USAddress", "ZIPCd"])
data["Mission Statement"] = find_element(root, ["ReturnData", "IRS990", "ActivityOrMissionDesc"])

for line in data:
    print(line + ": " + data[line])
