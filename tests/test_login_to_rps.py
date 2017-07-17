from pages.moderator import Moderator
from pages.reps import Reps
from pages.slack import Slack
from tests import conftest


class TestLogin:

    def test_login_reps(self, selenium, ldap, urls):
        test = Reps(selenium, urls['reps'])
        test.login_with_ldap(ldap['email'], ldap['password'], conftest.passcode(ldap['secret_seed']))
        assert test.is_logout_button_displayed
        test.click_logout()

    def test_login_slack(self, selenium, ldap, urls):
        test = Slack(selenium, urls['slack'])
        test.login_with_ldap(ldap['email'], ldap['password'], conftest.passcode(ldap['secret_seed']))
        assert test.is_username_displayed
        test.logout()

    def test_login_moderator(self, selenium, ldap, urls):
        test = Moderator(selenium, urls['moderator'])
        test.login_with_ldap(ldap['email'], ldap['password'], conftest.passcode(ldap['secret_seed']))
        assert test.is_logout_button_displayed
        test.click_logout()
