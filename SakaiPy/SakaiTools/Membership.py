#!/usr/bin/python
# -*- coding: utf-8 -*-
from SakaiPy import SakaiSession

class Membership(object):
    """
    Contains logic for the Sakai Membership API endpoint.

    More information about the RESTful interface can be found at:
    https://trunk-mysql.nightly.sakaiproject.org/direct/membership/describe
    """

    def __init__(self, sess):
        """
        Creates a standalone Membershop Object
        :param sess: The Session to use.
        :return: A Membership object
        """
        assert isinstance(sess, SakaiSession.SakaiSession)
        self.session = sess

    def getUserMembership(self, user=None, includeSites=True, includeGroups=False,
                         includeMemberDetails=True, role=None):
        """
        Get a list of all site memberships for a user
        :param user: The ID of the user to retrieve. Defaults to the current.
        :param includeSites: True to include sites in the list (default: True)
        :param includeGroups: True to include groups in the list (default: False)
        :param includeMemberDetails: True to include full member details. It
                                     cannot be used with includeGroups=true
                                     (default: True)
        :param role: Restrict the list to a member role type
        """
        params_temp = {
            'user': user,
            'includeSites': includeSites,
            'includeGroups': includeGroups,
            'includeMemberDetails': includeMemberDetails,
            'role': role
        }
        if includeGroups:
            includeMemberDetails = False
        # Do not submit None values
        params = {k: v for (k, v) in params_temp.items() if params_temp[k] is not None }

        return self.session.executeRequest('GET', '/membership.json', params=params)

    def getAllMembershipForSite(self, siteid):
        """
        Get a list of all members of a site
        :param siteid: The ID of the site
        """
        return self.session.executeRequest('GET',
                                           '/membership/site/{0}.json'.format(siteid))

    def getUserRoles(self, uid=None):
        """
        Get an user's role in all joined sites
        :param uid: The user's ID. Defaults to the current user
        """
        if uid is None:
            return self.session.executeRequest('GET', '/membership.json')
        else:
            return self.session.executeRequest('GET', '/membership/{0}.json'.format(uid))

    def getAllMembershipForGroup(self, groupid):
        """
        Get a list of all members of a group
        :param groupid: The ID of the group
        """
        return self.session.executeRequest('GET',
                                           '/membership/group/{0}.json'.format(groupid))
