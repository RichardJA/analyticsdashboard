import mailchimp
import requests

def google_grants_stats():
    pass


def google_paid_stats():
    pass


def mailchimp_stats():
    print('Loading in Secret Keys')
    try:
        username = open('secret_mailchimp_username.txt').read()
        apikey = open('secret_mailchimp_key.txt').read()
        split_test = apikey.split('-')
    except Exception as exc:
        print('Error downloading files.\n' + str(exc))
        input('Press any key to exit...')
        sys.exit()

    print('Checking API Key is correctly formatted for MailChimp')
    if len(split_test) != 2:
        print(apikey)
        print('This doesn\'t look like your API Key is formatted correctly: ' + apikey)
        input('Press any key to exit...')
        sys.exit()

    data_center = split_test[1]
    apiurl = "https://" + data_center + ".api.mailchimp.com/3.0/"
    print('API Key looks correct. Attempting to connect to MailChimp API: ' + data_center)
    connection_info = [username, apikey, apiurl]

    # declaring which fields I want in my list
    sends_params = {'fields': 'reports.campaign_title,reports.subject_line,reports.'
                              'emails_sent,reports.opens.unique_opens,reports.opens.open_rate'}
    lists_params = {'fields': 'lists.id,lists.name,lists.stats.member_count'}

    # This downloads the email reports & lists
    email_sends = requests.get(connection_info[2] + 'reports', auth=(connection_info[0], connection_info[1]), params=sends_params).json()
    email_lists = requests.get(connection_info[2] + 'lists?count=100', auth=(connection_info[0], connection_info[1]), params=lists_params).json()

    list_dict = {}
    for lists in email_lists['lists']:
        list_dict[lists['name']] = lists['stats']['member_count']

    for sends in email_sends['reports']:
        # need to create email items. It might be worth moving this into the main file so that I don't need two sub items for email
        print(sends)



def facebook_stats():
    pass


def twitter_stats():
    pass


def analytics_stats():
    pass


def display_results():
    pass


def start_web_scrape():
    pass


def main():
    """
    Starts the program.
    """
    # The first iteration of this function is completed outside of the loop as the home page is hard coded.
    # After the first iteration, the variable changes to "current_url" and can then be looped
    print('Starting Analysis...')
    mailchimp_stats()
    pass

if __name__ == '__main__':
    main()
