from pages.discourse import Discourse
from pages.moderator import Moderator
from pages.mozillians import Mozillians
from pages.reps import Reps
from pages.servicenow_stage import ServiceNowStage
from pages.slack import Slack
from pages.sso_dashboard import SsoDashboard
from pages.standups import Standups
from tests import conftest


class TestLogin:

    def test_login_reps(self, selenium, ldap, urls, counter_api):
        test = Reps(selenium, urls['reps'])
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'],
                                                                   conftest.increase_otp_counter(counter_api)))
        while two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'],
                                                                       conftest.increase_otp_counter(counter_api)))
        assert test.is_logout_button_displayed
        test.click_logout()

    def test_login_slack(self, selenium, ldap, urls, counter_api):
        test = Slack(selenium, urls['slack'])
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'],
                                                                   conftest.increase_otp_counter(counter_api)))
        while two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'],
                                                                       conftest.increase_otp_counter(counter_api)))
        assert test.is_username_displayed
        test.logout()

    def test_login_moderator(self, selenium, ldap, urls, counter_api):
        test = Moderator(selenium, urls['moderator'])
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'],
                                                                   conftest.increase_otp_counter(counter_api)))
        while two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'],
                                                                       conftest.increase_otp_counter(counter_api)))
        assert test.is_logout_button_displayed
        test.click_logout()

    def test_login_standups(self, selenium, ldap, urls, counter_api):
        test = Standups(selenium, urls['standups'])
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'],
                                                                   conftest.increase_otp_counter(counter_api)))
        while two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'],
                                                                       conftest.increase_otp_counter(counter_api)))
        assert test.is_user_menu_displayed
        test.click_logout()

    def test_login_discourse(self, selenium, ldap, urls, counter_api):
        test = Discourse(selenium, urls['discourse'])
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'],
                                                                   conftest.increase_otp_counter(counter_api)))
        while two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'],
                                                                       conftest.increase_otp_counter(counter_api)))
        assert test.is_avatar_displayed
        test.logout()

    def test_login_mozillians(self, selenium, ldap, urls, counter_api):
        test = Mozillians(selenium, urls['mozillians'])
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'],
                                                                   conftest.increase_otp_counter(counter_api)))
        while two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'],
                                                                       conftest.increase_otp_counter(counter_api)))
        assert test.is_username_displayed
        test.click_logout()

    def test_login_sso(self, selenium, ldap, urls, counter_api):
        test = SsoDashboard(selenium, urls['sso_dashboard'])
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'],
                                                                   conftest.increase_otp_counter(counter_api)))
        while two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'],
                                                                       conftest.increase_otp_counter(counter_api)))
        assert test.is_profile_icon_displayed
        test.logout()

    def test_login_servicenow_stage(self, selenium, ldap, urls, counter_api):
        test = ServiceNowStage(selenium, urls['servicenow_stage'])
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'],
                                                                   conftest.increase_otp_counter(counter_api)))
        while two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'],
                                                                       conftest.increase_otp_counter(counter_api)))
        assert test.is_profile_icon_displayed
        test.logout()
