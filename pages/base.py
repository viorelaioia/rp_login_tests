from pages.auth0 import Auth0
from pages.page import Page
from pages.two_factor_authentication import TwoFactorAuthentication


class Base(Page):

    def __init__(self, selenium, url):
        super(Base, self).__init__(selenium)
        self.go_to_url(url)

    def login_with_ldap(self, email, password):
        auth = Auth0(self.selenium)
        auth.login_with_ldap(email, password)
        return TwoFactorAuthentication(self.selenium)
