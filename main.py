# Import flask and datetime module for showing date and time
from flask import Flask

import os
import numpy as np
from azure.core.exceptions import ResourceExistsError
from azure.storage.blob import BlobServiceClient, ContainerClient, ContentSettings

import matplotlib.pyplot as plt
import pandas as pd

STORAGEACCOUNTURL = "https://milantisdevsa.blob.core.windows.net."
STORAGEACCOUNTKEY = "gR7Au8+eBHDiSwClRfwRVSZPvSeIAohEHWAHOmqUxoL6WjEd9IP7Cs088wPRPRPiyQ5CBfCG1QCw+ASt0uWDgg=="
LOCALFILENAME = "rishi.txt"
CONTAINERNAME = "user"
BLOBNAME = "User_Company_Date.xlsx"
# get file from container
blob_service_client_instance = BlobServiceClient(account_url=STORAGEACCOUNTURL, credential=STORAGEACCOUNTKEY)
blob_client_instance = blob_service_client_instance.get_blob_client(CONTAINERNAME, BLOBNAME, snapshot=None)
with open(LOCALFILENAME, "wb") as my_blob:
    blob_data = blob_client_instance.download_blob()
    blob_data.readinto(my_blob)

dfbd = pd.read_excel(LOCALFILENAME)
dfbd2 = dfbd.fillna(0)
arr = dfbd2.to_numpy()
vendors = dfbd2[dfbd2.columns[0:1]].to_numpy()
terms = dfbd2[dfbd2.columns[dfbd2.columns.size - 1:dfbd2.columns.size]].to_numpy()
size = dfbd2.columns.size - 1

# create data
head = ["col1", "col2", "col3"]
value = [[1, 2, 3], [4, 5, 6], [8, 7, 9]]
df = pd.DataFrame(value, columns=head)
output = df.to_csv(index=False, encoding="utf-8")

print(output)

connection_string = 'DefaultEndpointsProtocol=https;AccountName=milantisdevsa;AccountKey=gR7Au8+eBHDiSwClRfwRVSZPvSeIAohEHWAHOmqUxoL6WjEd9IP7Cs088wPRPRPiyQ5CBfCG1QCw+ASt0uWDgg==;EndpointSuffix=core.windows.net'
# Instantiate a new BlobServiceClient using a connection string
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
# Instantiate a new ContainerClient
container_client = blob_service_client.get_container_client('user')
try:
    # Create new Container in the service
    container_client.create_container()
    properties = container_client.get_container_properties()
except ResourceExistsError:
    print("Container already exists.")

# Instantiate a new BlobClient
# blob_client = container_client.get_blob_client("output.csv")
# upload data
# blob_client.upload_blob(output, blob_type="BlockBlob")

CONNECT_STR = os.getenv(
    'DefaultEndpointsProtocol=https;AccountName=milantisdevsa;AccountKey=gR7Au8+eBHDiSwClRfwRVSZPvSeIAohEHWAHOmqUxoL6WjEd9IP7Cs088wPRPRPiyQ5CBfCG1QCw+ASt0uWDgg==;EndpointSuffix=core.windows.net')
CONTAINER_NAME = os.getenv('user')

# Instantiate a ContainerClient. This is used when uploading a blob from your local file.
container_client = ContainerClient.from_connection_string(
    conn_str='DefaultEndpointsProtocol=https;AccountName=milantisdevsa;AccountKey=gR7Au8+eBHDiSwClRfwRVSZPvSeIAohEHWAHOmqUxoL6WjEd9IP7Cs088wPRPRPiyQ5CBfCG1QCw+ASt0uWDgg==;EndpointSuffix=core.windows.net',
    container_name='user'
)

# This is an optional setting for guaranteeing the MIME type to be always jpeg.
content_setting = ContentSettings(
    content_type='image/png',
    # content_encoding=None,
    # content_language=None,
    # content_disposition=None,
    # cache_control=None,
    # content_md5=None
)

# categories
scheduling = np.array(
    ["Calendly", "Acuity Schedulin", "Wrike", "Depty", "7shifts", "10to8 Limited", "Setmore", "Appointy",
     "Google Calendar", "StormCource LLC", "QuickBooks", "Square Appointments", "Mindbody", "Smartsheet",
     "Google Workspace", "Clockify", "Paycor", "Asana"])
sales = np.array(
    ["LAMBDA SOLUTIONS", "IRONMARK INC", "INTERCOM INC.", "HUBSPOT, INC.", "DYNADOT", "Creative Minds",
     "CopyTalk, LLC",
     "DOMAINS PRICED RIGHT - 101 domain", "THIRD AND GROVE LLC", "UNBOUNE", "Typeform", "VERIZON", "WISTIA, INC.",
     "VISUAL IMPACT", "ZENDESK", "Best Buy", "B&H Photo", "Salesforce", "Pipedrive", "HubSpot", "Zoho Corporation",
     "Salesloft", "Zendesk", "Freshsales", "Keap",
     "Insightly", "ActiveCampaign", "Nutshell", "PandaDoc", "LinkedIn", "Salesflare Freshworks", "Salesmate CRM",
     "Showpad", "ClearSlide", "Oracle", "MarketXpander Services Private Limited", "VanillaSoft",
     "Microsoft Corporation", "EngageBay Inc", "Beaver Builder"])
crm = np.array(
    ["KEAP", "ZAPIER", "Pipedrive", "Salesforce", "HubSpot", "ZOHO CORPORATION", "SugarCRM", "Insightly",
     "Nutshell",
     "Capsule", "Really Simple Systems", "Agile CRM Inc.", "NetSuite", "Freshworks", "Creatio",
     "Less Annoying CRM", "American Solutions for Business", "Streak", "Nimble", "Apptivo", "Microsoft Corporation",
     "Agile CRM", "ActiveCampaign",
     "SuiteCRM"])
project_management = np.array(
    ["LMS IMPLEMENTATION", "ENTERPRISE REPORTING - HOSTING", "ENTERPRISE REPORTING - SUPPORT", "Codekeeper",
     "SURVEY MONKEY", "THE FRANCHISE BUILDERS BRANDS", "Wrike", "Asana", "Trello", "ClickUp", "Microsoft Project",
     "Smartsheet", "Airtable", "Jira", "Zoho Projects",
     "Basecamp", "LiquidPlanner", "Workfront", "Notion", "Task management", "ProofHub", "GanttPRO", "Podio",
     "Freedcamp", "Celoxis Technologies Pvt. Ltd.", "Easy Projects", "Todoist", "Scoro",
     "Hive Design and Build LLC",
     "TeamGantt", "Ariba, Inc."])
productivity = np.array(
    ["Lucid Software", "LINKEDIN CORPORATION", "Liberated Syndication", "LearnUpon", "KANON SAPP VIRTUAL ASSISTANT",
     "Jelly Comb", "INCITE AUTOMATION LLC", "Hootsuite", "Graphly", "GOTO MEETING", "GoDaddy", "Sonix.Ai",
     "Techsmith",
     "Visme", "VIMEO", "WORKZONE, LLC", "WP Search", "XMIND", "ZOOM INFORMATION, INC.",
     "ZOOM VIDEO COMMUNICATIONS INC.", "Slack", "Articulate Global, Inc.", "Microsoft Teams", "Trello",
     "Bee by Mailup",
     "Flock", "Workplace", "Notion", "Freeware", "Wimi", "Confluence",
     "Microsoft Office", "Google Suite", "Adobe", "Docusign", "Microsoft Teams", "Microsoft Visio", "Zoom",
     "AudioAcrobat"])
cloud = np.array(
    ["LOGMEIN USA, INC", "Linode.com", "GOOGLE APPS", "GOOGLE MAPS API", "CORNERSTONE OnDEMAND, INC.", "TELESYSTEM",
     "Dropbox", "Amazon", "Microsoft Azure", "Google Cloud", "Google Drive", "Salesforce", "Amazon Web Services",
     "Adobe Creative Cloud", "Adobe Inc." "Google Workspace", "Oracle", "DigitalOcean", "Box", "IBM Cloud",
     "Alibaba Cloud", "Microsoft 365", "HubSpot", "Mailchimp", "Zendesk", "AWS Lambda", "Trello",
     "SlideRocket"])
accounting = np.array(
    ["IRON MOUNTAIN", "CONCUR TECHNOLOGIES, INC", "VISUAL ROI", "Xero", "Authorize.net", "QuickBooks", "FreshBooks",
     "Wave", "Zoho Corporation", "NetSuite", "Sage Group", "Sage Intacct",
     "Sage 50", "FreeAgent", "GnuCash", "ZipBooks", "Acclivity Group LLC", "Tipalti", "Intuit", "AvidXchange",
     "Tally",
     "Paychex", "Odoo", "Gusto", "Microsoft Dynamics NAV", "ClearBooks", "Melio", "ZarMoney"])
shipping = np.array(["FEDERAL EXPRESS", "Shopify", "Mimeo", "Fedex", "UPS", "USPS", "ShipBob", "ShipMonk"])
hr = np.array(
    ["LICENSE MANAGEMENT SOFTWARE", "GROSS, MENDELSOHN & ASSOCIATES", "STERLING INFOSYSTEMS, INC.", "BAMBOO HR",
     "Zenefits", "Namely", "ADP", "Workday", "Paycom", "Gusto", "Paycor", "SAP SuccessFactors", "Rippling",
     "Paylocity", "Applicant tracking system", "Zoho Corporation", "Sage Group", "Ceridian Dayforce Corporation",
     "OrangeHRM", "Deel", "Freshteam", "Deputy", "Cezanne HR Limited", "TriNet", "Cornerstone OnDemand", "15Five",
     "CakeHR"])

# implementation
# services
# support
# hardware - sever, workstation
# server - backup, office supplies, security services

scheduling_array = []
sales_array = []
crm_array = []
project_management_array = []
productivity_array = []
cloud_array = []
accounting_array = []
shipping_array = []
hr_array = []

# sum calculator
for i in range(len(vendors)):
    for j in range(size):
        test_list = arr[i][1:size]
        sum = 0.00
        for k in test_list:
            sum += k
    # print(arr[i][0] + "," + "$" + str(round(sum,2)))

def categorization_process(category, name, append_array):
    for i in range(vendors.size):
        for j in range(category.size):
            if vendors[i].__contains__(category[j]):
                append_array.append(vendors[i])
    return (str("$") + str(append_array))

list_table = pd.DataFrame()
list_table['Vendors'] = ["Scheduling", "Sales", "CRM", "Project Management", "Productivity", "Cloud", "Accounting",
                         "Shipping", "HR"]
list_table['Sum'] = [categorization_process(scheduling, "scheduling ", scheduling_array),
                     categorization_process(sales, "sales ", sales_array),
                     categorization_process(crm, "CRM ", crm_array),
                     categorization_process(project_management, "project management ", project_management_array),
                     categorization_process(productivity, "productivity ", productivity_array),
                     categorization_process(cloud, "cloud ", cloud_array),
                     categorization_process(accounting, "accounting ", accounting_array),
                     categorization_process(shipping, "shipping ", shipping_array),
                     categorization_process(hr, "HR ", hr_array)]
df_styled = list_table.style.background_gradient()  # adding a gradient based on values in cell

def categories_sum(array_argument):
    # sum calculator
    temp_categories_array = []
    sum_final_categories_array = []
    for i in range(len(array_argument)):
        itemindex = np.where(vendors == array_argument[i])[0][0]
        for j in range(10):
            test_list = arr[itemindex][1:10]
            sum = 0.00
            for k in test_list:
                sum += k
        temp_categories_array.append(round(sum, 2))

    result = 0.00

    for q in range(len(temp_categories_array)):
        result = result + temp_categories_array[q]
    sum_final_categories_array.append(result)

    return round(result, 2)

def singular_breakdown(argument):
    temp_categories_array = []
    sum_final_categories_array = []
    for i in range(len(argument)):
        itemindex = np.where(vendors == argument[i])[0][0]
        for j in range(10):
            test_list = arr[itemindex][1:10]
            sum = 0.00
            for k in test_list:
                sum += k
        temp_categories_array.append(round(sum, 2))

    for q in range(len(temp_categories_array)):
        print(*argument[q] + "," + "$" + str(temp_categories_array[q]))

category_table = pd.DataFrame()
category_table['Vendors'] = ["Scheduling", "Sales", "CRM", "Project Management", "Productivity", "Cloud",
                             "Accounting",
                             "Shipping", "HR"]
category_table['Sum'] = [categories_sum(scheduling_array), categories_sum(sales_array), categories_sum(crm_array),
                         categories_sum(project_management_array), categories_sum(productivity_array),
                         categories_sum(cloud_array), categories_sum(accounting_array),
                         categories_sum(shipping_array),
                         categories_sum(hr_array)]
# df_styled1 = category_table.style.background_gradient()  # adding a gradient based on values in cell
category_table.style.background_gradient().export()

input_file_path = "categorytable.png"
output_blob_name = "categorytable.png"

# This is an optional setting for guaranteeing the MIME type to be always jpeg.
content_setting = ContentSettings(
    content_type='image/png',
    # content_encoding=None,
    # content_language=None,
    # content_disposition=None,
    # cache_control=None,
    # content_md5=None
)

# Upload file
with open(input_file_path, "rb") as data:
    container_client.upload_blob(
        name=output_blob_name,
        data=data,
        content_settings=content_setting)

# Check the result
all_blobs = container_client.list_blobs(name_starts_with="BLOB_PIC", include=None)
for each in all_blobs:
    print("RES: ", each)

def sum_sort(argument):
    temp_categories_array = []
    sum_final_categories_array = []
    for i in range(len(argument)):
        itemindex = np.where(vendors == argument[i])[0][0]
        for j in range(10):
            test_list = arr[itemindex][1:10]
            sum = 0.00
            for k in test_list:
                sum += k
            temp_categories_array.append(round(sum, 2))
    index = np.argmin(temp_categories_array)

    return ((temp_categories_array[index]))

def vendors_sort(argument):
    temp_categories_array = []
    sum_final_categories_array = []
    for i in range(len(argument)):
        itemindex = np.where(vendors == argument[i])[0][0]
        for j in range(10):
            test_list = arr[itemindex][1:10]
            sum = 0.00
            for k in test_list:
                sum += k
        temp_categories_array.append(round(sum, 2))
    index = np.argmin(temp_categories_array)

    return (argument[index])

pie_array = np.array([categories_sum(sales_array), categories_sum(scheduling_array), categories_sum(crm_array),
                      categories_sum(project_management_array), categories_sum(productivity_array),
                      categories_sum(cloud_array), categories_sum(accounting_array), categories_sum(shipping_array),
                      categories_sum(hr_array)])
mylables = ["Sales", "Scheduling", "CRM", "Project Management", "Productivity", "Cloud", "Accounting", "Shipping",
            "HR"]
myexplode = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
plt.pie(pie_array, labels=mylables, startangle=90, autopct='%1.2f%%', radius=1)
plt.savefig("plot.png", bbox_inches='tight')

input_file_path = "plot.png"
output_blob_name = "plot.png"

# Upload file
with open(input_file_path, "rb") as data:
    container_client.upload_blob(
        name=output_blob_name,
        data=data,
        content_settings=content_setting)

# Check the result
all_blobs = container_client.list_blobs(name_starts_with="BLOB_PIC", include=None)
for each in all_blobs:
    print("RES: ", each)

final_table = pd.DataFrame()
final_table['Vendors'] = [*vendors_sort(sales_array), *vendors_sort(crm_array),
                          *vendors_sort(project_management_array),
                          *vendors_sort(productivity_array), *vendors_sort(cloud_array),
                          *vendors_sort(accounting_array), *vendors_sort(shipping_array), *vendors_sort(hr_array)]
final_table['Sum'] = [sum_sort(sales_array), sum_sort(crm_array), sum_sort(project_management_array),
                      sum_sort(productivity_array), sum_sort(cloud_array), sum_sort(accounting_array),
                      sum_sort(shipping_array), sum_sort(hr_array)]
# df_styled2 =
final_table.style.background_gradient().export()  # adding a gradient based on values in cell
# dfi.export(
#    df_styled2,
#    'final_table.png',
#    table_conversion="matplotlib"
# )

input_file_path = "final_table.png"
output_blob_name = "final_table.png"

# Upload file
with open(input_file_path, "rb") as data:
    container_client.upload_blob(
        name=output_blob_name,
        data=data,
        content_settings=content_setting)

# Check the result
all_blobs = container_client.list_blobs(name_starts_with="BLOB_PIC", include=None)
for each in all_blobs:
    print("RES: ", each)

def terms_calc(argument):
    sum = 0.00
    for i in range(len(terms)):
        if terms[i] == 'Y':
            sum = categories_sum(argument)
        elif terms[i] == 'M':
            sum = (categories_sum(argument) * 9.0) / 12.0
        elif terms[i] == 'A':
            sum = categories_sum(argument)
        elif terms[i] == 'B':
            sum = categories_sum(argument) * 2.0
    return sum

forecast_table = pd.DataFrame()
forecast_table['Vendors'] = [*vendors_sort(sales_array), *vendors_sort(crm_array),
                             *vendors_sort(project_management_array), *vendors_sort(productivity_array),
                             *vendors_sort(cloud_array), *vendors_sort(accounting_array),
                             *vendors_sort(shipping_array),
                             *vendors_sort(hr_array)]
forecast_table['Forecast'] = [categories_sum(sales_array) * 12.0, categories_sum(crm_array)* 12.0, categories_sum(project_management_array)* 12.0,
                              categories_sum(productivity_array)* 12.0, categories_sum(cloud_array)* 12.0, categories_sum(accounting_array)* 12.0,
                              categories_sum(shipping_array)* 12.0, categories_sum(hr_array)* 12.0]
# df_styled3 = \
forecast_table.style.background_gradient().export()  # adding a gradient based on values in cell
# dfi.export(
#    df_styled1,
#    'forecast_table.png',
#    table_conversion="matplotlib"
# )

input_file_path = "forecast_table.png"
output_blob_name = "forecast_table.png"

# Upload file
with open(input_file_path, "rb") as data:
    container_client.upload_blob(
        name=output_blob_name,
        data=data,
        content_settings=content_setting)

# Check the result
all_blobs = container_client.list_blobs(name_starts_with="BLOB_PIC", include=None)
for each in all_blobs:
    print("RES: ", each)



