#!/usr/bin/python
# -*- coding: utf-8 -*-
import SakaiPy.RequestGenerator



class Forums(object):

    def __init__(self, rq):
        self.requester = rq

    def getForumsForSite(self, siteid):
        return self.requester.executeRequest('/direct/forums/site/{0}.json'.format(siteid))

    def getAllTopicsForForum(self, siteid, forumid):
        return self.requester.executeRequest('/direct/forums/site/{0}/forum/{1}.json'.format(siteid,
                forumid))

    def getAllConversationsForTopic(
        self,
        siteid,
        forumid,
        topicid,
        ):
        return self.requester.executeRequest('/direct/forums/site/{0}/forum/{1}/topic/{2}.json'.format(siteid,
                forumid, topicid))

    def getAllMessagesForConversation(
        self,
        siteid,
        forumid,
        topicid,
        messageid,
        ):
        return self.requester.executeRequest('/direct/forums/site/{0}/forum/{1}/topic/{2}/message/{3}.json'.format(siteid,
                forumid, topicid, messageid))



			