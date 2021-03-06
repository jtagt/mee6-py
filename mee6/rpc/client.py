from mee6.rpc.http import HTTPClient
from mee6.exceptions import RPCException
from mee6.types import Guild, Member
from mee6.utils import get


class RPCClient:
    def __init__(self):
        self.http = HTTPClient()

    def get_guild(self, guild):
        guild_id = get(guild, 'id', guild)
        path = 'guild/{}'.format(guild_id)

        try:
            r = self.http.get(path)
        except RPCException as e:
            if e.status_code == 404:
                return None
            raise e

        payload = r.json()
        return Guild(**payload)

    def get_guild_members(self, guild):
        guild_id = get(guild, 'id', guild)
        path = 'guild/{}/members'.format(guild_id)

        try:
            r = self.http.get(path)
        except RPCException as e:
            if e.status_code == 404:
                return None
            raise e

        payload = r.json()
        return [Member(**m) for m in payload.values()]

    def get_guild_member(self, guild, member):
        guild_id = get(guild, 'id', guild)
        member_id = get(member, 'id', member)
        path = 'guild/{}/members/{}'.format(guild_id, member_id)

        try:
            r = self.http.get(path)
        except RPCException as e:
            if e.status_code == 404:
                return None
            raise e

        payload = r.json()
        return Member(**payload)

    def voice_connect(self, guild, channel):
        guild_id = get(guild, 'id', guild)
        channel_id = get(channel, 'id', channel)
        path = 'guild/{}/voice_connect/{}'.format(guild_id, channel_id)

        try:
            r = self.http.get(path)
        except RPCException as e:
            if e.status_code == 404:
                return None
            raise e

        return True

    def voice_play(self, guild, url):
        guild_id = get(guild, 'id', guild)
        path = 'guild/{}/voice_play'.format(guild_id)

        json_body = {'url': url}
        try:
            r = self.http.post(path, json=json_body)
        except RPCException as e:
            if e.status_code == 404:
                return None
            raise e

        return True

    def voice_stop(self, guild):
        guild_id = get(guild, 'id', guild)
        path = 'guild/{}/voice_stop'.format(guild_id)

        try:
            r = self.http.get(path)
        except RPCException as e:
            if e.status_code == 404:
                return None
            raise e

        return True

    def voice_disconnect(self, guild):
        guild_id = get(guild, 'id', guild)
        path = 'guild/{}/voice_disconnect'.format(guild_id)

        try:
            r = self.http.get(path)
        except RPCException as e:
            if e.status_code == 404:
                return None
            raise e

        return True

