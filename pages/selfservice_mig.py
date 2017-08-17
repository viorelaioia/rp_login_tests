from pages.auth0 import Auth0
from pages.base import Base
from pages.two_factor_authentication import TwoFactorAuthentication


class SelfServiceMig(Base):

    def __init__(self, selenium, url):
        super(SelfServiceMig, self).__init__(selenium)
        self.go_to_url(url)

    def login_with_ldap(self, email, password):
        auth = Auth0(self.selenium)
        auth.login_with_ldap(email, password, ldap_only=True)
        return TwoFactorAuthentication(self.selenium)
