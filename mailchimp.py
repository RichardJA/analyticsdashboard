import sys
import requests

# TODO: Add in Several elements to the MailChimp call as currently they're populated by "1"


def get_keys():
    """
    Checks the username, api key and that the api key is formatted correctly with the data center at the end
    Returns the relevant parts needed for the api call
    Quits the system if there are any errors
    """
    try:
        username = open('secret_mailchimp_username.txt').read()
        apikey = open('secret_mailchimp_key.txt').read()
        split_test = apikey.split('-')
    except Exception as exc:
        print('Error downloading files.\n' + str(exc))
        input('Press ENTER key to exit...')
        sys.exit()

    # Checking that there is two parts to the api key
    # This should be the case due to the way it is formatted with a dash

    if len(split_test) != 2:
        print(apikey)
        print('This doesn\'t look like your API Key is formatted correctly: ' + apikey)
        input('Press ENTER key to exit...')
        sys.exit()

    # Return the relevant information
    # split_test[1] now contains the "data center" that MailChimp stores our info on
    return [username, apikey, split_test[1]]


def open_connection(login_info):
    """
    Login info should contain the username, apikey and data center
    This function should open the connection, send the desired parameters and return that information
    """
    # Creates the API url with the relevant data center and stores it in the url
    # conn = the connection information required
    apiurl = "https://" + login_info[2] + ".api.mailchimp.com/3.0/"
    conn = [login_info[0], login_info[1], apiurl]

    # Declares which fields I want in my list
    send_fields = 'reports.campaign_title,reports.subject_line,reports.' \
                  'emails_sent,reports.opens.unique_opens,reports.opens.open_rate'
    list_fields = 'lists.id,lists.name,lists.stats.member_count'

    sends_params = {'fields': send_fields}
    lists_params = {'fields': list_fields}

    # This downloads the email reports & lists.
    # mc_sends are the actual emails & mc_lists are the MailChimp lists
    mc_lists = requests.get(conn[2] + 'lists?count=75', auth=(conn[0], conn[1]), params=lists_params).json()
    mc_sends = requests.get(conn[2] + 'reports', auth=(conn[0], conn[1]), params=sends_params).json()

    return [mc_lists, mc_sends]


def get_lists(mc_lists):
    """
    Pulls out the MailChimp list information and returns the dictionary
    """
    list_dict = {}
    for lists in mc_lists['lists']:
        list_dict[lists['name']] = lists['stats']['member_count']

    return list_dict


def get_emails(mc_emails):
    """
    Pulls out the MailChimp emails sent and returns a list
    """
    emails = []
    for sends in mc_emails['reports']:
        email = Email([sends['campaign_title'], sends['subject_line'], 1, sends['emails_sent'], sends['opens']
                            ['unique_opens'], sends['opens']['open_rate'], 1, 1])
        emails.append(email)

    return emails


class Email(object):
    def __init__(self, email):
        self.campaign_name = email[0]
        self.subject_line = email[1]
        self.list_name = email[2]
        self.total_recipients = email[3]
        self.unique_opens = email[4]
        self.open_rate = email[5]
        self.unique_clicks = email[6]
        self.click_rate = email[7]

    def print_emails(self):
        print("Campaign Name: " + str(self.campaign_name))
        print("Subject Line: " + str(self.subject_line))
        print("List Name: " + str(self.list_name))
        print("Total Recipients: "+ str(self.total_recipients))
        print("Unique Opens: " + str(self.unique_opens))
        print("Open Rate: " + str(self.open_rate))
        print("Unique Clicks: " + str(self.unique_clicks))
        print("Click Rate: " + str(self.click_rate))
