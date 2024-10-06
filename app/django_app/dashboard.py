"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'app.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import gettext_lazy as _
from grappelli.dashboard import Dashboard, modules


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        # append a group for "Administration" & "Applications"
        self.children.append(
            modules.Group(
                _("Administration & Applications"),
                column=1,
                collapsible=True,
                children=[
                    modules.AppList(
                        _("Administration"),
                        column=1,
                        collapsible=False,
                        models=("django.contrib.*",),
                    ),
                    modules.AppList(
                        _("Applications"),
                        column=1,
                        css_classes=("collapse closed",),
                        exclude=("django.contrib.*",),
                    ),
                ],
            )
        )

        # append another link list module for "support".
        self.children.append(
            modules.LinkList(
                _("Support"),
                column=2,
                children=[
                    {
                        "title": _("Project Documentation"),
                        "url": "https://github.com/AlexanderZug/Blog-Api",
                        "external": True,
                    },
                ],
            )
        )

        # append a recent actions module
        self.children.append(
            modules.RecentActions(
                _("Recent actions"),
                limit=5,
                collapsible=False,
                column=3,
            )
        )
