DATABASE_SETTINGS = {
    "DB": "weltcharity"
}

# This is our secret key that will be used for signing our session cookies.
# With a signed session cookie the user can view a cookie's data, but they
# cannot change any data in the cookie.  To be even more safe we will not
# store any form of sensitive data in the cookies to begin with.  Each release,
# even hotfixes, we will change this secret key.  This will mean that users will have
# to sign in again, but it will be result in more security.
SEC_KEY = "JdsDSa(*&)JKLDRT$%^&jkljsd@#$)(*f*(FHu94)jf8"

ROLES = {
	"admin": "AdministrationRole",
	"mod": "ModeratorRole"
}