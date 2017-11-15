from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import mailchimp
import analytics

emails = []
analytics_report = ""


# This is the Google AdWords Section of the code #
def google_grants_stats():
    print('Starting Google Adwords Grants API Call')
    pass


def google_paid_stats():
    print('Starting Google AdWords Paid API Call')
    pass


# This is the MailChimp Section of the code #
def mailchimp_control():
    """
    This function calls the MailChimp API and pulls the stats for both the lists and the emails
    It stores the email stats in a list of emails called "email" and the list info in a dictionary called "list_dict"
    """
    print('Starting MailChimp API Call')
    mc_login_info = mailchimp.get_keys()
    mc_data = mailchimp.open_connection(mc_login_info)

    mc_lists = mc_data[0]
    mc_emails = mc_data[1]

    mc_lists = mailchimp.get_lists(mc_lists)
    emails[:] = mailchimp.get_emails(mc_emails)
    return [mc_lists, mc_emails]

# This is the Facebook Section of the code #
def facebook_stats():
    print('Starting Facebook API Call')
    pass


# This is the Twitter Section of the code #
def twitter_stats():
    print('Starting Twitter API Call')
    pass


# This is the Google Analytics Section of the code #
def ga_control():
    print('Starting Google Analytics API Call')
    connection_info = analytics.get_keys()
    report_info = analytics.create_service_object(connection_info)


# This is the Web Scrape Section of the code #


def start_web_scrape():
    pass


def display_results():
    pass


def main():
    """
    Starts the program.
    """
    # The first iteration of this function is completed outside of the loop as the home page is hard coded.
    # After the first iteration, the variable changes to "current_url" and can then be looped
    print('Starting Analysis...')
    mc_data = mailchimp_control()
    ga_control()

    pass

if __name__ == '__main__':
    main()
