from pages.moderator import Moderator
from pages.reps import Reps
from pages.slack import Slack
from tests import conftest


class TestLogin:

    def test_login_reps(self, selenium, ldap, urls):
        test = Reps(selenium, urls['reps'])
        counter = int(conftest.file_content("index"))
        test.login_with_ldap(ldap['email'], ldap['password'], conftest.passcode(ldap['secret_seed'], counter))
        conftest.write_in_file("index", counter + 1)
        assert test.is_logout_button_displayed
        test.click_logout()

    def test_login_slack(self, selenium, ldap, urls):
        test = Slack(selenium, urls['slack'])
        counter = int(conftest.file_content("index"))
        test.login_with_ldap(ldap['email'], ldap['password'], conftest.passcode(ldap['secret_seed'], counter))
        conftest.write_in_file("index", counter + 1)
        assert test.is_username_displayed
        test.logout()

    def test_login_moderator(self, selenium, ldap, urls):
        test = Moderator(selenium, urls['moderator'])
        counter = int(conftest.file_content("index"))
        test.login_with_ldap(ldap['email'], ldap['password'], conftest.passcode(ldap['secret_seed'], counter))
        conftest.write_in_file("index", counter + 1)
        assert test.is_logout_button_displayed
        test.click_logout()
