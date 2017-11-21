import pytest

from pages.biztera import Biztera
from pages.discourse import Discourse
from pages.greenhouse import Greenhouse
from pages.mana import Mana
from pages.moderator import Moderator
from pages.mozdatacollective import MozDataCollective
from pages.mozillians import Mozillians
from pages.phonebook import Phonebook
from pages.reps import Reps
from pages.selfservice_mig import SelfServiceMig
from pages.servicenow import ServiceNow
from pages.slack import Slack
from pages.smartsheet import Smartsheet
from pages.sso_dashboard import SsoDashboard
from pages.standups import Standups
from pages.testrp import TestRp
from tests import conftest


class TestLogin:

    @pytest.mark.parametrize('url', ['https://web-remo-staging.production.paas.mozilla.community/',
                                     'https://reps.mozilla.org/'])
    def test_login_reps(self, selenium, ldap, url, counter_api):
        test = Reps(selenium, url)
        test.click_login_button()
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        if two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        assert test.is_logout_button_displayed
        test.click_logout()

    def test_login_slack(self, selenium, ldap, urls, counter_api):
        test = Slack(selenium, urls['slack'])
        test.click_sign_in_button()
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        while two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        assert test.is_username_displayed
        test.logout()

    @pytest.mark.parametrize('url', ['https://moderator-staging.production.paas.mozilla.community/',
                                     'https://moderator.mozilla.org/'])
    def test_login_moderator(self, selenium, ldap, url, counter_api):
        test = Moderator(selenium, url)
        test.click_sign_in_button()
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        if two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        assert test.is_logout_button_displayed
        test.click_logout()

    def test_login_standups(self, selenium, ldap, urls, counter_api):
        test = Standups(selenium, urls['standups'])
        test.click_sign_in()
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        if two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        assert test.is_user_menu_displayed
        test.click_logout()

    @pytest.mark.parametrize('url', ['https://discourse-staging.production.paas.mozilla.community',
                                     'https://discourse.mozilla.org/'])
    def test_login_discourse(self, selenium, ldap, url, counter_api):
        test = Discourse(selenium, url)
        test.click_login_in_button()
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        if two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        assert test.is_avatar_displayed
        test.logout()

    @pytest.mark.parametrize('url', ['https://web-mozillians-staging.production.paas.mozilla.community/',
                                     'https://mozillians.org/'])
    def test_login_mozillians(self, selenium, ldap, url, counter_api):
        test = Mozillians(selenium, url)
        test.click_sign_in_button()
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        if two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        assert test.is_username_displayed
        test.logout()

    @pytest.mark.parametrize('url', ['https://sso.allizom.org/', 'https://sso.mozilla.com/'])
    def test_login_sso(self, selenium, ldap, url, counter_api):
        test = SsoDashboard(selenium, url)
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        if two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        assert test.is_profile_icon_displayed
        test.logout()

    @pytest.mark.parametrize('url', ['https://mozillastage.service-now.com/', 'https://mozillaupgrade.service-now.com/',
                                     'https://mozillatest.service-now.com/', 'https://mozilladev.service-now.com/',
                                     'https://mozilla.service-now.com/'])
    def test_login_servicenow(self, selenium, ldap, url, counter_api):
        test = ServiceNow(selenium, url)
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        if two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        assert test.is_profile_icon_displayed
        test.logout()

    def test_login_biztera(self, selenium, ldap, urls, counter_api):
        test = Biztera(selenium, urls['biztera'])
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        if two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        assert test.is_name_displayed
        test.logout()

    def test_login_selfservice_mig(self, selenium, ldap, urls, counter_api):
        test = SelfServiceMig(selenium, urls['selfservice_mig'])
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        if two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        assert test.user_email_locator[:-1] == ldap['email']

    def test_login_testrp(self, selenium, ldap, urls, counter_api):
        test = TestRp(selenium, urls['testrp'])
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        if two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        assert test.is_logout_button_displayed
        test.click_logout()

    @pytest.mark.parametrize('url', ['https://phonebook.allizom.org/', 'https://phonebook.mozilla.org/'])
    def test_login_phonebook(self, selenium, ldap, url, counter_api):
        test = Phonebook(selenium, url)
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        if two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        assert test.is_search_region_displayed

    def test_login_mozdatacollective(self, selenium, ldap, urls, counter_api):
        test = MozDataCollective(selenium, urls['mozdatacollective'])
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        if two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        assert test.is_user_menu_displayed
        test.sign_out()

    @pytest.mark.parametrize('url', ['https://mana.allizom.org/', 'https://mana.mozilla.org/'])
    def test_login_mana(self, selenium, ldap, url, counter_api):
        test = Mana(selenium, url)
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        if two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        assert test.is_user_menu_displayed
        test.logout()

    def test_login_smartsheet(self, selenium, ldap, urls, counter_api):
        test = Smartsheet(selenium, urls['smartsheet'])
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        if two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        assert test.is_user_menu_displayed
        test.logout()

    def test_login_greenhouse(self, selenium, ldap, urls, counter_api):
        test = Greenhouse(selenium, urls['greenhouse'])
        two_factor_authentication = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        if two_factor_authentication.is_error_message_displayed:
            two_factor_authentication.enter_passcode(conftest.passcode(ldap['secret_seed'], counter_api))
        assert test.is_support_link_displayed
        test.sign_out()
