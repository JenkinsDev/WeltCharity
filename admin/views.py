from flask import Blueprint, request, redirect, render_template, session, url_for
from flask.views import MethodView
from listings.models import Listing, Comment
from weltcharity.models import User, ContactInfo, Address


admin = Blueprint('admin', __name__, template_folder='../templates/admin')

class BaseAdminView(MethodView):
    """ The BaseAdminView class will handle the main admin dashboard page
    and logging the user in as an admin.  We will require that users do have
    the admin role before allowing them into the admin dashboard.
    """
    def get(self):
        user_id = session.get('user_id')
        if not user_id:
            return redirect('login')
        return render_template('admin_base.html', user=User.objects.get(id=user_id))


admin.add_url_rule('/admin-dashboard/', view_func=BaseAdminView.as_view('admin.base'))